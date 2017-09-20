# -*- coding: utf-8 -*-
import requests


def test_date(get_case):
    response = requests.get(get_case.api_url)
    assert 'Date' in response.headers


def test_content_encoding(get_case):
    response = requests.get(get_case.api_url)
    assert (
        response.headers['Content-Encoding'] ==
        get_case.exp_headers['Content-Encoding']
    )


def test_cache_control(get_case):
    response = requests.get(get_case.api_url)
    assert (
        response.headers['Cache-Control'] ==
        get_case.exp_headers['Cache-Control']
    )


def test_server(get_case):
    response = requests.get(get_case.api_url)
    assert (
        response.headers['Server'] ==
        get_case.exp_headers['Server']
    )


def test_content_type(get_case):
    response = requests.get(get_case.api_url)
    assert (
        response.headers['Content-Type'] ==
        get_case.exp_headers['Content-Type']
    )


def test_transfer_encoding(get_case):
    response = requests.get(get_case.api_url)
    assert (
        response.headers['Transfer-Encoding'] ==
        get_case.exp_headers['Transfer-Encoding']
    )
