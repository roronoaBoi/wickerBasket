# print('paste the token')
# token = input()

# def apiCall(token):
#     print('i just performed an API call to https://google.com with the token ' + token)

# if len(token) == 10:
#     apiCall(token)
# else:
#     print('the token is not the correct length')

import random

def eight_ball(answer):
    if answer == 1:
        return 'Hey, I\'m not going to do this 9 times...'
    if answer == 2:
        return 'i\'m serious... it would be too much busy work...'
    if answer == 3:
        return 'you got the third option...'
    
print('press \'s\' to shake the magic 3 ball')
shake = input()

if shake != 's':
    print('i\'m done... press \'s\' next time')
else:
    item = random.randint(1,3)
    print(eight_ball(item))

