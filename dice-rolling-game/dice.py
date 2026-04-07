# import sys
# import random
# import re
# import argparse

# def main():
#     dice = [1,2,3,4,5,6]
#     count = 0
#     while True:
#         roll = input("Roll the dice? (y/n): ")
#         if  not re.search("^(y|n)$", roll):
#             print("Invalid Input")
#         if roll == "y":
#             dice_output = random.choices(dice, k=2)
#             count += 1
#             print(dice_output)
#             continue
#         else:
#             if count >= 1:
#                 print("Thanks for playing")
#                 break
#             else:
#                 continue



# if __name__ == "__main__":
#     main()

import random

playing = True
count = 0
while playing:
    choice = input("Want to roll dice? (y/n) ")

    if choice == "n" and count > 1:
        print("Thanks for playing")
        playing = False
    elif(choice  == "y"):
        count += 1
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print([dice1, dice2])
        continue
    else:
        print("Invalid Input")