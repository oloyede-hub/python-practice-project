
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file_loader import file_loader

def main():
    stories = file_loader("stories.json")
    for i,story in enumerate(stories):
        print(f"\n{i + 1}. {story}")
        while True:
            noun = input("Enter a noun: ")
            verb = input("Enter a verb: ")
            new_text = story.split(" ")
            noun_index = new_text.index("{noun}")
            verb_index = new_text.index("{verb}")

            new_text[noun_index] = noun 
            new_text[verb_index] = verb 
        
            print(f'{" ".join(new_text)}')
            print("Hurray🎉")
            break

if __name__ == "__main__":
    main()