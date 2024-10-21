"""
create csv of users
"""

import csv
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
            user_list.append([email])
            i += 1
        if int(user_count) > 0:
            with open('users.csv', 'w', newline = '', encoding='utf-8') as csvfile:
                user_writer = csv.writer(csvfile, delimiter=' ',
                                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
                # for user in user_list:
                    # user_writer.writerow(user)
                user_writer.writerows(user_list)
        break
    print(f'{user_count} is not a number')
