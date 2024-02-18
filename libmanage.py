class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.file = open("books.txt", "a+")
        self.file.seek(0)
        self.file.truncate()

    def __del__(self):
        self.file.close()

    def add_book(self, bookName, author, releaseDate, numberOfPages):
        self.file.write(bookName + "," + author + "," + releaseDate + "," + numberOfPages + "\n")
        self.file.flush()

    def list_books(self):
        print("------------LMS------------")
        print(f"Books in {self.name}:")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            books = line.split(",")
            print(books[0] + " - " + books[1])
        print("\n")

    def remove_book(self, bookName):
        index = -1
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for i, line in enumerate(lines):
            books = line.split(",")
            if books[0] == bookName:
                index = i
        if index == -1:
            print("There is no book in the library with this title\n")
            newBookName = input("Could you give another title: ")
            self.remove_book(newBookName)
        else:
            del lines[index]
            self.file.seek(0)
            self.file.truncate()
            for line in lines:
                self.file.write(line + "\n")
        print("The book you give is deleted successfully. The updated book list is:")
        self.list_books()


def main():
    print("Hi, this is an application for library management. Can you give a name for this library?")
    libName = input("Library name: ")
    lib = Library(libName)
    isContinue = True
    while isContinue:
        print("***MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Exit\n")
        num = input("What would you like to do?")
        try:
            num = int(num)
        except:
            print("Give an integer value between 1-4\n")
            continue

        if num < 1 or num > 4:
            print("Give an integer value between 1-4\n")
        else:
            if num == 1:
                lib.list_books()
            elif num == 2:
                bookName = input("Can you enter the book title: ")
                author = input("Can you enter the author: ")
                releaseDate = input("Can you enter the first release year: ")
                numberOfPages = input("Can you enter the number of pages: ")
                lib.add_book(bookName, author, releaseDate, numberOfPages)
            elif num == 3:
                bookName = input("Can you enter the title of the book you want to remove: ")
                lib.remove_book(bookName)
            else:
                isContinue = False
    
    print("Thank you for your contribution. Have a good day:))")
    return

if __name__ == "__main__":
    main()

