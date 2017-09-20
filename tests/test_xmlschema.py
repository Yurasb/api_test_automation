# -*- coding: utf-8 -*-
import requests

from tests import get_doc


def test_xml_schema(get_case):
    response = requests.get(get_case.api_url)
    body = response.content
    get_case.xsd.assertValid(get_doc(body))
