
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"You start reading '{self.title}' by {self.author}.")

    def info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")


class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size_mb}MB)...")

    def info(self):
        print(
            f"'{self.title}' (E-Book) by {self.author}, {self.pages} pages, {self.file_size_mb}MB.")


class Vehicle:
    def move(self):
        print("The vehicle moves.")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 328)
    ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 2.5)

    book1.read()
    book1.info()
    ebook1.download()
    ebook1.info()

    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
