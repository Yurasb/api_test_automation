# -*- coding: utf-8 -*-

import requests


def test_status_code(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert response.status_code == get_case.exp_status_code
