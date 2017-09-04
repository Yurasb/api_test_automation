# -*- coding: utf-8 -*-


class Case(object):
    def __init__(
            self, url_params, status_code, headers, xsd
    ):
        self.url_parameters = url_params
        self.exp_status_code = status_code
        self.exp_headers = headers
        self.xsd = xsd


valid_case = Case(
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
        'Date': 'Sun, 20 Aug 2017 20:29:37 GMT'
    },
    xsd=open('../test_cases/valid_case.xsd', 'r')
)
