# -*- coding: utf-8 -*-
from cffi import FFI
ffi = FFI()
ffi.cdef("""
    struct Matrix;
    typedef struct Matrix Matrix;

    Matrix* matrix_new(double, double, double, double);
    void matrix_delete(Matrix*);
    double matrix_elem(Matrix*, uintptr_t);
    double matrix_det(Matrix*);
    Matrix* matrix_mul(Matrix*, Matrix*);
""")
lib = ffi.dlopen("target/release/libmatrix.so")

class Matrix:
    def __init__(self):
        self._matrix = None

    @classmethod
    def from_tuple(cls, values):
        matrix = cls()
        matrix._matrix = ffi.gc(
            lib.matrix_new(values[0], values[1], values[2], values[3]),
            lib.matrix_delete)
        return matrix

    def det(self):
        return lib.matrix_det(self._matrix)

    def __mul__(self, other):
        matrix = self.__class__()
        matrix._matrix = ffi.gc(
            lib.matrix_mul(self._matrix, other._matrix),
            lib.matrix_delete)
        return matrix

    def print_(self):
        values = [lib.matrix_elem(self._matrix, i) for i in range(4)]
        print("⎛{:6.2f} {:6.2f}⎞".format(values[0], values[1]))
        print("⎝{:6.2f} {:6.2f}⎠".format(values[2], values[3]))

m1 = Matrix.from_tuple((0, 1, 2, 3))
m2 = Matrix.from_tuple((0, 1, 1, 0))
det = m1.det()
m3 = m1 * m2

print("m1:")
m1.print_()
print("det(m1): {}".format(det))
print("")
print("m2:")
m2.print_()
print("")
print("m1 * m2:")
m3.print_()
print("")
print("m2 * m1:")
(m2*m1).print_()
