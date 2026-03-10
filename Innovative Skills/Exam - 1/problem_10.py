class library:
    def __init__(self, available_books):
        self.available_books = set(available_books)
        self.borrowed_books = {}

    def borrow(self, student, book):
        if book in self.available_books:
            if student not in self.borrowed_books:
                self.borrowed_books[student] = []

            if book not in self.borrowed_books[student]:
                self.available_books.remove(book)
                self.borrowed_books[student].append(book)

    def return_book(self, student, book):
        if student in self.borrowed_books and book in self.borrowed_books[student]:
            self.borrowed_books[student].remove(book)
            self.available_books.add(book)
            if not self.borrowed_books[student]:
                del self.borrowed_books[student]


with open("Innovative Skills/Exam - 1/test10.txt") as file:
    content = file.readlines()

    number_of_books = content[0].strip()
    book_names = content[1].strip().split()
    operation_number = int(content[2].strip())

    my_library = library(book_names)

    for num in range(operation_number):
        student_data = content[3+num].strip().split()
        name = student_data[0]
        action = student_data[1]
        subject = student_data[2]

        if action == "borrow":
            my_library.borrow(name, subject)
        elif action == "return":
            my_library.return_book(name, subject)

    print(f"Available Books: {sorted(list(my_library.available_books))}")
    print("Borrow Records:")
    for student, books in my_library.borrowed_books.items():
        print(f"{student}: {books}")
