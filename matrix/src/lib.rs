use std::f64;
use std::ops::Mul;
use std::ptr;

#[derive(Copy, Clone)]
pub struct Matrix {
    values: [f64; 4],
}

impl Matrix {
    pub fn new(a11: f64, a12: f64, a21: f64, a22: f64) -> Matrix {
        Matrix { values: [a11, a12, a21, a22] }
    }

    pub fn det(&self) -> f64 {
        self.values[0] * self.values[3] - self.values[1] * self.values[2]
    }
}

impl Mul for Matrix {
    type Output = Matrix;

    fn mul(self, rhs: Matrix) -> Matrix {
        Matrix {
            values: [
                self.values[0] * rhs.values[0] + self.values[1] * rhs.values[2],
                self.values[0] * rhs.values[1] + self.values[1] * rhs.values[3],
                self.values[2] * rhs.values[0] + self.values[3] * rhs.values[2],
                self.values[2] * rhs.values[1] + self.values[3] * rhs.values[3],
            ],
        }
    }
}

#[no_mangle]
pub extern fn matrix_new(a11: f64, a12: f64, a21: f64, a22: f64) -> *mut Matrix {
    let matrix = Box::new(Matrix::new(a11, a12, a21, a22));
    Box::into_raw(matrix)
}

#[no_mangle]
pub extern fn matrix_delete(matrix: *mut Matrix) {
    if !matrix.is_null() {
        unsafe { Box::from_raw(matrix) };
    }
}

#[no_mangle]
pub extern fn matrix_elem(matrix: *const Matrix, index: usize) -> f64 {
    if !matrix.is_null() {
        let matrix = unsafe { &*matrix };
        matrix.values[index]
    } else {
        f64::NAN
    }
}

#[no_mangle]
pub extern fn matrix_det(matrix: *const Matrix) -> f64 {
    if !matrix.is_null() {
        let matrix = unsafe { &*matrix };
        matrix.det()
    } else {
        f64::NAN
    }
}

#[no_mangle]
pub extern fn matrix_mul(lhs: *const Matrix, rhs: *const Matrix) -> *mut Matrix {
    if lhs.is_null() || lhs.is_null() {
        ptr::null_mut()
    } else {
        let lhs = unsafe { *lhs };
        let rhs = unsafe { *rhs };
        let result = Box::new(lhs * rhs);
        Box::into_raw(result)
    }
}
