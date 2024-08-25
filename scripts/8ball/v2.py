"""
v2.py

An 8 ball that is an 8 ball because random.choice is way less painful than the v1 example.
if you try to be a funny guy, the 8 ball will be a jerk.
"""
import random
import sys

options = [
    'it is certain',
    'it is decidedly so',
    'yes definitely',
    'can\'t tell... try again!',
    'ask later...',
    'concentrate and ask again',
    'no',
    'outlook is not so good',
    'doubtful...'
]

hate_message = [
    'you\'re dumb for not pressing s... i\'m done.',
    'are you serious? learn what "s" is.',
    'i can\'t with you.',
    'i\'m done... press \'s\' next time.'
]
while True:
    print('press \'s\' to shake the magic 8 ball, or \'q\' tio quit.')
    shake = input()
    if shake not in ['q','s']:
        print('what\'s your name?')
        name = input()
        print('well ' + name + ' ... ' + random.choice(hate_message))
    elif shake == 'q':
        print('See ya!')
        sys.exit()
    else:
        print(random.choice(options))
