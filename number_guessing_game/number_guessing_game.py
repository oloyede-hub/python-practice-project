from play_game import play_game
def main():
    play_game()
    while True:
        play_again = input("\nWould you like to play gain (yes|no)?").lower()
        if play_again == "no":
            print("Goodbye! See you next time")
            break
        elif play_again != ("yes" or "no"):
            print(f"Invalid option: ({play_again})")
            continue
        else:
            play_game()
            
        

if __name__ == "__main__":
    main()