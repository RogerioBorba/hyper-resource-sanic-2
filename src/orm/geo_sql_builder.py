from geoalchemy2 import WKBElement
from shapely import wkb, Geometry
from sqlalchemy import Row

from src.hyper_resource.abstract_resource import AbstractResource
from src.orm.sa_sql_builder import SASQLBuilder


class GEOSASQLBuilder(SASQLBuilder):
    def __init__(self, resource: AbstractResource, path: str, prefix_column: str | None = None, delimiter: str = '/*/'):
        super().__init__(resource=resource, path=path, prefix_column=prefix_column, delimiter=delimiter)


    def geom_attribute_name(self) -> str:
        """Returns the name of the geo attribute
        Returns (str)
        """
        return self.entity_class().geo_attribute_name()

    def projection_has_geometry(self) -> bool:
        proj_list: list = self.get_projection()
        projection: list[str] = [obj._label for obj in proj_list]
        geo_name: str = self.geom_attribute_name()
        return geo_name in projection

    async def rows_as_dict(self, rows):
        if len(rows) == 0:
            return []
        response_data: list = []
        geom_attribute: str = self.geom_attribute_name()
        a_row: Row = rows[0]
        if geom_attribute not in a_row._fields:
            return await super().rows_as_dict(rows)
        feature_collection = {"type": "FeatureCollection", }
        try:
            for row in rows:
                row_dict = await self.dialect_db().convert_row_to_dict(row)
                feature = {"type": "Feature"}
                geom_value: WKBElement = row_dict[geom_attribute]
                geometry: Geometry = wkb.loads(bytes(geom_value.data))
                geometry_as_dict: dict = geometry.__geo_interface__  # json.loads(row_dict[geom_attribute])
                row_dict.pop(geom_attribute, None)
                feature["geometry"] = geometry_as_dict
                feature["properties"] = row_dict
                response_data.append(feature)
        except Exception as err:
            print(err)
            raise
        feature_collection["features"] = response_data
        return feature_collection

    async def fetch_all_as_json(self) -> object:
        """Execute statement from path adn returns a dict (json)
        Returns
            (dict) - dict (json)
        """
        if self.has_only_one_aggregate_math_function():
            res = await self.fetch_one()
            return res[0] if res is not None else 0
        else:
            rows = await self.fetch_all()
            return await self.rows_as_dict(rows)

    async def fetch_all_as_geobuf(self):

        col_name: str = self.column_name_given(self.geom_attribute_name())
        full_column_name: str = f'{self.entity_class().full_table_name()}.{col_name}'
        sub_query: str = self.query()
        new_sub_query: str = sub_query.replace(f'ST_AsEWKB({full_column_name})', full_column_name)
        a_query: str = self.dialect_db().geobuf_query(new_sub_query)
        rows = await self.dialect_db().fetch_all_by(a_query)
        if rows:
            row = rows[0]
            return row._mapping['st_asgeobuf']
        return None

    async def fetch_all_as_flatgeobuffers(self):
        sub_query: str = self.query()
        col_name: str = self.column_name_given(self.geom_attribute_name())
        full_column_name: str = f'{self.entity_class().full_table_name()}.{col_name}'
        new_sub_query: str = sub_query.replace(f'ST_AsEWKB({full_column_name})', full_column_name)
        a_query: str = self.dialect_db().flatgeobuf_query(new_sub_query)
        rows = await self.dialect_db().fetch_all_by(a_query)
        if len(rows):
            row = rows[0]
            return row._mapping['st_asflatgeobuf']
        return None

