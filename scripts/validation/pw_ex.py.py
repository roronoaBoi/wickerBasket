"""
basics of PyInputPlus in a venv
"""
#pylint: disable=import-error
#added the above disble and the below type ignore as this import is working correctly
import pyinputplus as pyip # type: ignore

while True:
    print('type your password')
    password = pyip.inputPassword()
    print('type your password again to confirm')
    passwordC = pyip.inputPassword()
    if password == passwordC:
        break
    print('passwords do not match')

print('passwords match')
