from setuptools import setup, Extension, find_packages
import os

setup(
    cffi_modules=["pyxorfilter/ffibuild.py:ffi"],
    test_suite="nose.collector",
    tests_require=["nose"],
)
