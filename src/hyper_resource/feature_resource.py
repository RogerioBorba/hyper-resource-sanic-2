import json
import os
import urllib
from typing import Optional, Any
import time
import shapely
from sanic import response
from shapely import wkb
from shapely.geometry import Point, LineString, Polygon, MultiPolygon, MultiPoint, MultiLineString
from sqlalchemy import Row
from settings import SOURCE_DIR
from src.hyper_resource import feature_utils
from src.hyper_resource.common_resource import *
from src.hyper_resource.feature_utils import polygon_as_figure, linestring_as_figure, point_as_figure, \
    geometry_as_figure
from src.hyper_resource.spatial_resource import SpatialResource
import sanic

from src.orm.database_postgis import DialectDbPostgis

MIME_TYPE_JSONLD = "application/ld+json"


class FeatureResource(SpatialResource):
    def __init__(self, request):
        super().__init__(request)

    def dialect_DB(self) -> DialectDbPostgis:
        return DialectDbPostgis(self.request.app.ctx.db, self.metadata_table(), self.entity_class())

    def serialize_as_geojson(self, raw_data) -> dict:
        geometry = raw_data[self.dialect_DB().get_geom_column()]
        del raw_data[self.dialect_DB().get_geom_column()]
        serialized = {
            "type": "Feature",
            "geometry": geometry,
            "properties": raw_data
        }
        return serialized

    async def get_representation_old(self, id_or_key_value):
        data = await self.dialect_DB().fetch_one_as_json(id_or_key_value)
        serialized = self.serialize_as_geojson(data)
        return sanic.response.json(serialized)

    """"
    async def get_html_representation(self, id_or_key_value):
        row = await self.dialect_DB().fetch_one_as_json(id_or_key_value)
        if row is None:
            return sanic.response.json("The resource was not found.", status=404)
        return sanic.response.text(row, content_type='application/json')
    """

    def set_html_variables(self, html_content: str) -> str:
        return feature_utils.set_html_variables(
            html_content, self.metadata_table().name,
            json.dumps(
                self.context_class(
                    self.dialect_DB(),
                    self.metadata_table(),
                    self.entity_class()
                ).get_basic_context(),
                indent=2
            )
        )

    async def get_html_representation(self, id_or_key_value):
        html_filepath = os.path.join(SOURCE_DIR, "hyper_resource", "templates", "basic_geo.html")
        with open(html_filepath, "r") as body:
            html_content = body.read()
            content = self.set_html_variables(html_content)
            return sanic.response.html(content, 200)

    async def get_json_representation(self, id_or_key_value):
        model = await self.dialect_DB().fetch_one_model(id_or_key_value)
        if model is None:
            return sanic.response.json("The resource was not found.", status=404)
        j_d = model.json_dict(model.__class__.attribute_names())
        return sanic.response.json(j_d)

    async def get_image_representation(self, id_or_key_value):

        if isinstance(id_or_key_value, tuple):
            tup = id_or_key_value
        else:
            tup = (self.entity_class().primary_key(), id_or_key_value)

        a_query: str = self.dialect_DB().basic_select_one_by_key_value(tup)
        query: str = self.dialect_DB().wkb_query(a_query)
        rows: list[Row] = await self.dialect_DB().fetch_all_by(query)
        geometries = [shapely.from_wkb(row)[0] for row in rows]
        if len(geometries) == 0:
            return sanic.response.raw({}, content_type=CONTENT_TYPE_JSON)
        extent = await self.dialect_DB().extent(query)

        res = await geometry_as_figure(geometries, extent)
        return sanic.response.raw(res, content_type=CONTENT_TYPE_IMAGE_PNG)

    async def get_representation(self, id_or_key_value: Optional[Any] = None):
        if type(id_or_key_value) == tuple:
            self.entity_class()
        try:
            accept = self.request.headers['accept']
            if CONTENT_TYPE_HTML in accept:
                return await self.get_html_representation(id_or_key_value)
            elif CONTENT_TYPE_WKB in accept:
                return await self.get_wkb_representation(id_or_key_value)
            elif CONTENT_TYPE_IMAGE_PNG in accept:
                return await self.get_image_representation(id_or_key_value)
            else:
                return await self.get_json_representation(id_or_key_value)
        except (Exception, SyntaxError, NameError) as err:
            print(err)
            return sanic.response.json({"Error": f"{err}"})

    async def get_representation_given_path(self, id_or_key_value, a_path: str):
        try:
            a_path = urllib.parse.unquote(a_path)
            accept = self.request.headers['accept']
            if CONTENT_TYPE_HTML in accept:
                return await self.get_html_representation_given_path(id_or_key_value, a_path)
            elif CONTENT_TYPE_GEOBUF in accept:
                return await self.get_geobuf_representation_given_path(id_or_key_value, a_path)
            elif CONTENT_TYPE_JSON in accept:
                return await self.get_json_representation_given_path(id_or_key_value, a_path)
            elif CONTENT_TYPE_WKB in accept:
                return await self.get_wkb_representation_given_path(id_or_key_value, a_path)

            return await self.get_json_representation_given_path(id_or_key_value, a_path)
        except (Exception, SyntaxError, NameError) as err:
            print(err)
            return sanic.response.json({"Error": f"{err}"})

    async def get_html_representation_given_path(self, id_or_key_value, a_path):
        html_filepath = os.path.join(SOURCE_DIR, "hyper_resource", "templates", "basic_geo.html")
        with open(html_filepath, "r") as body:
            html_content = body.read()
            content = self.set_html_variables(html_content)
            return sanic.response.html(content, 200)

    async def get_json_representation_given_path(self, id_or_key_value, a_path):

        try:
            self.entity_class().validate_path(a_path)
            if self.entity_class().is_only_attribute_list_from_path(a_path):
                model = await self.dialect_DB().fetch_one_model(id_or_key_value)
                attributes_from_path = [att.strip() for att in a_path.split('/')[0].split(',')]
                dic = model.json_dict(attributes_from_path)
                res = dic if len(dic) > 1 else dic.popitem()[1]
                return sanic.response.json(res)
            elif self.entity_class().starts_by_one_attribute_with_functions(a_path):
                model = await self.dialect_DB().fetch_one_model(id_or_key_value)
                result = await model.execute_attribute_given(a_path)
                if isinstance(result, bytes):
                    return sanic.response.raw(result, content_type=CONTENT_TYPE_WKB)
                res = convert_to_json(result)
                return sanic.response.json(res)
            else:
                start = time.time()
                print(f" Start time: {start} load from database")
                model = await self.dialect_DB().fetch_one_model(id_or_key_value)
                end = time.time()
                print(f"time: {end - start} to load from database")
                start = time.time()
                print(f" Start execute function load --- time: {start} in python")
                res = await model.execute_function_given(a_path)
                end = time.time()
                print(f"Execute function End time: {end - start} in python")
                if isinstance(res, dict):
                    res = model.json_dict(list(res.keys()))
                    return sanic.response.json(res)
                return sanic.response.json(convert_to_json(res))

        except (Exception, AttributeError, SyntaxError, NameError) as err:
            print(err)
            return sanic.response.json({"Error": f"{err}"}, status=400)

    async def get_wkb_representation(self, id_or_key_value):
        try:
            model = await self.dialect_DB().fetch_one_model(id_or_key_value)
            result = model.get_geom()
            return sanic.response.raw(result, content_type=CONTENT_TYPE_WKB)
        except (Exception, SyntaxError, NameError) as err:
            print(err)
            return sanic.response.json({"Error": f"{err}"}, status=400)

    async def get_wkb_representation_given_path(self, id_or_key_value, a_path: str):
        try:
            model = await self.dialect_DB().fetch_one_model(id_or_key_value)
            method_name: str = a_path.split('/')[0]
            if self.entity_class().starts_by_one_attribute_with_functions(a_path):
                if model.has_action(method_name):
                    a_path = model.geo_attribute_name() + '/' + a_path
                res = await model.execute_attribute_given(a_path)
                result = res.wkb
            elif model.has_action(method_name):
                res = await model.execute_attribute_given(model.geo_attribute_name() + '/' + a_path)
                result = res.wkb
            else:
                result = (wkb.loads(model.get_geom(), hex=True)).wkb
            return sanic.response.raw(result, content_type=CONTENT_TYPE_WKB)
        except (Exception, SyntaxError, NameError) as err:
            print(err)
            return sanic.response.json({"Error": f"{err}"}, status=400)

    async def options(self, *args, **kwargs):
        context = self.context_class(self.dialect_DB(), self.metadata_table(), self.entity_class())
        return response.json(context.get_basic_context(), content_type=CONTENT_TYPE_LD_JSON)

    async def options_given_path(self, id, path):
        context = self.context_class(self.dialect_DB(), self.metadata_table(), self.entity_class())

        if path[-1] == '/':  # Removes trail slash
            path = path[:-1]

        operation_name_or_attribute_comma = path.split('/')[0].strip().lower()
        att_names = set(operation_name_or_attribute_comma.split(','))
        diff_atts = att_names.difference(set(self.attribute_names()))

        if len(diff_atts) == 1:
            return sanic.response.json(f"The operation or attribute in this {list(diff_atts)} does not exists",
                                       status=400)
        elif len(diff_atts) > 1:
            return sanic.response.json(f"The operations or attributes {list(diff_atts)} do not exists", status=400)

        return response.json(context.get_projection_context(list(att_names)), content_type=CONTENT_TYPE_LD_JSON)
