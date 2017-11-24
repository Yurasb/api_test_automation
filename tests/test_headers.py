# -*- coding: utf-8 -*-

import requests


def test_date(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert 'Date' in response.headers


def test_content_encoding(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert (
        response.headers['Content-Encoding'] ==
        get_case.exp_headers['Content-Encoding']
    )


def test_cache_control(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert (
        response.headers['Cache-Control'] ==
        get_case.exp_headers['Cache-Control']
    )


def test_server(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert (
        response.headers['Server'] ==
        get_case.exp_headers['Server']
    )


def test_content_type(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert (
        response.headers['Content-Type'] ==
        get_case.exp_headers['Content-Type']
    )


def test_transfer_encoding(base, get_case):
    response = requests.get('{}{}'.format(base, get_case.url_parameters))
    assert (
        response.headers['Transfer-Encoding'] ==
        get_case.exp_headers['Transfer-Encoding']
    )
