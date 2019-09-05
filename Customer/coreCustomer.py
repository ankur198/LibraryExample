class coreCustomer:
    def __init__(self, name):
        self.__name = name
        self.__books = []
        self.__library = None

    def linkToLibrary(self, library):
        if self.__library:

            if len(self.__books) > 0:
                self.__library.getMultipleBooks(self.books)
                # self.__books.append(self.__library.__books.pop())  choriii

            self.__library.removeCustomer(self)

        self.library = library

    def rentBook(self, bookName):
        book = self.library.issueBook(bookName)
        if book:
            self.__books.append(book)
            return True
        else:
            return False