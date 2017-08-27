# -*- coding: utf-8 -*-


def test_status_code(status_code, case):
    assert status_code == case.expected_status_code
