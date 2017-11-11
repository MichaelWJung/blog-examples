use std::ffi::CStr;
use std::os::raw::c_char;

#[no_mangle]
pub extern fn print_text(text: *const c_char) {
    assert!(!text.is_null());
    let c_str = unsafe { CStr::from_ptr(text) };
    let string = c_str.to_str().expect("Not a valid UTF-8 string");
    println!("{}", string);
}
