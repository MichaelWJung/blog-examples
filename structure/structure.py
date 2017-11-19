# -*- coding: utf-8 -*-
from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef struct { double x; double y; } Point;
    typedef struct { Point points[4]; } LineString;
    Point rotate(Point, int16_t);
    double length(LineString);
""")

lib = ffi.dlopen("target/release/libstructure.so")

point = ffi.new("Point *")
point.x = 1
point.y = 2

angle = 73
result = lib.rotate(point[0], angle)
print("Rotating ({}, {}) through {}°: ({:.2f}, {:.2f})".format(
    point.x, point.y, angle, result.x, result.y))

line_string = ffi.new("LineString *", [[(0, 0), (1, 0), (1, 1), (0, 2)]])
length = lib.length(line_string[0])
print("Line length: " + str(length))
