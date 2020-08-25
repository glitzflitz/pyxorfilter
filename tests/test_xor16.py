from pyxorfilter import Xor16
import random


def test_xor16_int():
    xor_filter = Xor16(100)
    test_lst = random.sample(range(0, 1000), 100)
    xor_filter.populate(test_lst.copy())
    for i in test_lst:
        assert xor_filter.contains(i) == True
    for i in random.sample(range(1000, 3000), 500):
        assert xor_filter.contains(i) == False

def test_xor16_int_iterable():
    xor_filter = Xor16(100)
    xor_filter.populate(range(50))
    for i in range(50):
        assert xor_filter.contains(i) == True

def test_xor16_strings():
    xor_filter = Xor16(10)
    test_str = ["あ", "/dev/null; touch /tmp/blns.fail ; echo", "अ", "Normal", "122"]
    xor_filter.populate(test_str.copy())
    for test in test_str:
        assert xor_filter.contains(test) == True
    test_str2 = ["月", "क", "12", "delta"]
    for i in test_str2:
        assert xor_filter.contains(i) == False


def test_xor16_floats():
    xor_filter = Xor16(10)
    test_floats = [1.23, 9999.88, 323.43, 0.0]
    xor_filter.populate(test_floats.copy())
    for i in test_floats:
        assert xor_filter.contains(i) == True
    test_floats2 = [-1.23, 1.0, 0.1, 676.5, 1.234]
    for i in test_floats2:
        assert xor_filter.contains(i) == False


def test_xor16_all():
    xor_filter = Xor16(5)
    test_str = ["string", 51, 0.0, 12.3]
    xor_filter.populate(test_str.copy())
    for i in test_str:
        assert xor_filter.contains(i) == True
    test_str2 = [12, "४", 0.1]
    for i in test_str2:
        assert xor_filter.contains(i) == False
