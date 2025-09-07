class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}"


class Membership:
    def __init__(self, user_type):
        self.user_type = user_type
        self.borrow_limit = 3 if user_type == "Student" else 5


class Student(Person):
    def __init__(self, name, email, student_id, course):
        super().__init__(name, email)
        self.student_id = student_id
        self.course = course
        self.membership = Membership("Student")
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.membership.borrow_limit:
            print(f"❌ {self.name} has reached the borrowing limit ({self.membership.borrow_limit}).")
            return
        if book.copies_available > 0:
            book.copies_available -= 1
            self.borrowed_books.append(book)
            print(f"✅ {self.name} borrowed {book.title}")
        else:
            print(f"❌ {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.copies_available += 1
            print(f"🔄 {self.name} returned {book.title}")
        else:
            print(f"❌ {self.name} does not have {book.title} borrowed.")

    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"📚 {self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"ℹ️ {self.name} has no borrowed books.")


class Teacher(Person):
    def __init__(self, name, email, employee_id, department):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department
        self.membership = Membership("Teacher")
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.membership.borrow_limit:
            print(f"❌ {self.name} has reached the borrowing limit ({self.membership.borrow_limit}).")
            return
        if book.copies_available > 0:
            book.copies_available -= 1
            self.borrowed_books.append(book)
            print(f"✅ {self.name} borrowed {book.title}")
        else:
            print(f"❌ {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.copies_available += 1
            print(f"🔄 {self.name} returned {book.title}")
        else:
            print(f"❌ {self.name} does not have {book.title} borrowed.")

    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"📚 {self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"ℹ️ {self.name} has no borrowed books.")


class Book:
    def __init__(self, title, author, isbn, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def show_info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Copies: {self.copies_available}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"📘 Added: {book.title}")

    def register_user(self, user):
        self.users.append(user)
        print(f"👤 Registered: {user.name}")

    def display_books(self):
        print("\n📚 Available Books in Library:")
        for book in self.books:
            print(book.show_info())
        print("-" * 40)


if __name__ == "__main__":
    library = Library()

    b1 = Book("Python Basics", "John Smith", "111", 2)
    b2 = Book("OOP in Depth", "Jane Doe", "222", 1)
    library.add_book(b1)
    library.add_book(b2)

    s1 = Student("Alice", "alice@example.com", "S123", "CS")
    t1 = Teacher("Dr. Bob", "bob@example.com", "T456", "Math")
    library.register_user(s1)
    library.register_user(t1)

    s1.borrow_book(b1)
    s1.borrow_book(b2)
    s1.view_borrowed_books()

    t1.borrow_book(b1)
    t1.borrow_book(b2)
    t1.view_borrowed_books()

    s1.return_book(b2)
    s1.view_borrowed_books()
    library.display_books()
