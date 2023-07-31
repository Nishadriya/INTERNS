class Book:
     def __init__(self,book_id,title,author,copies):
          self.book_id = book_id
          self.title = title
          self.author = author
          self.copies = copies

class Member:
     def __init__(self,member_id,name): 
          self.member_id = member_id
          self.name = name

class Library:
     def __init__(self):
          self.books = []
          self.members = []
          self.transaction = []

def add_book(self,book_id,title,author,copies):
     book = Book(book_id,title,author,copies) 
     self.books.append(book)   

def add_member(self,member_id,name):
     member = Member(member_id, name) 
     self.members.append(member) 

def issue_book(self,member_id,book_id):
     member = next((m for m in self.members if m.member_id == member_id), None) 
     book = next((b for b in self.books if b.book_id == book_id), None)
     
     if member and book:
          if book.copies > 0:
               book.copies -= 1
               transaction = (member_id, book_id)
               self.transactions.append(transaction)
               return f"Book '{book.title}' issued to {member.name}."
          else:
               return "Book is not available."
     else:
          return "Member or book not found."

def display_books(self):
     for book in self.books:
          print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Copies: {book.copies}")

def display_members(self):
     for member in  self.members:
          print(f"Member ID: {member.member_id}, Name: {member.name}")


library = Library()

library.add_member(101, "john doe")
library.add_member(102, "meera desai")



library.add_member(101, "john doe")
library.add_member(102, "meera desai")

library.display_books()
library.display_members()

print(library.issue_book(101, 1))
print(library.issue_book(102, 1))

library.display_books()