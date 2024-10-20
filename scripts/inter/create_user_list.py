"""
create list of users
"""

import requests

URL = 'https://randomuser.me/api/'

while True:
    print('how many users would you like to generate?')
    user_count = input()
    if user_count.isnumeric():
        print(f'creating {user_count} users')
        user_list = []
        i = 0
        while i < int(user_count):
            response = requests.get(URL, timeout = 5)
            data = response.json()
            email = data['results'][0]['email']
            user_list.append(email)
            i = i + 1
        print(user_list)
        break
    print(f'{user_count} is not a number')
