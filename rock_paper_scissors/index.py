import random
import time
def main():
    """Rock paper scissors"""

    print("---ROCK PAPER SCISSOR GAME---")
    print("Chose between rock or scissors by typing ANY of these!(R|P|S)")
    choice = ["rock", "paper", "scissors"]
    winner = ""
    random_choice = round(random.randint(0, 2))

    while True:
        user_choice = input("Enter choice (R|P|S): ").upper().strip()
        if user_choice != ("rock" or "paper" or "scissors"):
            break

        computer_choice = choice[random_choice]
        print("Computers Choice: ", computer_choice)
        
        if computer_choice == "paper" and user_choice == "rock":
            winner = "Computer won"
        elif computer_choice == "rock" and user_choice == "scissors":
            winner = "Computer won"
        elif computer_choice == "scissors" and user_choice == "paper":
            winner = "Computer won"
        elif computer_choice == "paper" and user_choice == "scissors":
            winner = "You won🎉"
        elif computer_choice == "rock" and user_choice == "paper":
            winner = "You won🎉"
        elif computer_choice == "scissors" and user_choice == "rock":
            winner = "You won🎉"
        else:
            winner = "Tile Game"
            
        print(f"{winner}")

        time.sleep(1)
        try_again = input("Want to play again? (Y|N)").upper()
        if try_again != "y":
            break

if __name__ == "__main__":
    main()