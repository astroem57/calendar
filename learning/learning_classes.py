
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

class Book:
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

book = Book("The Picture of Dorian Gray", "Oscar Wilde", 201)
print(book.title)
print(book.author)
print(book.page)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance+= amount
    
    def withdraw(self, amount):
        self.balance-= amount

account = BankAccount("Me", 100)
account.deposit(50)
account.withdraw(40)

print(account.owner)
print(account.balance)