# -*- coding: utf-8 -*-

import requests


def test_encoding(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert response.encoding == 'utf-8'
