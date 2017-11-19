use std::f64::consts;

#[repr(C)]
#[derive(Copy, Clone)]
pub struct Point {
    x: f64,
    y: f64,
}

#[repr(C)]
pub struct LineString {
    points: [Point; 4],
}

#[no_mangle]
pub extern fn rotate(Point { x, y }: Point, angle: i16) -> Point {
    let angle = angle as f64 * consts::PI / 180.;
    let (sin, cos) = angle.sin_cos();
    Point {
        x: x * cos - y * sin,
        y: x * sin + y * cos,
    }
}

#[no_mangle]
pub extern fn length(line_string: LineString) -> f64 {
    line_string
        .points
        .windows(2)
        .map(|x| line_length(x[0], x[1]))
        .sum()
}

fn line_length(start: Point, end: Point) -> f64 {
    let x_diff = end.x - start.x;
    let y_diff = end.y - start.y;
    (x_diff * x_diff + y_diff * y_diff).sqrt()
}
