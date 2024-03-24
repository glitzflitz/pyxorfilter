from ._xorfilter import lib, ffi
from ctypes import c_ulonglong
import xxhash
import struct

def hash(item):
    return xxhash.xxh64(str(item)).intdigest()

class Xor8:
    def __init__(self, size):
        self.__filter = ffi.new("xor8_t *")
        status = lib.xor8_allocate(size, self.__filter)
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
    
    def serialize(self):
        buffer = ffi.new("char[]", lib.xor8_serialization_bytes(self.__filter))
        lib.xor8_serialize(self.__filter, buffer)
        return ffi.buffer(buffer)

    @staticmethod
    def deserialize(buffer):
        self = object.__new__(Xor8)
        self.__filter = ffi.new("xor8_t *")
        lib.xor8_deserialize(self.__filter, ffi.from_buffer(buffer))
        return self


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

    def serialize(self):
        buffer = ffi.new("char[]", lib.xor16_serialization_bytes(self.__filter))
        lib.xor16_serialize(self.__filter, buffer)
        return ffi.buffer(buffer)

    @staticmethod
    def deserialize(buffer):
        self = object.__new__(Xor16)
        self.__filter = ffi.new("xor16_t *")
        lib.xor16_deserialize(self.__filter, ffi.from_buffer(buffer))
        return self

class Fuse8:
    def __init__(self, size):
        self.__filter = ffi.new("binary_fuse8_t *")
        status = lib.binary_fuse8_allocate(size, self.__filter)
        if not status:
            print("Unable to allocate memory for 8 bit filter")

    def __repr__(self):
        return "Fuse8 object with size(in bytes):{}".format(self.size_in_bytes())

    def __getitem__(self, item):
        return self.contains(item)

    def __del__(self):
        lib.binary_fuse8_free(self.__filter)

    def populate(self, data: list):
        """
        Data can either be a list or iterable
        """
        data = list(map(lambda x: c_ulonglong((hash(x))).value, data))
        return lib.binary_fuse8_populate(data, len(data), self.__filter)

    def contains(self, item):
        item = c_ulonglong((hash(item))).value
        return lib.binary_fuse8_contain(item, self.__filter)

    def size_in_bytes(self):
        return lib.binary_fuse8_size_in_bytes(self.__filter)

    def serialize(self):
        buffer = ffi.new("char[]", lib.binary_fuse8_serialization_bytes(self.__filter))
        lib.binary_fuse8_serialize(self.__filter, buffer)
        return ffi.buffer(buffer)

    @staticmethod
    def deserialize(buffer):
        self = object.__new__(Fuse8)
        self.__filter = ffi.new("binary_fuse8_t *")
        lib.binary_fuse8_deserialize(self.__filter, ffi.from_buffer(buffer))
        return self

class Fuse16:
    def __init__(self, size):
        self.__filter = ffi.new("binary_fuse16_t *")
        status = lib.binary_fuse16_allocate(size, self.__filter)
        if not status:
            print("Unable to allocate memory for 16 bit filter")

    def __repr__(self):
        return "Fuse16 object with size(in bytes):{}".format(self.size_in_bytes())

    def __getitem__(self, item):
        return self.contains(item)

    def __del__(self):
        lib.binary_fuse16_free(self.__filter)

    def populate(self, data: list):
        """
        Data can either be a list or iterable
        """
        data = list(map(lambda x: c_ulonglong((hash(x))).value, data))
        return lib.binary_fuse16_populate(data, len(data), self.__filter)

    def contains(self, item):
        item = c_ulonglong((hash(item))).value
        return lib.binary_fuse16_contain(item, self.__filter)

    def size_in_bytes(self):
        return lib.binary_fuse16_size_in_bytes(self.__filter)

    def serialize(self):
        buffer = ffi.new("char[]", lib.binary_fuse16_serialization_bytes(self.__filter))
        lib.binary_fuse16_serialize(self.__filter, buffer)
        return ffi.buffer(buffer)

    @staticmethod
    def deserialize(buffer):
        self = object.__new__(Fuse16)
        self.__filter = ffi.new("binary_fuse16_t *")
        lib.binary_fuse16_deserialize(self.__filter, ffi.from_buffer(buffer))
        return self