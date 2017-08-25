# -*- coding: utf-8 -*-


def test_body(body, case):
    assert body == case.expected_body


def test_body(body, invalid_case):
    assert body == invalid_case.expected_body
