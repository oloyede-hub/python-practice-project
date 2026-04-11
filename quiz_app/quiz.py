from load_questions import load_questions
import time
def parse_question(questions):
    if not questions:
        return []
    else:
        return questions["questions"]

def main():
    """
    1. lists of questions dictionary with options
        load questions from a file
        parse the file and create a list of question dictionaries
    2. Answer input from the users
        users option
        compare it with the answer field from the question dictionary

        What is changing:
        Questions
        User answer
    """
    questions = parse_question(load_questions())
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
            print("🤦‍♂️Wrong Answer")



    print(f"Your Total Score is {total_score}")


if __name__ == "__main__":
    main()