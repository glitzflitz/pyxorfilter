# pyxorfilter

Python bindings for [C]([https://github.com/FastFilter/xor_singleheader](https://github.com/FastFilter/xor_singleheader)) implementation of [Xor Filters: Faster and Smaller Than Bloom and Cuckoo Filters](https://arxiv.org/abs/1912.08258)
## Installation
### From Source
```
git clone https://github.com/GreyDireWolf/pyxorfilter
cd pyxorfilter
setup.py build_ext
setup.py install
```
## Usage
```
>>> from pyxorfilter import Xor8, Xor16
>>> filter = Xor8(100)	#or Xor16(size)
>>> filter.populate([_ for _ in range(100)])
True
>>> filter.contains(90)
True
>>> filter.contains(150)
False
>>> filter.size_in_bytes()
177
```
## Caveats
### Overflow
Both Xor8 and Xor16 take uint8_t and uint_16t respectively. Make sure that the input is unsigned.
