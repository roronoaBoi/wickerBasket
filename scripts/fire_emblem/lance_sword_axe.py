"""a simple game based on the fire emblem triangle"""
# pylint: disable=invalid-name
# pylint: disable=multiple-imports
# pylint: disable=consider-using-f-string
import random, sys

print('Lance, Sword, or Axe')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True:
        print('Type (l)ance, (s)word, (a)xe, or (quit)')
        player_input = input()
        if player_input == 'q':
            print('Thanks for playing!')
            sys.exit()
        if player_input in ['a','s','l','q']:
            break
        print('You have to type (l)ance, (s)word, (a)xe, or (quit)!')

    if player_input == 'l':
        print('Lance vs...')
    elif player_input == 's':
        print('Sword vs...')
    elif player_input =='a':
        print('Axe vs...')

    # display computer choice
    ops = ['l','s','a']
    # replaced old code which used random.int with random.choice
    comp_input = random.choice(ops)

    if comp_input == 'l':
        print('... lance!')
    elif comp_input == 's':
        print('...sword!')
    elif comp_input == 'a':
        print('... axe!')

    if player_input == comp_input:
        print('Draw!')
        ties = ties + 1
    elif player_input == 'l' and comp_input == 's':
        print('Victory!')
        wins = wins + 1
    elif player_input == 's' and comp_input == 'a':
        print('Victory!')
        wins = wins + 1
    elif player_input == 'a' and comp_input == 'l':
        print('Victory!')
        wins = wins + 1
    elif player_input == 'l' and comp_input == 'a':
        print('Defeat!')
        losses = losses + 1
    elif player_input == 's' and comp_input == 'l':
        print('Defeat!')
        losses = losses + 1
    elif player_input == 'a' and comp_input == 's':
        print('Defeat!')
        losses = losses + 1
