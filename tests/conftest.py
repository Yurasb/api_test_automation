# -*- coding: utf-8 -*-
import pytest
from test_cases.cases import valid_case


@pytest.fixture(scope='function')
def get_case(request):
    case = valid_case
    return case
