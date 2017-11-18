use std::f64::consts;

#[repr(C)]
pub struct Point {
    x: f64,
    y: f64,
}

#[no_mangle]
pub extern fn rotate(Point {x, y}: Point, angle: i16) -> Point {
    let angle = angle as f64 * consts::PI / 180.;
    let (sin, cos) = angle.sin_cos();
    Point {
        x: x * cos - y * sin,
        y: x * sin + y * cos,
    }
}
