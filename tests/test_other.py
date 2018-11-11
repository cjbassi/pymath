from pymath.other import *


def test_convert_base():
    assert convert_base('5', 10, 2) == '101'
    assert convert_base('7', 10, 4) == '13'
    assert convert_base('101', 2, 4) == '11'
    assert convert_base('222', 3, 4) == '122'
