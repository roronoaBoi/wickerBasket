"""
a generic coin toss
"""

import random
import sys

options = ['heads','tails']

while True:
    print('press (f) to flip the coin or (q) to quit')
    flip = input()
    if flip not in ['f','q']:
        print('nope...')
    elif flip == 'q':
        print('bye!')
        sys.exit()
    else:
        result = random.choice(options)
        print(result + '!')
