# this is a guess number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinging of a number between 1 and 20')
secretNumber = random.randint(1, 20)

#print('DEBUG: Secret number is ' + str(secretNumber)) to make sure it works, can check like this

for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this condition is for the correct answer!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))
          
