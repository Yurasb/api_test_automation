# -*- coding: utf-8 -*-


def test_status_code(body, case):
    assert body == case.expected_body