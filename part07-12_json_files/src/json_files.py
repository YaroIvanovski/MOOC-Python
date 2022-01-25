
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        persons = json.loads(data)
    
    for person in persons:
        hobbies = ", ".join(person['hobbies'])
        print(f'{person["name"]} {person["age"]} years ({hobbies})')

if __name__ == "__main__":
    print_persons("file1.json")
    print_persons("file2.json")
    print_persons("file3.json")
    print_persons("file4.json")

"""Suggested solution
import json
def print_persons(filename: str):
    with open(filename) as file:
        content = file.read()
        persons = json.loads(content)

    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f"{name} {age} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file1.json")
    print_persons("file2.json")
    print_persons("file3.json")
    print_persons("file4.json")
"""   
