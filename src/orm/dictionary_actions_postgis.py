from geoalchemy2 import Geometry
from typing import Dict

from src.hyper_resource.common_resource import CONTENT_TYPE_GEOJSON, CONTENT_TYPE_WKT, CONTENT_TYPE_GEOBUF, CONTENT_TYPE_WKB, CONTENT_TYPE_EWKB
from src.orm.action_type import ActionFunction, ParamAction, ActionAttribute

dic_geometry_action = {
        'area': ActionFunction('area', 'ST_Area', float, [], 'Returns the area using the current coordinate system', 'http://a-server/apis/states/RJ/geom/area/'),
        'azimuth': ActionFunction('azimuth', 'ST_Azimuth', float,  [ParamAction('other', Geometry)], 'Returns the azimuth in radians of the line segment defined by the given point geometries, or NULL if the two points are coincident.', 'http://a-server/apis/states/RJ/geom/azimuth/Point(23,-23)'),
        'minimum-bounding-circle': ActionFunction('minimum-bounding-circle', 'ST_MinimumBoundingCircle', Geometry,  [], 'Returns the azimuth in radians of the line segment defined by the given point geometries, or NULL if the two points are coincident.', 'http://a-server/apis/states/RJ/geom/azimuth/Point(23,-23)'),
        'boundary': ActionFunction('boundary', 'ST_Boundary', Geometry,[], 'Returns the closure of the combinatorial boundary of this Geometry.'),
        'buffer': ActionFunction('buffer', 'ST_Buffer', Geometry, [ParamAction('distance', float), ParamAction('resolution', int, False, 16),ParamAction('cap_style', int, False, 1), ParamAction('join_style', int, False, 1), ParamAction('mitre_limit', float, False, 5.0),ParamAction('single_sided', bool, False, False)],'Returns a Geometry that represents all points whose distance from this geometry is less than or equal to the given width.', 'http://a-server/apis/states/RJ/geom/buffer/1.2/'),
        'centroid': ActionFunction('centroid', 'ST_Centroid', Geometry, [],'Computes a point which is the geometric center of mass of a geometry.' ),
        'convex_hull': ActionFunction('convex_hull', 'ST_ConvexHull', Geometry,[],'Computes the convex hull of a geometry. The convex hull is the smallest convex geometry that encloses all geometries in the input.'),
        'difference': ActionFunction('difference', 'ST_Difference', Geometry, [ParamAction('other', Geometry)],'Returns a geometry representing the part of geometry A that does not intersect geometry B.'),
        'disjoint': ActionFunction('disjoint', 'ST_Disjoint', Geometry, [ParamAction('other', Geometry)], 'Disjoint implies false for spatial intersection.'),
        'distance': ActionFunction('distance', 'ST_Distance', float, [ParamAction('other', Geometry)], 'For geometry types returns the minimum 2D Cartesian (planar) distance between two geometries, in projected units (spatial ref units).'),
        'envelope': ActionAttribute('envelope', 'ST_Envelope', Geometry, 'Returns the double-precision (float8) minimum bounding box for the supplied geometry, as a geometry.'),
        'geometryType': ActionFunction('geometryType', 'ST_GeometryType', str, 'Returns the type of the geometry as a string.'),
        'intersection': ActionFunction('intersection', 'ST_Intersection',  Geometry, [ParamAction('other', Geometry)], 'Returns a geometry representing the point-set intersection of two geometries.'),
        'simplify': ActionFunction('simplify', 'ST_Simplify',  Geometry, [ParamAction('tolerance', float), ParamAction('preserve_topology', bool)], 'Returns a "simplified" version of the given geometry using the Douglas-Peucker algorithm.'),
        'symmetric_difference': ActionFunction('symmetric_difference', 'ST_SymDifference',  Geometry, [ParamAction('other', Geometry)], 'Returns a geometry representing the portions of geometries A and B that do not intersect.'),
        'transform': ActionFunction('transform', 'ST_Transform',  Geometry, [ParamAction('srid', int)], 'Returns a new geometry with its coordinates transformed to a different spatial reference system.'),
        'wkb': ActionFunction('wkb', ' ST_AsBinary', str,[ParamAction('other', Geometry)]),
        'wkt': ActionFunction('wkt', 'ST_AsText', str, [ParamAction('other', Geometry)])
}
representations = [CONTENT_TYPE_GEOJSON, CONTENT_TYPE_GEOBUF]
dic_spatial_lookup_action: Dict[str, ActionFunction] = {
    'bbcontains': ActionFunction('bbcontains', '~',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box completely contains the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/bbcontains/Point(22, 34)',
                               representations),
    'bboverlaps': ActionFunction('bboverlaps',
                                 '&&',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box overlaps the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/bboverlaps/Point(22, 34)',
                               representations),
    'contained': ActionFunction('contained',
                                '@',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box is completely contained by the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/contained/POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))',
                               representations),
    'contains': ActionFunction('contains',
                               'ST_Contains',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field spatially contains the lookup geometry.',
                               'http://a-server/apis/states/contains/Point(22, 34)',
                               representations),
    'contains_properly': ActionFunction('contains_properly',
                                        'ST_ContainsProperly',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Returns true if the lookup geometry intersects the interior of the geometry field, but not the boundary (or exterior).',
                               'http://a-server/apis/states/contains_properly/Point(22, 34)',
                               representations),
    'coveredby': ActionFunction('coveredby',
                                'ST_CoveredBy',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if no point in the geometry field is outside the lookup geometry',
                               'http://a-server/apis/capitals/coveredby/POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))',
                               representations),
    'covers': ActionFunction('covers',
                             'ST_Covers',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if no point in the lookup geometry is outside the geometry field.',
                               'http://a-server/apis/states/covers/Point(22, 34)',
                               representations),
    'crosses': ActionFunction('crosses',
                              'ST_Crosses',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field spatially crosses the lookup geometry.',
                               'http://a-server/apis/railroads/crosses/Linestring(1.5 2.45,3.21 4)',
                               representations),
    'disjoint': ActionFunction('disjoint',
                               'ST_Disjoint',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field spatially crosses the lookup geometry.',
                               'http://a-server/apis/states/disjoint/Point(22, 34)',
                               representations),
    'equals': ActionFunction('equals',
                             'ST_Equals',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field is spatially equal to the lookup geometry.',
                               'http://a-server/apis/states/equals/Point(22, 34)',
                               representations),
    'same_as': ActionFunction('same_as',
                              '~=',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests equality of bounding boxes geometries.',
                               'http://a-server/apis/states/same_as/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'intersects': ActionFunction('intersects',
                                 'ST_Intersects',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field spatially intersects the lookup geometry.',
                               'http://a-server/apis/states/intersects/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'isvalid': ActionFunction('isvalid',
                              'ST_IsValid',
                               bool,
                               [],
                               'Tests if the geometry is valid.',
                               'http://a-server/apis/states/isvalid',
                               representations),
    'overlaps': ActionFunction('overlaps',
                               'ST_Overlaps',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field spatially overlaps the lookup geometry.',
                               'http://a-server/apis/states/overlaps/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'relate': ActionFunction('relate',
                             'ST_Relate',
                               bool,
                               [ParamAction('other', Geometry), ParamAction('pattern', str) ],
                               'Tests if the geometry field is spatially related to the lookup geometry by the values given in the given pattern.',
                               'http://a-server/apis/states/relate/Polygon((1 2,1 4,3 4,3 2,1 2))&"pattern"',
                               representations),
    'touches': ActionFunction('touches',
                              'ST_Touches',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field spatially touches the lookup geometry.',
                               'http://a-server/apis/states/touches/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'within': ActionFunction('within',
                             'ST_Within',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field is spatially within the lookup geometry.',
                               'http://a-server/apis/states/within/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'left': ActionFunction('left',
                           '<<',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box is strictly to the left of the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/left/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'right': ActionFunction('right',
                            '>>',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box is strictly to the right of the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/right/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'overlaps_left': ActionFunction('overlaps_left',
                                    '&<',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box overlaps or is to the left of the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/overlaps_left/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'overlaps_right': ActionFunction('overlaps_right',
                                     '&>',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box overlaps or is to the right of the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/overlaps_right/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'overlaps_above': ActionFunction('overlaps_above',
                                     '|&>',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box overlaps or is above the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/overlaps_above/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'overlaps_below': ActionFunction('overlaps_below',
                                     '&<|',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box overlaps or is below the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/overlaps_below/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'strictly_above': ActionFunction('strictly_above',
                                     '|>>',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box is strictly above the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/strictly_above/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'strictly_below': ActionFunction('strictly_below',
                                     '<<|',
                               bool,
                               [ParamAction('other', Geometry)],
                               'Tests if the geometry field’s bounding box is strictly below the lookup geometry’s bounding box.',
                               'http://a-server/apis/states/strictly_below/Polygon((1 2,1 4,3 4,3 2,1 2))',
                               representations),
    'dwithin': ActionFunction('dwithin',
                              'ST_DWithin',
                               bool,
                               [ParamAction('other', Geometry), ParamAction('distance_of_srid', float)],
                               'Returns true if the geometries are within a given distance.',
                               'http://a-server/apis/states/dwithin/Polygon((1 2,1 4,3 4,3 2,1 2))&5',
                               representations),

}
dic_spatial_aggregate_action: Dict[str, ActionFunction] = {

    'union': ActionFunction('union',
                            'ST_Union',
                               Geometry,
                               [],
                               'Unions the input geometries, merging geometry to produce a result geometry with no overlaps.',
                               'http://a-server/apis/states/union',
                               representations),
    'extent': ActionFunction('extent',
                             'ST_Extent',
                               Geometry,
                               [],
                               'Returns BBOX.',
                               'http://a-server/apis/states/extent',
                               representations),

}
dic_action = {**dic_geometry_action, **dic_spatial_lookup_action, **dic_spatial_aggregate_action}