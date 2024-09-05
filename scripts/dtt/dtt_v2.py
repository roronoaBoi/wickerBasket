"""
seeing if i can do tic tac toe off the dome... i cant, but I will be back!
"""
#pylint: disable=invalid-name
import sys

while True:
    print('Wins: %s, Losses: %s, Cat\'s Games: %s' % (W,L,T))
    while True:
        print('play tic tac toe! press (p) to play or (q) to quit')
        pinput = input()
        if pinput not in ['p','q']:
            print('do p or q')
        elif pinput == 'q':
            sys.exit()
        elif pinput == 'p':
            print('play time!')

        the_hash = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

        def print_board(board):
            """prints the board"""
            print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
            print('-+-+-')
            print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
            print('-+-+-')
            print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

        def x_move():
            print('X move')
            move = input()
            the_hash[move] = 'X'


        def o_move():
            print('O move')
            move = input()
            the_hash[move] = 'O'

# left off here
