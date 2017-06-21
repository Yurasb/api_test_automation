# -*- coding: utf-8 -*-


def test_status_code(headers, case):
    assert headers == case.expected_headers