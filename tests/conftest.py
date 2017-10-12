# -*- coding: utf-8 -*-

import pytest
from test_cases.cases import test_cases


@pytest.fixture(scope='function', params=range(2))
def get_case(request):
    case = test_cases[request.param]
    return case
