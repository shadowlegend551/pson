import json

def load(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'File not saved: No file called "{filename}".')


def save(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            json.dump(dictionary, file)
    except FileNotFoundError:
        print(f'File not saved: No file called "{filename}".')


def save_formatted(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            json.dump(dictionary, file, indent=4)
    except FileNotFoundError:
        print(f'File not saved: No file called "{filename}".')

