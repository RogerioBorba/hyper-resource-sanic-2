import shapely
from shapely.geometry import Point, LineString, Polygon, MultiPolygon, MultiPoint, MultiLineString
from shapely.geometry import shape, GeometryCollection
from shapely.geometry.base import BaseGeometry
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import io


def set_html_variables(html_content: str, title:str, jsonld: str) -> str:
    TITLE_VARIABLE = "{{title}}"
    JSONLD_VARIABLE = "{{jsonld}}"
    content = html_content.replace(TITLE_VARIABLE, title)

    content = content.replace( JSONLD_VARIABLE, jsonld )
    return content


def geojson_to_geometry_collection(geoJson) -> GeometryCollection:
    features = geoJson["features"]
    return GeometryCollection([shape(feature["geometry"]).buffer(0) for feature in features])


def geojson_to_geometries(geoJson) -> list[BaseGeometry]:
    features = geoJson["features"]
    return [shape(feature["geometry"]).buffer(0) for feature in features]


async def linestring_as_figure(geometries: list, extent: list[float]):
    ax = plt.axes(projection=ccrs.PlateCarree(),  frameon=False)
    ax.set_extent(extent, ccrs.PlateCarree())
    ax.patch.set_visible(False)
    ax.add_geometries(geometries, ccrs.PlateCarree(), facecolor='none',  edgecolor="black")
    b = io.BytesIO()
    plt.savefig(b, format='png')
    plt.close()
    return b.getvalue()


async def polygon_as_figure(geometries: list, extent: list[float]):
    ax = plt.axes(projection=ccrs.PlateCarree(), frameon=False)
    ax.set_extent(extent, ccrs.PlateCarree())
    ax.add_geometries(geometries, ccrs.PlateCarree(), facecolor='#C8A2C8', alpha=0.5, edgecolor="black")
    b = io.BytesIO()
    plt.savefig(b, format='png')
    plt.close()
    return b.getvalue()


async def point_as_figure(geometries: list, extent: list[float]):
    ax = plt.axes(projection=ccrs.PlateCarree(), frameon=False)
    ax.set_extent(extent, ccrs.PlateCarree())
    for point in geometries:
        plt.plot(point.x, point.y,  markersize=1, marker='o', color='b', transform=ccrs.PlateCarree())
    b = io.BytesIO()
    plt.savefig(b, format='png')
    plt.close()
    return b.getvalue()


async def geometry_as_figure(geometries: list[shapely.Geometry], extent):
    type_geometry = type(geometries[0])
    if type_geometry == MultiPolygon or type_geometry == Polygon:
        return await polygon_as_figure(geometries, extent)
    elif type_geometry == LineString or type_geometry == MultiLineString:
        return await linestring_as_figure(geometries, extent)
    elif type_geometry == Point or type_geometry == MultiPoint:
        return await point_as_figure(geometries, extent)
