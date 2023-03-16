from setuptools import setup, Extension, find_packages

setup(
    setup_requires=["cffi"],
    packages=find_packages(),
    ext_package="pyxorfilter",
    cffi_modules=["pyxorfilter/ffibuild.py:ffi"],
    test_suite="nose.collector",
    tests_require=["nose"],
)
