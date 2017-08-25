# -*- coding: utf-8 -*-


def test_status_code(status_code, case):
    assert status_code == case.expected_status_code


def test_invalid_status_code(status_code, invalid_case):
    assert status_code == invalid_case.expected_status_code
