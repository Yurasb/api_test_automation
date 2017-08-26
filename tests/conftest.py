# -*- coding: utf-8 -*-


import pytest
import requests

from main import url
from test_cases.test_cases import get_case


@pytest.fixture(scope='function', params=range(6))
def case(request):
    case = get_case(request.param)
    return case


@pytest.fixture(scope='function')
def response(case):
    response = requests.get(url + case.url_parametes)
    yield response


@pytest.fixture(scope='function')
def status_code(response):
    yield response.status_code


@pytest.fixture(scope='function')
def headers(response):
    yield response.headers


@pytest.fixture(scope='function')
def body(response):
    yield response.content
