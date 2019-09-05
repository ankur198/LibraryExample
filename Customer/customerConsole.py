from Customer.coreCustomer import coreCustomer


class customerConsole(coreCustomer):
    def rentBook(self, bookName):
        if super().rentBook(bookName)==False:
            print("Book not available")
        else:
            print(f"{self._coreCustomer__name} got {bookName}")