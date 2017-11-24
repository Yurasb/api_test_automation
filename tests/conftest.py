# -*- coding: utf-8 -*-

import pytest
from test_cases.cases import test_cases
from utils.transport_config import ConfigFactory


@pytest.fixture(scope='session', params=['http'], autouse=True)
def base(request):
    config = ConfigFactory()
    transport = config.get_config(request.param)
    url = transport.base_url()
    return url


@pytest.fixture(scope='function', params=range(2))
def get_case(request):
    case = test_cases[request.param]
    return case
