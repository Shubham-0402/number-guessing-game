import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed it.")
        if attempts <= 3:
            print("you are kind of mind reader , you guessed it in only ", attempts,"attempts")
        else:
            print("very good , only ",attempts,"attempts")
        
        break

