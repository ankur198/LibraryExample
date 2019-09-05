class library:
    def __init__(self, *args, **kwargs):
        self.__books = []
        self.__customer = []

    def addCustomer(self, customer):
        self.__customer.append(customer)
        customer.linkToLibrary(self)

    def addMultipleCustomers(self, customers):
        for customer in customers:
            self.addCustomer(customer)

    def removeCustomer(self, customer):
        if customer in self.customer:
            self.__customer.remove(customer)
            return True
        else:
            return False

    def haveBook(self, bookName):
        return bookName in self.__books

    def issueBook(self, bookName):
        if self.haveBook(bookName):
            index = self.__books.index(bookName)
            book = self.__books.pop(index)
            return book
        else:
            return None

    def getBook(self, bookName):
        self.__books.append(bookName)

    def getMultipleBooks(self, books):
        for book in books:
            self.getBook(book)
        books.clear()

    def addBooks(self, books):
        self.__books += books