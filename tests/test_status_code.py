# -*- coding: utf-8 -*-

import requests


def test_status_code(get_case):
    response = requests.get(get_case.api_url)
    assert response.status_code == get_case.exp_status_code
