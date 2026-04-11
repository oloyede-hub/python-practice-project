from countdown import countdown

def main():

    while True:
        try:
            minutes = int(input("Enter your countdown(minutes): "))
            countdown(minutes)
            break
        except ValueError:
            print("Invalid input!")


if __name__ == "__main__":
    main()