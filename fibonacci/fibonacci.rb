require 'ffi'

module Fibonacci
  extend FFI::Library
  ffi_lib 'target/release/libfibonacci.so'
  attach_function :fibonacci, [:uint32], :uint64
end

numbers = (0..9).map { |n| Fibonacci.fibonacci(n) }
puts numbers.join(', ')
