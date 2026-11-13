import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calc import sub


def test_sub():
    assert sub(5, 3) == 2
