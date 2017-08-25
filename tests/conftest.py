# -*- coding: utf-8 -*-


import pytest
import requests
from main import url
from test_cases.test_cases import valid_case, invalid_case_1


@pytest.fixture(scope='function')
def case(request):
    case = valid_case
    return case


@pytest.fixture(scope='function')
def invalid_case(request):
    invalid_case = invalid_case_1
    return invalid_case


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
    yield response.text
