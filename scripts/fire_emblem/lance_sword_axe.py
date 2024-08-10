import random, sys

print('Lance, Sword, or Axe')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    print('Type (l)ance, (s)word, (a)xe, or (quit)')
    player_input = input()
    if player_input == 'q':
        print('Thanks for playing!')
        sys.exit()
    if player_input not in ['l','s','a','q']:
        print('You have to type (l)ance, (s)word, (a)xe, or (quit)!')

    if player_input == 'l':
        print('Lance vs...')
    elif player_input == 's':
        print('Sword vs...')
    elif player_input =='a':
        print('Axe vs...')

    # display computer choice
    comp_int = random.randint(1,3)

    if comp_int == 1:
        comp_input = 'l'
        print('... lance!')
    elif comp_int == 2:
        comp_input = 's'
        print('...sword!')
    elif comp_int == 3:
        comp_input = 'a'
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

