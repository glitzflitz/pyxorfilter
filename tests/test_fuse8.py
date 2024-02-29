from pyxorfilter import Fuse8
from random import sample
import tempfile, os

def test_fuse8_int():
    xor_filter = Fuse8(50)
    xor_filter.populate([_ for _ in range(50)])
    for i in range(50):
        assert xor_filter.contains(i) == True

def test_fuse8_int_iterable():
    xor_filter = Fuse8(50)
    xor_filter.populate(range(50))
    for i in range(50):
        assert xor_filter.contains(i) == True

def test_fuse8_strings():
    xor_filter = Fuse8(10)
    test_str = ["あ", "/dev/null; touch /tmp/blns.fail ; echo", "अ", "Normal", "122"]
    xor_filter.populate(test_str.copy())
    for i in test_str:
        assert xor_filter.contains(i) == True


def test_fuse8_floats():
    xor_filter = Fuse8(10)
    test_floats = [1.23, 9999.88, 323.43, 0.0]
    xor_filter.populate(test_floats.copy())
    for i in test_floats:
        assert xor_filter.contains(i) == True


def test_fuse8_all():
    xor_filter = Fuse8(5)
    test_str = ["string", 51, 0.0, 12.3]
    xor_filter.populate(test_str.copy())
    for i in test_str:
        assert xor_filter.contains(i) == True

def test_fuse8_serialize():
    xor_filter = Fuse8(5)
    test_str = ["string", 51, 0.0, 12.3]
    xor_filter.populate(test_str.copy())
    serialized_filter = tempfile.NamedTemporaryFile(delete=False).name
    with open(serialized_filter, 'wb') as f:
        f.write(xor_filter.serialize())

    with open(serialized_filter, 'rb') as f:
        recover_xor_filter = Fuse8.deserialize(f.read())

    for i in test_str:
        assert recover_xor_filter.contains(i)

    os.remove(serialized_filter)
