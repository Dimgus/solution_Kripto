#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

xor = "label"

for c in xor:
    print("".join([chr(ord(c)^13) for c in xor]))