"""
initial lint format
"""
while True:
    print('Who is the repo owner?')
    name = input()
    if name != 'roronoaBoi':
        continue
    print('Thanks possibly ' + name + '. What is the name of the repo this code is in?')
    repoName = input()
    if repoName == 'wickerBasket':
        break
print('I like what you got. Good job!')
