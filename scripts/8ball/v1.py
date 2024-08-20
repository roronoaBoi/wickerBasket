"""
v1.py

An 8 ball that wasnt actually an 8 ball... 
"""
import random

def eight_ball(answer):
    """
    This function takes an answer and returns a string. more like a three ball...
    Args:
        x (int): The input integer.
    Returns:
        a string
    """
    if answer == 1:
        return 'Hey, I\'m not going to do this 9 times...'
    if answer == 2:
        return 'i\'m serious... it would be too much busy work...'
    if answer == 3:
        return 'you got the third option...'
    return 'invalid input'

print('press \'s\' to shake the magic 3 ball')

shake = input()

if shake != 's':
    print('i\'m done... press \'s\' next time')
else:
    item = random.randint(1,3)
    print(eight_ball(item))
