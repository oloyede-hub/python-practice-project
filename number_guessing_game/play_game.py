import random
from set_difficulty import set_difficulty
def play_game():
    """
    1. Generate a random number
    2. Asked for users guess
    3. break out of the loop if guess is correct
    """
    ceil_number = set_difficulty()
    random_int = random.randint(1, ceil_number)
    attempts = 0
    # max_attempts = 10

    print(f"Guess a number between 1 and {ceil_number}")
    
    while True:
        try:
            guess = int(input("Your guess?"))
        except ValueError:
            print("Invalid Number")
            continue

        attempts += 1
        
        if guess == random_int:
            print(f"Correct🔥! You guessed it in {attempts} attempts")
            return
        elif guess > random_int:
            print("Too High")
        else:
            print("Too Low")

if __name__ == "__play_game__":
    play_game()
