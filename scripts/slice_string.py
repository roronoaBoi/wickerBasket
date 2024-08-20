# pylint: disable=invalid-name
"""
slice_string.py

slicing strings with basic index
see basic_slice_substr in bokken for js equivalent!
"""

name = 'roronoa'

nickname = name[0:2] # index 2 is exclusive so:
#  Index:  0  1  2  3  4  5  6
#          r  o  r  o  n  o  a
# index 2 is not included in the return

print('hello ' + nickname)
