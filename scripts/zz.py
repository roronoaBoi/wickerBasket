# pylint: disable=invalid-name
"""
zz.py

simple zigzag automation
"""

import time
import sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end = '')
        print('**********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent +1
            if indent == 50:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

# press crtl + c to quit
except KeyboardInterrupt:
    sys.exit()
