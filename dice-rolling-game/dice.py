import random

def main():
    COUNT = 0
    while True:
        choice = input("Want to roll dice? (y/n) ")

        if choice == "n":
            if COUNT > 0:
                print("Thanks for playing")
                break
            else:
                play_agin = input("Do you want to play again?")
                if play_agin == "n":
                    break
                else:
                    COUNT += 1
                    continue
        elif choice  == "y":
            COUNT += 1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print([dice1, dice2])
            continue
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()