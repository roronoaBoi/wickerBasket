"""
template for rom game
"""
import random

items = [
    'this',
    'that',
    'other'
]

while True:
    print('press any key to ask a question!')
    p_input = input()
    if len(items) > 0:
        random_item = str(random.choice(items))
        print(random_item)
        items.remove(random_item)
    else:
        print('no more questions!')
        break
