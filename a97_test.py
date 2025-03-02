# Tests
# File names should start with test_ or end with _test.py
# Test functions should start with test_
# Run pytest in prompt

import pytest
from a97_add import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(4, -1) == 3