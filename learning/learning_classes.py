
class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def age_in_n_years(self, n):
        return self.age + n

bob = Person("Bob", 168, 21)

print(bob.age)
print(bob.age_in_n_years(5))