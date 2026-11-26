
import random

def number_guessing_game():
    print("================================")
    print("     NUMBER GUESSING GAME")
    print("================================")
    
    secret_number = random.randint(1, 100)
    attempts = 7

    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it!")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == secret_number:
                print("Congratulations! You guessed it correctly!")
                print(f"The number was {secret_number}.")
                break

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            attempts -= 1
            print(f"Attempts remaining: {attempts}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == 0:
        print("\nGame Over!")
        print(f"The correct number was {secret_number}.")

    print("\nThanks for playing!")

number_guessing_game()
