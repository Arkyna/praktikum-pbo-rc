class Book:
    def __init__(self, book_name, ISBN, author, publisher, genre, available=True):
        self.book_name = book_name
        self.ISBN = ISBN
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.available = available

    def get_title(self):
        return self.book_name

    def get_isbn(self):
        return self.ISBN

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def is_available(self):
        return self.available

    def check_in(self):
        if not self.available:
            self.available = True
            print(f"{self.book_name} has been checked in.")
        else:
            print(f"{self.book_name} is already available.")

    def check_out(self):
        if self.available:
            self.available = False
            print(f"{self.book_name} has been checked out.")
        else:
            print(f"{self.book_name} is not available for checkout.")

# Example usage:
my_book = Book("The Great Gatsby", "123456789", "F. Scott Fitzgerald", "Charles Scribner's Sons", "Fiction")

print(my_book.get_title())
print(my_book.is_available())
my_book.check_out()
print(my_book.is_available())
my_book.check_in()
