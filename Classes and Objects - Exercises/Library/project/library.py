from typing import List
from project.user import User

class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if author in self.books_available.keys():
            for value in self.books_available.values():
                for value_ in value:
                    if book_name == value_:
                        user.books.append(book_name)
            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {book_name: days_to_return}
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            
        rented_book_days = 0
        for _value_ in self.rented_books.values():
            if book_name in _value_.keys():
                rented_book_days = _value_[book_name]
        return f'The book "{book_name}" is already rented and will be available in {rented_book_days} days!'
    
    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            for value in self.rented_books.values():
                del value[book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"