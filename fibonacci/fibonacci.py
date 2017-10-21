from cffi import FFI
ffi = FFI()
ffi.cdef("""
    uint64_t fibonacci(uint32_t);
""")

C = ffi.dlopen("target/release/libfibonacci.so")

numbers = [C.fibonacci(n) for n in range(10)]
print(', '.join(str(x) for x in numbers))

