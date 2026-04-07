def main():
    """What is good!"""   
    run = True

    while run:
        password = input("Enter your password: ")
        if len(password) >= 6:
            print(check_password_strenght(password))
            run = False
        else:
            run = True

def check_password_strenght(password):
    """This function check the strength of a password!"""
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1
    else: 
        return "No Uppercase letter"

    if any(char.islower() for char in password):
        score += 1
    else:
        return "No lower letter"

    if any(not char.isalnum() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1
    else:
        return "No digit"

    if score == 5:
        return "Password very strong"
    elif score >= 3:
        return "Password strong"
    else:
        return "Password weak"


if __name__ == "__main__":
    main()
