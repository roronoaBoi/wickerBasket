"""
simple concept for validating input
(ex, token) for script
"""

while True:
    print('input token for automation') #example: should be alphanumeric and 32 characters
    # voCwFWnmr4v50fAQzY2GbGPEHS4k0mBa
    token = input()
    print('validating token...')
    if token.isalnum() and len(token) == 32:
        print('token valid... automation proceeding')
        break
    if token.isalnum() is False:
        print('token should be alphanumeric only')
    elif len(token) != 32:
        print('token should be 32 characters')
