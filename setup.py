from setuptools import setup, Extension, find_packages
import os

setup(
    name="pyxorfilter",
    version="0.1.1",
    description="Python bindings for C implementation of xorfilter",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author="Amey Narkhede",
    author_email="ameynarkhede02@gmail.com",
    url="https://github.com/glitzflitz/pyxorfilter",
    license="Apache 2.0",
    python_requires=">=3.0",
    packages=find_packages(),
    ext_package="pyxorfilter",
    install_requires=["cffi"],
    setup_requires=["cffi"],
    cffi_modules=["pyxorfilter/ffibuild.py:ffi"],
    test_suite="nose.collector",
    tests_require=["nose"],
)
