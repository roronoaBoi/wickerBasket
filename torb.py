# script with inputs (un-indent)
    # print('paste the api token?')
    # token = input()
    # print('check ' + token)
    # print('token verified')
    # is there an equivalent to input for nodeJS

#len for py (not zero-based indexing)
    # dorb = 'thalia'
    # dreeb = ['thalia', 'roby']
    # print(len(dorb))
    # print(len(dreeb))

#numbers and data
    # cake = 29
    # sent = 'the number is '
    # # print(sent + cake) returns error because num and string
    # print(sent + str(cake)) # changes num to string

#comparison basics (with if then)
    # token = 'asdf12345'
    # validator = 8
    # option2 = len(token)
    # if option2 == validator :
    #     print('token correct length')
    # else:
    #     print('token length is wrong')

#nested if then
    # print('Hello. Please tell me your name.')
    # name = input()
    # print('Thank you, ' + name + '.')
    # if name == 'Roby' :
    #     print('You are ' + name)
    #     print('Create a password')
    #     password = input()
    #     if len(password) >= 8:
    #         print('Good password!')
    #     else:
    #         print('that password is shite...')
    # else:
    #     print("I actually don't know you.")
    #     print('This conversation is over...')

#ITERATIONS
    # item = 0
    # while item <= 5:
    #     print('run ' + str(item) + ' complete!')
    #     item = item + 1
    # items = ['rick','morty'] #lists zbi
    # position = 0

    # while position < len(items):
    #     print('url/' + items[position])
    #     position = position + 1

# basic call with pretty JSON
    # import requests
    # import json 
    # token = '257da7a25dafdf453ff7511eceafdca3d6a5b0b7e301504733dfadb199aaa7c5'
    # url = "https://api.safetyculture.io/feed/users"
    # headers = {
    #     "accept": "application/json",
    #     "sc-integration-id": "sc-readme",
    #     "Authorization": "Bearer " + token
    # }
    # response = requests.get(url, headers=headers)
    # cleaned = json.loads(response.text)
    # toRead = json.dumps(cleaned, indent = 4)
    # print(toRead)

    #pg.37
    # name = ''
    # while name != 'Thalia':
    #     print('Please type your name')
    #     name = input()
    # print("Thank you!")

#pg.39
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thanks!')