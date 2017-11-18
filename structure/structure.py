# -*- coding: utf-8 -*-
from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef struct { double x; double y; } Point;
    Point rotate(Point, int16_t);
""")

lib = ffi.dlopen("target/release/libstructure.so")

point = ffi.new("Point *")
point.x = 1
point.y = 2

for a in range(20, 361, 20):
    result = lib.rotate(point[0], a)
    print("Rotating ({}, {}) through {}°: ({:.2f}, {:.2f})".format(
        point.x, point.y, a, result.x, result.y))
