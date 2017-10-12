# -*- coding: utf-8 -*-

import requests

from tests import parse_body


def test_xml_schema(get_case):
    response = requests.get(get_case.api_url)
    body = response.content
    get_case.xml_schema.assertValid(parse_body(body))
