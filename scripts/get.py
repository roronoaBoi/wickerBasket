# pylint: disable=invalid-name
"""
get.py

using get to check AND return a value from a dictionary
"""
#pylint: disable=line-too-long

weapon = {
    'class': 'sword',
    'mat': 'iron',
    'dur': 41
}

print('The ' + weapon['class'] + ' has ' + str(weapon.get('dur', 0)) + ' hits left.')
# The sword has 41 hits left.

print('The ' + weapon['class'] + ' has ' + str(weapon.get('duration', 0)) + ' hits left.') #'duration is not found, so 0 is returned.
# The sword has 0 hits left.

print('The ' + weapon['class'] + ' has ' + str(weapon.get('duration', 'literally zero')) + ' hits left.') #'duration is not found, so 'literally zero' is returned.
# The sword has literally zero hits left.
