import json
def file_loader(path=""):
    try:
        with open(path, "r" ) as f:
                return json.load(f)
    except:
         return []

if __name__ == "__file_loader__":
    file_loader()


