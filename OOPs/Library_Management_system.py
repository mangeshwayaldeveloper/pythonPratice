class Library:
 no_of_books = 0
 books = []

 def __init__(self, newBook):
  self.newBook = newBook

 def addBooks(self):
  self.books.append(self.newBook)

 def show(self):
  self.no_of_books = len(self.books)
  print(f"The Number of books are {self.no_of_books}")


obj = Library("book3")
obj.show()
obj2 = Library("book4")
obj.show()
