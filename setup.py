from setuptools import setup, Extension, find_packages
import os

setup(
    name='pyxorfilter',
    version='0.1.0',
    description="Python bindings for c implementation of xorfilter",
    author='Amey Narkhede',
    author_email='ameynarkhede02@gmail.com',
    url='',
    license='Apache 2.0',
    python_requires=">=3.0",
    packages=find_packages(),
    ext_package='pyxorfilter',
    install_requires = ['cffi'],
    setup_requires = ['cffi'],
    cffi_modules = ['pyxorfilter/ffibuild.py:ffi'],
    )
