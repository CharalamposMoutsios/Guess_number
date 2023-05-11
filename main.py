import random


# Define function to get player input and validate it
def get_input(prompt, type_=None, min_=None, max_=None, range_=None):
    while True:
        try:
            value = type_(input(prompt))
            if min_ is not None and value < min_:
                print(f"Value must be greater than or equal to {min_}.")
            elif max_ is not None and value > max_:
                print(f"Value must be less than or equal to {max_}.")
            elif range_ is not None and value not in range(*range_):
                print(f"Value must be between {range_[0]} and {range_[1]}.")
            else:
                return value
        except ValueError:
            print("Invalid input.")


# Define function to play the game
def play_game():
    print("Welcome to Guess the Number!")
    
    # Get difficulty level from the player
    level = get_input("Select a difficulty level (1 = easy, 2 = medium, 3 = hard): ",
                      type_=int, min_=1, max_=3)
    
    # Define difficulty levels
    if level == 1:
        attempts = 10
        low = 1
        high = 50
    elif level == 2:
        attempts = 7
        low = 1
        high = 100
    else:
        attempts = 5
        low = 1
        high = 200
    
    # Generate random number
    secret_number = random.randint(low, high)
    
    # Loop until the player guesses the number or runs out of attempts
    for attempt in range(1, attempts + 1):
        print(f"You have {attempts - attempt + 1} attempts remaining.")
        guess = get_input(f"Guess a number between {low} and {high}: ",
                          type_=int, range_=(low, high))
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            return True
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    # If the player runs out of attempts, reveal the secret number and end the game
    print(f"Game over! The secret number was {secret_number}.")
    return False

# Main game loop
while True:
    play_game()
    response = input("Do you want to play again? (y/n) ")
    if response.lower() != "y":
        print("Thanks for playing!")
        break
