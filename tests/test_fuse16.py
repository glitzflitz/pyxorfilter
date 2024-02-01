from pyxorfilter import Fuse16
from random import sample

def test_fuse16_serialization():
    import urllib.request
    import tempfile
    import os

    # tranco list contains the top 1M most popular domain names.
    url = "https://tranco-list.eu/download/LJ494/1000000"
    
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8", errors="replace")

    # extract the domain list from the second column of the CSV (rank, domain)
    domains = [line.split(",")[1] for line in data.splitlines()]

    # populate XORF.
    xor_filter = Fuse16(len(domains))
    xor_filter.populate(domains)

    # initial assertions.
    needle = "google.com"
    assert needle in domains
    assert xor_filter.contains(needle)

    # serialize to a temporary file.
    path_serialized = tempfile.NamedTemporaryFile(delete=False).name

    with open(path_serialized, "wb+") as fh:
        fh.write(xor_filter.serialize())

    # refresh XORF from disk.
    with open(path_serialized, "rb") as fh:
        deserialized_xor = Fuse16.deserialize(fh.read())

    # is needle in the XORF?
    try:
        assert deserialized_xor.contains(needle)
    except Exception as e:
        raise e
    finally:
        # disk cleanup.
        os.remove(path_serialized)
    
def test_fuse16_int():
    xor_filter = Fuse16(50)
    xor_filter.populate([_ for _ in range(50)])
    for i in range(50):
        assert xor_filter.contains(i) == True

def test_fuse16_int_iterable():
    xor_filter = Fuse16(50)
    xor_filter.populate(range(50))
    for i in range(50):
        assert xor_filter.contains(i) == True

def test_fuse16_strings():
    xor_filter = Fuse16(10)
    test_str = ["あ", "/dev/null; touch /tmp/blns.fail ; echo", "अ", "Normal", "122"]
    xor_filter.populate(test_str.copy())
    for i in test_str:
        assert xor_filter.contains(i) == True


def test_fuse16_floats():
    xor_filter = Fuse16(10)
    test_floats = [1.23, 9999.1616, 323.43, 0.0]
    xor_filter.populate(test_floats.copy())
    for i in test_floats:
        assert xor_filter.contains(i) == True


def test_fuse16_all():
    xor_filter = Fuse16(5)
    test_str = ["string", 51, 0.0, 12.3]
    xor_filter.populate(test_str.copy())
    for i in test_str:
        assert xor_filter.contains(i) == True

if __name__ == "__main__":
    test_fuse16_all()
    print("good")
