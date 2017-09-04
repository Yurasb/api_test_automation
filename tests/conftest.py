# -*- coding: utf-8 -*-


import pytest
import requests
from StringIO import StringIO
from lxml import etree
from main import url
from test_cases.test_cases import valid_case


@pytest.fixture(scope='function')
def case(request):
    case = valid_case
    return case


@pytest.fixture(scope='function')
def response(case):
    response = requests.get(url + case.url_parameters)
    yield response


@pytest.fixture(scope='function')
def status_code(response):
    yield response.status_code


@pytest.fixture(scope='function')
def headers(response):
    yield response.headers


@pytest.fixture(scope='function')
def xmlschema(case):
    xmlschema_doc = etree.parse(case.xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    yield xmlschema


@pytest.fixture(scope='function')
def doc(response):
    xml = StringIO(response.content)
    doc = etree.parse(xml)
    yield doc
