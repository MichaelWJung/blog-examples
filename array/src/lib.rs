use std::slice;

#[no_mangle]
pub extern fn sum(ptr: *const i32, len: usize) -> i32 {
    assert!(!ptr.is_null());
    let array = unsafe { slice::from_raw_parts(ptr, len) };
    array.iter().sum()
}

#[no_mangle]
pub extern fn reverse(ptr: *mut i32, len: usize) {
    assert!(!ptr.is_null());
    let array = unsafe { slice::from_raw_parts_mut(ptr, len) };
    array.reverse();
}
