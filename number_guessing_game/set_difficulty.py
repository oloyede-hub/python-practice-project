import sys
def set_difficulty():
    """Set the level of difficuty and return
    return range
    """
    print("\nChoose difficulty")
    print("1. Easy: (1-10)")
    print("2. Medium (1-50)T")
    print("3. Hard (1-100)")
    print("4. exit")

    try:
        choice = int(input("Select Option: "))
    except ValueError:
        print("Choose a valid number!")
        return set_difficulty()

    if choice == 1:
        return 10
    elif choice == 2:
        return 50
    elif choice == 3:
        return 100
    elif choice == 4:
        sys.exit()
    else:
        print("Invalid option")
        return set_difficulty()
    