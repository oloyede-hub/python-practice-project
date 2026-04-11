import json
def load_questions():
    try:
        with open("questions.json", "r" ) as f:
                return json.load(f)
    except:
         return []

if __name__ == "__load_question__":
    load_questions()