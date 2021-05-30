#!/usr/local/bin/python3
# this is a pytest compliant file
# Contents of conftest.py
# author: prabhat
# project: none

import pytest
import test

def pytest_addoption(parser):
    parser.addoption("--msg", action="store_true", default="You are using GitHub Actions and Python3", help="type a custome message")

@pytest.fixture
def msg(request):
    return request.config.getoption("--msg")
