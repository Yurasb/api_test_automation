# -*- coding: utf-8 -*-

import requests


def test_encoding(get_case):
    response = requests.get(get_case.api_url)
    assert response.encoding == 'utf-8'
