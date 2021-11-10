import random

r = random.randint(1,9)

print('Number guessing game')
print('Guess a number (between 1 to 9)')

guess=None

while guess != r:
    guess=input('Choose a numbers: ')

while chances < 5:

if guess == r :
        print('Congratulation u won')

else:
        print('you lose')