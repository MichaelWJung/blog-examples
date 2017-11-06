from cffi import FFI
ffi = FFI()
ffi.cdef("""
    void reverse(int32_t*, uintptr_t);
    int32_t sum(const int32_t*, uintptr_t);
""")

lib = ffi.dlopen("target/release/libarray.so")

list_ = [1, 2, 3, 4]
sum_ = lib.sum(list_, len(list_))
print(sum_)

tuple_ = (1, 2, 3, 4, 1)
sum_ = lib.sum(tuple_, len(tuple_))
print(sum_)

# Will not modify list_!
lib.reverse(list_, len(list_))
print(list_)

c_array = ffi.new("int32_t[]", list(range(10)))
lib.reverse(c_array, len(c_array))
print(', '.join(str(x) for x in c_array))

import numpy as np
np_array = np.int32([17, 42, 73])
pointer = ffi.cast("int32_t*", np_array.ctypes.data)
lib.reverse(pointer, len(np_array))
print(np_array)

