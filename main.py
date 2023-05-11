import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("Try to guess the secret number within the chosen range.")
  
    while True:
        difficulty = input("Select a difficulty level (easy, medium, hard): ").lower()
        
        if difficulty not in ['easy', 'medium', 'hard']:
            print("Invalid difficulty level. Please try again.")
            continue

        if difficulty == 'easy':
            low = 1
            high = 50
            attempts_allowed = 10
        elif difficulty == 'medium':
            low = 1
            high = 100
            attempts_allowed = 7
        else:
            low = 1
            high = 200
            attempts_allowed = 5

        print(f"You've selected {difficulty} level. Guess a number between {low} and {high}.")

        number = random.randint(low, high)
        attempts = 0

        while attempts < attempts_allowed:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break

        if attempts >= attempts_allowed:
            print(f"Game over! The number was {number}. Better luck next time!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

guess_the_number()
