# pylint: disable=invalid-name
"""
dictionary.py

basics of dictionaries and keys, values, and items
"""
#pylint: disable=consider-iterating-dictionary
#pylint: disable=expression-not-assigned

weapon = {
    'class': 'sword',
    'mat': 'iron',
    'dur': 41
}

#basics of keys, values, items
# for i in weapon.keys():
#     print(i)

# for i in weapon.values():
#     print(i)

# for i in weapon.items():
#     print(i)

#iterations with dictionaries
# for k, v in weapon.items():
#     print('Key: ' + k + ' value: ' + str(v))

#check if key is in dictionary
'class' in weapon.keys() # returns True
