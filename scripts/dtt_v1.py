"""
seeing if i can do tic tac toe off the dome
"""
#pylint: disable=invalid-name
# import sys

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

# while True:
#     print('play tic tac toe! press (p) to play or (q) to quit')
#     pinput = input()
#     if pinput not in ['p','q']:
#         print('do p or q')
#     elif pinput == 'q':
#         sys.exit()
#     elif pinput == 'p':
#         print('play time!')

turn = 'X'

for i in range(9):
    print_board(the_hash)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_hash[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_hash)
