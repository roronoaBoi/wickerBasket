import random

answer = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for guesses in range (1,7):
    print('Try to guess the number!')
    guess = int(input())
#indentation is KEY 0_0
    if guess > answer:
        print('Too d#$@ high!')
    elif guess < answer:
        print('Too low!')
    else:
        break

if guess == answer:
    print('Ayee... you got it! It took you ' + str(guesses) + ' tries!')
else:
    print('Sorry, you lose. The number I was thinking of is ' + str(answer) + '.')