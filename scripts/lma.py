"""
dont ask
"""
#pylint: disable
import random
import time

processes = [
    'deleting item ',
    'truncating the flux data on record ',
    'callibrating vpn for record ',
    'de-centralizing load balancers on record ',
    'copying and pasting record '
]

ports = [
    '1522',
    '2309',
    '5434',
    '1432',
    '0800'
]

while True:
    record = random.randint(10000000,70000000)
    to_proc = random.choice(processes)
    to_port = random.choice(ports)
    print(to_proc + str(record) + ' through api port ' + to_port + '...')
    time.sleep(3)
    print('completed record ' + str(record) + '!')
    print({
        'record': record,
        'desc': 'event logged in local cache'
    })
    print('----------')
