"""
simple script to apply pyinputplus and regex
"""

import random
import time
import pyinputplus as pyip # type: ignore

#pylint: disable= consider-using-f-string, invalid-name

numOfQs = 10
answers = 0

for qnum in range(numOfQs):
    num_one = random.randint(0,9)
    num_two = random.randint(0,9)

    board = '#%s: %s x %s = ' % (qnum, num_one,num_two)

    try:
        pyip.inputStr(board, allowRegexes = ['^%s$' % (num_one * num_two)],
                      blockRegexes = [('.*', 'Wrong!')],
                      timeout = 5, limit = 3)
    except pyip.TimeoutException:
        print('ooh, out of time')
    except pyip.RetryLimitException:
        print('no more attempts allowed...')
    else:
        print('yeah!')
        answers += 1
    time.sleep(1)
print('Score: %s / %s' % (answers,numOfQs))
