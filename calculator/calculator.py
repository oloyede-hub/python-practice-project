import argparse

def main():
    # Argparse instantiation with desciption
    parser = argparse.ArgumentParser(description="Input your Math operation here!")
    # Addition of required position argument
    parser.add_argument("first_operand", help="Your first operand")
    parser.add_argument("operator", help="Your first operator (+|-|/|x)")
    parser.add_argument("second_operand", help="Your second operand")
    args = parser.parse_args()

    
    while True:
        if args:
            num1 = float(args.first_operand)
            num2 = float(args.second_operand)
            # num1 = float(input("Second: ")
            # num2 = float(input("Second: "))
            


            operation = args.operator

            if operation == "+":
                result = addition(num1, num2)
            elif operation == "-":
                result = subtraction(num1, num2)
            elif operation == "/":
                if num2 == 0:
                    result = "Can't divide an integer by zero!"
                else:
                    result = division(num1, num2)
            elif operation == "x":
                result = multiplication(num1, num2)
            else: 
                result = "Invalid Math operation"


            print(f"Result: {result}")
            again = input("Do you want to calculate again? (yes|no) ").lower()
            if again == "no":
                break

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2
def division(num1, num2):
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2



if __name__ == "__main__":
    main()
