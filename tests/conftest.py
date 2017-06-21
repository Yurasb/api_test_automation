# -*- coding: utf-8 -*-


import pytest
import requests
from main import url
from test_cases.test_cases import valid_case


@pytest.fixture(scope='function')
def response():
    response = requests.get(url)
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


@pytest.fixture(scope='function')
def case(request):
    case = valid_case
    return case
