"""in not in"""
items = ['phone', 'wallet', 'computer']

print('What item are you searching for?')
item = input()

if item in items:
    print('Yes! We have your ' + str(item) + '!')
else:
    print('Sorry we don\'t have your ' + str(item) + '!')
