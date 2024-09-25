"""
basics of PyInputPlus in a venv
"""
#pylint: disable=import-error
#added the above disble... as this import is working correctly
import pyinputplus as pyip

print('type a number')

damage = pyip.inputNum()

print(f'{damage} is valid')
