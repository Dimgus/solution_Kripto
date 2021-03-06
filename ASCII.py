#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")
    
ASCII =  [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114,
49, 110, 116, 52, 98, 108, 51, 125]

for num in ASCII:
    print("".join([chr(num) for num in ASCII]))