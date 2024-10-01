"""
basics of PyInputPlus in a venv
"""
#pylint: disable=import-error
#added the above disble and the below type ignore as this import is working correctly
import pyinputplus as pyip # type: ignore

print('type a number')

damage = pyip.inputNum()

print(f'{damage} is valid')
