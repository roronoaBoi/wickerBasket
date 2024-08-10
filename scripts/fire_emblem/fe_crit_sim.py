"""
fe_crit_sim.py

A module for simulating critical hits in a game scenario.
"""

import random
import sys
# determines enemy crit chance
enemy_crit = random.randint(1,100)
actual_hit = random.randint(1,100)
print('Enemy crit chance showing at ' + str(enemy_crit) + '% ' + 'likely' + '. Do you engage?')
print('Yes or No?')
answer = input()
while answer not in ['Yes','No']:
    print('You have to type Yes or No')
    answer = input()
if answer == 'Yes':
    if actual_hit <= enemy_crit:
        print('Enemy hit a critical. You lost your favorite character.')
        sys.exit()
    print('Nice - they missed their crit and you won the game!')
if answer == 'No':
    if actual_hit <= enemy_crit:
        print('Nice. You played it smart and you would have died.')
        sys.exit()
    print('They would have missed the crit. You could have won it all...')
