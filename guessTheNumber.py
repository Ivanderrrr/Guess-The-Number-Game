import random

# guess the number
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

# ask the player to guess 6 times
for guessNumber in range(1, 7):
    print('Take a guess')
    guess = int(input())

# validation guess and secretNumber
    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break
    
if guess == secretNumber:
    print("good job! you guessed my number in " +
              str(guessNumber) + " guesses!")
else:
    print("Nope. this number is "+ str(secretNumber) +".")