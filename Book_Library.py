class BooksLibrary:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_books = {}
        print(f'Wel Come to {self.library_name}')

    def show_book(self):
        print(f"We have following books in our {self.library_name}")
        for book in self.book_list:
            print(book.capitalize())

    def add_book(self, book_name):
        book_name = book_name.lower()
        self.book_list.append(book_name)
        print('Book is added!')

    def lend_book(self, book_name, user_name):
        book_name = book_name.lower()
        if book_name not in self.lend_books.keys():
            if book_name in self.book_list:
                self.lend_books[book_name] = user_name
                print(f'Your lended book "{book_name.capitalize()}"')
            else:
                print(f'This book "{book_name}" is not Available in our Library')
        else:
            print(f'Book has already taken by {(self.lend_books[book_name]).capitalize()} Please chose another book')

    def return_book(self, book_name, user_name):
        if book_name in self.lend_books.keys():
            del self.lend_books[book_name]
            print('Book Returned')
        else:
            print('This is Not our Book')

if __name__ == '__main__':
    l1 = BooksLibrary(['python', 'c++', 'java', 'django'], 'SubodhLibrary')
    
    while True:
        print('1. Show Books')
        print('2. Add a Book')
        print('3. Lend a Book')
        print('4. Return Book')
        print('5. Exit')

        choice = input('Chose : ')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                l1.show_book()
            elif choice == 2:
                book = input('Enter Book Name : ')
                l1.add_book(book)
            elif choice == 3:
                user = input('Enter Your name : ')
                book = input('Enter Book Name : ')
                l1.lend_book(book, user)
            elif choice == 4:
                user = input('Enter Your name : ')
                book = input('Enter Book Name : ')
                l1.return_book(book, user)
            elif choice == 5:
                print('Thanks for Visiting our Library, Please Visit Again')
                break
            else:
                print('Invalid input')
                continue
        else:
            print('Only Number Allowed!')