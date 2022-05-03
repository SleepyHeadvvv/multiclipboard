import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    if command == "save":
        key = input('Insert a key:\n-')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved.")
    elif command == "load":
        key = input('Insert a key:\n-')
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key nonexistent")
    elif command == "list":
        print(data)
    else:
        print("Pick one of the following commands: save, load or list")
else:
    print("Pick one command")
