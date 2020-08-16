from cffi import FFI
import os
from sys import exit, platform


ffi = FFI()
cdef_from_file = None

header = "lib/xor_singleheader/include/xorfilter.h"

with open(header, "r") as src:
    ffi.set_source(
        "_xorfilter", src.read(),
    )

ffi.cdef(
    """
static inline uint64_t xor_murmur64(uint64_t h) ;

static inline uint64_t xor_mix_split(uint64_t key, uint64_t seed) ;

static inline uint64_t xor_rotl64(uint64_t n, unsigned int c) ;

static inline uint32_t xor_reduce(uint32_t hash, uint32_t n) ;

static inline uint64_t xor_fingerprint(uint64_t hash) ;

static inline uint64_t xor_rng_splitmix64(uint64_t *seed) ;


typedef struct xor8_s {
  uint64_t seed;
  uint64_t blockLength;
  uint8_t
      *fingerprints; // after xor8_allocate, will point to 3*blockLength values
} xor8_t;

struct xor_xorset_s {
  uint64_t xormask;
  uint32_t count;
};

typedef struct xor16_s {
  uint64_t seed;
  uint64_t blockLength;
  uint16_t
      *fingerprints; // after xor16_allocate, will point to 3*blockLength values
} xor16_t;

typedef struct xor_xorset_s xor_xorset_t;

struct xor_hashes_s {
  uint64_t h;
  uint32_t h0;
  uint32_t h1;
  uint32_t h2;
};
typedef struct xor_hashes_s xor_hashes_t;

struct xor_h0h1h2_s {
  uint32_t h0;
  uint32_t h1;
  uint32_t h2;
};
typedef struct xor_h0h1h2_s xor_h0h1h2_t;

struct xor_keyindex_s {
  uint64_t hash;
  uint32_t index;
};

typedef struct xor_keyindex_s xor_keyindex_t;

struct xor_setbuffer_s {
  xor_keyindex_t *buffer;
  uint32_t *counts;
  int insignificantbits;
  uint32_t slotsize; // should be 1<< insignificantbits
  uint32_t slotcount;
  size_t originalsize;
};
typedef struct xor_setbuffer_s xor_setbuffer_t;

static inline bool xor8_contain(uint64_t key, const xor8_t *filter);
static inline bool xor16_contain(uint64_t key, const xor16_t *filter);

static inline bool xor8_allocate(uint32_t size, xor8_t *filter);
static inline bool xor16_allocate(uint32_t size, xor16_t *filter);
static inline size_t xor8_size_in_bytes(const xor8_t *filter);
static inline size_t xor16_size_in_bytes(const xor16_t *filter);
static inline void xor8_free(xor8_t *filter);
static inline void xor16_free(xor16_t *filter);

static inline xor_hashes_t xor8_get_h0_h1_h2(uint64_t k, const xor8_t *filter) ;
static inline xor_h0h1h2_t xor8_get_just_h0_h1_h2(uint64_t hash, const xor8_t *filter) ;
static inline uint32_t xor8_get_h0(uint64_t hash, const xor8_t *filter) ;
static inline uint32_t xor8_get_h1(uint64_t hash, const xor8_t *filter) ;
static inline uint32_t xor8_get_h2(uint64_t hash, const xor8_t *filter) ;
static inline uint32_t xor16_get_h0(uint64_t hash, const xor16_t *filter) ;
static inline uint32_t xor16_get_h1(uint64_t hash, const xor16_t *filter) ;
static inline uint32_t xor16_get_h2(uint64_t hash, const xor16_t *filter) ;
static inline xor_hashes_t xor16_get_h0_h1_h2(uint64_t k, const xor16_t *filter) ;

static inline bool xor_init_buffer(xor_setbuffer_t *buffer, size_t size) ;
static inline void xor_free_buffer(xor_setbuffer_t *buffer) ;
static inline void xor_buffered_increment_counter(uint32_t index, uint64_t hash, xor_setbuffer_t *buffer, xor_xorset_t *sets) ;
static inline void xor_make_buffer_current(xor_setbuffer_t *buffer, xor_xorset_t *sets, uint32_t index, xor_keyindex_t *Q, size_t *Qsize) ;
static inline void xor_buffered_decrement_counter(uint32_t index, uint64_t hash, xor_setbuffer_t *buffer, xor_xorset_t *sets, xor_keyindex_t *Q, size_t *Qsize) ;
static inline void xor_flush_increment_buffer(xor_setbuffer_t *buffer, xor_xorset_t *sets) ;
static inline void xor_flush_decrement_buffer(xor_setbuffer_t *buffer, xor_xorset_t *sets, xor_keyindex_t *Q, size_t *Qsize) ;
static inline uint32_t xor_flushone_decrement_buffer(xor_setbuffer_t *buffer, xor_xorset_t *sets, xor_keyindex_t *Q, size_t *Qsize) ;

bool xor8_buffered_populate(const uint64_t *keys, uint32_t size, xor8_t *filter) ;
bool xor8_populate(const uint64_t *keys, uint32_t size, xor8_t *filter) ;
bool xor16_buffered_populate(const uint64_t *keys, uint32_t size, xor16_t *filter) ;
bool xor16_populate(const uint64_t *keys, uint32_t size, xor16_t *filter) ;
"""
)

if __name__ == "__main__":
    ffi.compile(verbose=True)
