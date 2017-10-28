# -*- coding: utf-8 -*-

from test_cases import url, get_xmlschema


class Case(object):
    def __init__(
            self, url_params, status_code, headers, xsd_path
    ):
        self.url_parameters = url_params
        self.exp_status_code = status_code
        self.exp_headers = headers
        self.xml_schema = get_xmlschema(xsd_path)
        self.api_url = self.test_url

    @property
    def test_url(self):
        api_url = '{}{}'.format(url, self.url_parameters)
        return api_url


valid_case_with_objects = Case(
    url_params=u'31.17268681526184,52.56401245027321,'
               u'31.17742896080017,52.56634718820995',
    status_code=200,
    headers={
        'Cache-Control': 'private, max-age=0, must-revalidate',
        'Transfer-Encoding': 'chunked',
        'Keep-Alive': 'timeout=5, max=100',
        'Content-Disposition': 'attachment; filename="map.osm"',
        'Content-Type': 'text/xml; charset=utf-8',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'Keep-Alive',
        'Content-Encoding': 'gzip',
    },
    xsd_path='../test_cases/valid_case_1.xsd'
)

valid_case_without_objects = Case(
    url_params=u'-21.12396240234375,42.02685388718981,'
               u'-20.637817382812496,42.36869093640926',
    status_code=200,
    headers={
        'Content-Disposition': 'attachment; filename="map.osm"',
        'Content-Encoding': 'gzip',
        'Transfer-Encoding': 'chunked',
        'Keep-Alive': 'timeout=5, max=100',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'Keep-Alive',
        'Cache-Control': 'private, max-age=0, must-revalidate',
        'Content-Type': 'text/xml; charset=utf-8'
    },
    xsd_path='../test_cases/valid_case_2.xsd'
)

# invalid_case_bbox_is_empty = Case(
#     url_params=u'',
#     status_code=400,
#     headers={
#         'Content-Length': '88',
#         'Cache-Control': 'no-cache',
#         'Server': 'Apache/2.4.18 (Ubuntu)',
#         'Connection': 'close',
#         'Error': 'The parameter bbox is required, and must be '
#                  'of the form min_lon,min_lat,max_lon,max_lat.',
#         'Content-Type': 'text/plain; charset=utf-8'
#     }
# )
#
# invalid_case_too_many_nodes = Case(
#     url_params=u'27.,53.85379229563698,'
#                u'27.671985626220707,53.886459293813054',
#     status_code=400,
#     headers={
#         'Content-Length': '95',
#         'Content-Disposition': 'attachment; filename="map.osm"',
#         'Cache-Control': 'no-cache',
#         'Server': 'Apache/2.4.18 (Ubuntu)',
#         'Connection': 'close',
#         'Error': 'You requested too many nodes (limit is 50000).'
#                  ' Either request a smaller area, or use planet.osm',
#         'Content-Type': 'text/plain; charset=utf-8'
#     }
# )
#
# invalid_case_wrong_param_1 = Case(
#     url_params=u'100.61649608612061,53.85379229563698,'
#                u'27.671985626220707,53.886459293813054',
#     status_code=400,
#     headers={
#         'Content-Length': '118',
#         'Cache-Control': 'no-cache',
#         'Server': 'Apache/2.4.18 (Ubuntu)',
#         'Connection': 'close',
#         'Error': 'The latitudes must be between -90 and 90,'
#                  ' longitudes between -180 and 180 and the minima must be less than the maxima.',
#         'Content-Type': 'text/plain; charset=utf-8'
#     }
# )
#
# invalid_case_wrong_param_2 = Case(
#     url_params=u'27.61649608612061,53.85379229563698,'
#                u'27.671985626220707,52.886459293813054',
#     status_code=400,
#     headers={
#         'Content-Length': '118',
#         'Cache-Control': 'no-cache',
#         'Server': 'Apache/2.4.18 (Ubuntu)',
#         'Connection': 'close',
#         'Error': 'The latitudes must be between -90 and 90,'
#                  ' longitudes between -180 and 180 and the minima must be less than the maxima.',
#         'Content-Type': 'text/plain; charset=utf-8'
#     }
# )
#
# invalid_case_bbox_size_overhead = Case(
#     url_params=u'13.359375,-81.82379431564337,'
#                u'16.875,83.97925949886205',
#     status_code=400,
#     headers={
#         'Content-Length': '111',
#         'Cache-Control': 'no-cache',
#         'Server': 'Apache/2.4.18 (Ubuntu)',
#         'Connection': 'close',
#         'Error': 'The maximum bbox size is 0.25, and your request was too large.'
#                  ' Either request a smaller area, or use planet.osm',
#         'Content-Type': 'text/plain; charset=utf-8'
#     }
# )

test_cases = [valid_case_with_objects, valid_case_without_objects]
