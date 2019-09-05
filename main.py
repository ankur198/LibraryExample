from Customer.customerConsole import customerConsole
from Library.library import library;

def main():
    shweta = customerConsole('Shweta')
    sumit = customerConsole('Sumit')
    prashant = customerConsole('Prashant')

    gnit = library()
    bookList = ["abc", 'abc', 'xyc', 'dsa']
    gnit.addBooks(bookList)
    gnit.addMultipleCustomers([shweta, sumit, prashant])

    # consoleWapper(shweta,"abc")
    # consoleWapper(sumit,"abc")
    # consoleWapper(prashant,"abc")

    shweta.rentBook("abc")
    sumit.rentBook("abc")
    prashant.rentBook("abc")

    iit = library()
    iit.addBooks(bookList)
    iit.addMultipleCustomers([shweta, sumit])

    shweta.rentBook("abc")
    sumit.rentBook("abc")
    prashant.rentBook("abc")


if __name__ == "__main__":
    main()
