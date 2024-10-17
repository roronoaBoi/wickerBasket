"""
api interaction
"""

import requests

URL = 'https://randomuser.me/api/'

random_user = requests.get(URL,timeout = 5)

if random_user.status_code == 200:
    data = random_user.json()
    print(data)
else:
    print('bad call')
