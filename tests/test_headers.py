# -*- coding: utf-8 -*-


def test_id(headers):
    assert 'X-GitHub-Request-Id' in headers


def test_date(headers):
    assert 'Date' in headers


def test_expires(headers):
    assert 'Expires' in headers


def test_content_encoding(headers, case):
    assert (
        headers['Content-Encoding'] ==
        case.expected_headers['Content-Encoding']
    )


def test_cache_control(headers, case):
    assert (
        headers['Cache-Control'] ==
        case.expected_headers['Cache-Control']
    )


def test_server(headers, case):
    assert (
        headers['Server'] ==
        case.expected_headers['Server']
    )


def test_content_type(headers, case):
    assert (
        headers['Content-Type'] ==
        case.expected_headers['Content-Type']
    )


def test_access_control(headers, case):
    assert (
        headers['Access-Control-Allow-Origin'] ==
        case.expected_headers['Access-Control-Allow-Origin']
    )


def test_transfer_encoding(headers, case):
    assert (
        headers['Transfer-Encoding'] ==
        case.expected_headers['Transfer-Encoding']
    )
