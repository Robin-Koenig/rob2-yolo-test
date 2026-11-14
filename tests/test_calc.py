import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from calc import add, div


def test_add():
    assert add(2, 3) == 5


def test_div():
    assert div(6, 3) == 2


def test_div_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        div(1, 0)
