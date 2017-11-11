# -*- coding: utf-8 -*-
from cffi import FFI
ffi = FFI()
ffi.cdef("""
    void print_text(const char*);
""")

lib = ffi.dlopen("target/release/libtext.so")

def to_cstring(text):
    return ffi.new("char[]", text.encode("utf-8"))

text = to_cstring("test äöü Война и миръ السلام عليكم 圍棋 😎")
lib.print_text(text)
