# This is the file in which the method of storing event data is described
# Learn CLASSES, figure out how to use them here
# when you want to define something but haven't used it yet use pass
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