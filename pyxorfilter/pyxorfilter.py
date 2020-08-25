from ._xorfilter import lib, ffi
from ctypes import c_ulonglong
import struct


class Xor8:
    def __init__(self, size):
        self.__filter = ffi.new("xor8_t *")
        status = lib.xor8_allocate(size, self.__filter)
        self.size = size
        if not status:
            print("Unable to allocate memory for 8 bit filter")

    def __repr__(self):
        return "Xor8 object with size(in bytes):{}".format(self.size_in_bytes())

    def __getitem__(self, item):
        return self.contains(item)

    def __del__(self):
        lib.xor8_free(self.__filter)

    def populate(self, data: list):
        """
        Data can either be a list or iterable
        """
        data = list(map(lambda x: c_ulonglong((hash(x))).value, data))
        return lib.xor8_buffered_populate(data, len(data), self.__filter)

    def contains(self, item):
        item = c_ulonglong((hash(item))).value
        return lib.xor8_contain(item, self.__filter)

    def size_in_bytes(self):
        return lib.xor8_size_in_bytes(self.__filter)


class Xor16:
    def __init__(self, size):
        self.__filter = ffi.new("xor16_t *")
        status = lib.xor16_allocate(size, self.__filter)
        if not status:
            print("Unable to allocate memory for 16 bit filter")

    def __repr__(self):
        return "Xor16 object with size(in bytes):{}".format(self.size_in_bytes())

    def __getitem__(self, item):
        return self.contains(item)

    def __del__(self):
        lib.xor16_free(self.__filter)

    def populate(self, data):
        data = list(map(lambda x: c_ulonglong((hash(x))).value, data))
        return lib.xor16_buffered_populate(data, len(data), self.__filter)

    def contains(self, item):
        item = c_ulonglong((hash(item))).value
        return lib.xor16_contain(item, self.__filter)

    def size_in_bytes(self):
        return lib.xor16_size_in_bytes(self.__filter)
