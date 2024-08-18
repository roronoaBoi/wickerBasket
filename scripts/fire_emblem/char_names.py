"""log fe character names"""
# pylint: disable=invalid-name
chars = []
while True:
    print('Enter FE Character ' + str(len(chars) + 1) + ' or press Enter to stop...')
    character = input()
    if character == '':
        break
    chars = chars + [character]
print('The characters are:')
for character in chars:
    print(' ' + character)
