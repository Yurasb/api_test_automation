# -*- coding: utf-8 -*-


def test_status_code(status_code, case):
    assert status_code == case.exp_status_code
