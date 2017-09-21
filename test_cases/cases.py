# -*- coding: utf-8 -*-
from main import url
from test_cases import get_xmlschema


class Case(object):
    def __init__(
            self, url_params, status_code, headers, xsd_path
    ):
        self.url_parameters = url_params
        self.exp_status_code = status_code
        self.exp_headers = headers
        self.xsd = get_xmlschema(xsd_path)
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
        'Date': 'Sun, 20 Aug 2017 20:29:37 GMT'
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
        'Date': 'Thu, 21 Sep 2017 19:52:36 GMT',
        'Content-Type': 'text/xml; charset=utf-8'
    },
    xsd_path='../test_cases/valid_case_2.xsd'
)

test_cases = [valid_case_with_objects, valid_case_without_objects]
