# -*- coding: utf-8 -*-


def test_date(headers):
    assert 'Date' in headers


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


def test_transfer_encoding(headers, case):
    assert (
        headers['Transfer-Encoding'] ==
        case.expected_headers['Transfer-Encoding']
    )


def test_content_length(headers, case):
    assert (
        headers['Content-Length'] ==
        case.expected_headers['Content-Length']
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


def test_connection(headers, case):
    assert (
        headers['Connection'] ==
        case.expected_headers['Connection']
    )


def test_error(headers, case):
    assert (
        headers['Error'] ==
        case.expected_headers['Error']
    )


def test_content_type(headers, case):
    assert (
        headers['Content-Type'] ==
        case.expected_headers['Content-Type']
    )


def test_content_disposition(headers, case):
    assert (
        headers['Content-Disposition'] ==
        case.expected_headers['Content-Disposition']
    )


def test_status(headers, case):
    assert (
        headers['Status'] ==
        case.expected_headers['Status']
    )


def test_x_request_id(headers):
    assert 'X-Request-Id' in headers


def test_x_xss_protection(headers, case):
    assert (
        headers['X-XSS-Protection'] ==
        case.expected_headers['X-XSS-Protection']
    )


def test_x_content_type_options(headers, case):
    assert (
        headers['X-Content-Type-Options'] ==
        case.expected_headers['X-Content-Type-Options']
    )


def test_x_download_options(headers, case):
    assert (
        headers['X-Download-Options'] ==
        case.expected_headers['X-Download-Options']
    )


def test_x_download_options(headers, case):
    assert (
        headers['X-Download-Options'] ==
        case.expected_headers['X-Download-Options']
    )


def test_keep_alive(headers, case):
    assert (
        headers['Keep-Alive'] ==
        case.expected_headers['Keep-Alive']
    )


def test_x_runtime(headers):
    assert 'X-Runtime' in headers


def test_x_permitted_cross_domain_policies(headers, case):
    assert (
        headers['X-Permitted-Cross-Domain-Policies'] ==
        case.expected_headers['X-Permitted-Cross-Domain-Policies']
    )


def test_x_frame_options(headers, case):
    assert (
        headers['X-Frame-Options'] ==
        case.expected_headers['X-Frame-Options']
    )
