"""Utilities for handling IEEE 754 floating point special values

This class implements constants and functions for working with IEEE754
double-precision special values.  It provides constants for NaN (Not a
Number), NegInf (Negative Infinity), PosInf (Positive Infinity), and
Inf (also Positive Infinity), as well as functions to test for these
values.

The code is implemented in pure python by taking advantage of the
'struct' standard module.  Some efficiency could be gained by
translating the core routines into C.

See <http://babbage.cs.qc.edu/courses/cs341/IEEE-754references.html>
for a description of the IEEE 754 floating point standard.

Author: Gregory R. Warnes <gregory_r_warnes@groton.pfizer.com>
Date::  2003-03-25
Version 0.5.0

"""

ident = "$Id$"

__version__ = "0.5.0"

from struct import pack, unpack

# check endianess
_big_endian = pack('i',1)[0] != '\x01'

# and define appropriate constants
if(_big_endian): 
    HW=0
    LW=1
    
    NaN = unpack('d', '\x7F\xFF\xFF\xFF\xFF\xFF\xFF\xFF')[0]
    Inf = unpack('d', '\x7F\xF0\x00\x00\x00\x00\x00\x00')[0]
    PosInf = Inf
    NegInf = -Inf
    
else:
    HW=1
    LW=0

    NaN = unpack('d', '\x00\x00\x00\x00\x00\x00\xf8\xff')[0]
    Inf = unpack('d', '\x00\x00\x00\x00\x00\x00\xf0\x7f')[0]
    PosInf = Inf
    NegInf = -Inf

def _double_as_longs(dval):
    "Use unpack to decode a double precision float into two long integers"
    tmp = unpack('ll',pack('d', dval))
    return (tmp[HW], tmp[LW] )


##
## Functions to extract components of the IEEE 754 floating point format
##

def sign(dval):
    "Extract the sign bit from a double-precision floating point value"
    ll = _double_as_longs(dval)
    return ll[0] >> 31 & 0x01 

def exponent(dval):
    """Extract the exponentent bits from a double-precision floating
    point value.

    Note that for normalized values, the exponentdent bits have an offset
    of 1023. As a consequence, the actual exponentent is obtained
    by subtracting 1023 for the value returned by this function
    """
    ll = _double_as_longs(dval)
    return ( ll[0] >> 20 ) & 0x7ff

def mantissa(dval):
    ll = _double_as_longs(dval)
    mantissa1 = ( ll[0] & 0xfffffL ) << 32
    mantissa2 = ll[1] 
    return mantissa1 + mantissa2

##
## Functions to test for IEEE 754 special values
##

def is_NaN(value):
    "Determine if the argument is a IEEE 754 NaN (Not a Number) value."
    return ( exponent(value)==0x7ff and mantissa(value)!=0 ) 

def is_Infinite(value):
    """Determine if the argument is an infinite IEEE 754 value (positive
    or negative inifinity)"""
    return ( exponent(value)==0x7ff and mantissa(value)== 0 )

def is_Finite(value):
    """Determine if the argument is an finite IEEE 754 value (i.e., is
    not NaN, positive or negative inifinity)"""
    return ( exponent(value)!=0x7ff )


def is_Inf(value):
    "Determine if the argument is a IEEE 754 positive infinity value"
    return ( sign(value)==0 and exponent(value)==0x7ff \
             and mantissa(value)== 0 ) 

is_PosInf = is_Inf

def is_NegInf(value):
    "Determine if the argument is a IEEE 754 negative infinity value"
    return ( sign(value)==1 and exponent(value)==0x7ff and \
             mantissa(value)== 0 ) 



