
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight



def save(filename, person):
    with open('person.txt', "w") as file:
        file.write(person.name + "\n")
        file.write(person.age + "\n")
        file.write(person.height + "\n")
        file.write(person.weight + "\n")

def load(filename):
    with open('person.txt', "w") as file:
        lines = [lines.strip() for line in file.readlines()]
    return lines
person = Person("bob", "15", "170","60")
print(int(person))