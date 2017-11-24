# -*- coding: utf-8 -*-

import requests

from tests import parse_body


def test_xml_schema(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    body = response.content
    get_case.xml_schema.assertValid(parse_body(body))
