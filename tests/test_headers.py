# -*- coding: utf-8 -*-


def test_date(headers):
    assert 'Date' in headers


def test_content_encoding(headers, case):
    assert (
        headers['Content-Encoding'] ==
        case.exp_headers['Content-Encoding']
    )


def test_cache_control(headers, case):
    assert (
        headers['Cache-Control'] ==
        case.exp_headers['Cache-Control']
    )


def test_server(headers, case):
    assert (
        headers['Server'] ==
        case.exp_headers['Server']
    )


def test_content_type(headers, case):
    assert (
        headers['Content-Type'] ==
        case.exp_headers['Content-Type']
    )


def test_transfer_encoding(headers, case):
    assert (
        headers['Transfer-Encoding'] ==
        case.exp_headers['Transfer-Encoding']
    )
