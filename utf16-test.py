#!/usr/bin/python
# -*- coding: utf-8 -*-
import struct
import sys

def manual_decode_utf16le(s):
    unicodes = []
    code = None
    i = 0
    while i < len(s):
        # Read 16-bit natural number (LE).
        codepoint = struct.unpack("<H", s[i:i + 2])[0]

        if ((codepoint >= 0x0000 and codepoint <= 0xD7FF) or
            (codepoint >= 0xE000 and codepoint <= 0xFFFF)):
            unicodes.append(codepoint)
            i += 2
            continue
        
        if code is None:
            # We are dealing with the first 16-bit number.
            # It is worth making sure that this is the case.
            if not (codepoint >= 0xD800 and codepoint <= 0xDBFF):
                print>>sys.stderr, "Invalid UTF-16 string (1)."
                return None
            code = (codepoint & 0x3ff) << 10
            i += 2
            continue
        
        # We are dealing with the second 16 bit number.
        # As above, it is worth checking if this is the case.
        if not (codepoint >= 0xDC00 and codepoint <= 0xDFFF):
            print>>sys.stderr, "Invalid UTD-16 string (2)."
            return None

        code |= (codepoint & 0x3ff)
        code += 0x1000
        unicodes.append(code)
        code = None
        i += 2
        
    return unicodes

s = u"Cat pictogram: \U0001f408"
sutf16 = s.encode("utf-16-le")
for ch in manual_decode_utf16le(sutf16):
    print ("U+%x " %ch,)
print ("")