import time
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file_loader import file_loader
def parse_question(questions):
    if isinstance(questions, dict):
        return questions.get("questions", [])
    elif isinstance(questions, list):
        return questions

def main():
    """
    1. lists of questions dictionary with options
        load questions from a file
        parse the file and create a list of question dictionaries
    2. Answer input from the users
        users option
        compare it with the answer field from the question dictionary
        increment the score if the answer is correct
        What is changing:
        Questions
        User answer
    """
    questions = parse_question(file_loader("questions.json"))
    total_score = 0
    labels = ["A","B", "C", "D"]

    for i, question in enumerate(questions):
        print(f"{i + 1} {question['question']}")
        for j, option in enumerate(question["options"]):
            print(f" ({labels[j]}.){option}", end="")

        while True:
            choice = input("\nAnswer (A|B|C|D): ").upper()
            if choice in labels:
                break
            print("Invalid input")

        index = labels.index(choice)
        selected_option = question["options"][index]

        if question["answer"] == selected_option:
                print("🎉 Correct")
                total_score += 1 
        else:
            print("🤦Wrong Answer")



    print(f"Your Total Score is {total_score}")


if __name__ == "__main__":
    main()