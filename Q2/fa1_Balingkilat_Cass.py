class Publication:
def __init__(self, title, author):
self._title = title
self._author = author


def title(self):
return self._title


def author(self):
return self._author

def display(self):
print(f"Title: {self.title}, Author: {self.author}")


class Book(Publication):
def __init__(self, title, author, number_of_pages):
super().__init__(title, author)
self.number_of_pages = number_of_pages


def number_of_pages(self):
return self._number_of_pages


def number_of_pages(self, value):
if value <= 0:
print("The number of pages must be positive")
else:
self._number_of_pages = value

def display(self):
print(f"Title: {self.title}, Author: {self.author}, Pages: {self.number_of_pages}")


class Magazine(Publication):
def __init__(self, title, author, issue_number):
super().__init__(title, author)
self.issue_number = issue_number


def issue_number(self):
return self._issue_number

def issue_number(self, value):
if value <= 0:
print("The issue number must be positive")
else:
self._issue_number = value

def display(self):
print(f"Title: {self.title}, Author: {self.author}, Issue: {self.issue_number}")


if __name__ == "__main__":
print("=== Library Materials ===\n")

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
b2 = Book("1984", "George Orwell", 328)
b1.display()
b2.display()
print()

m1 = Magazine("National Geographic", "Various", 2023)
m2 = Magazine("TIME", "Edward Felsenthal", 1923)
m1.display()
m2.display()
print()

p1 = Publication("Silent Spring", "Rachel Carson")
p2 = Publication("Brave New World", "Aldous Huxley")
p1.display()
p2.display()
print()

print("--- Validation Tests ---\n")

invalid_book = Book("Bad Book", "Unknown Author", 0)
invalid_book.display()
print()

invalid_magazine = Magazine("Fake News", "Anonymous", -5)
invalid_magazine.display()
