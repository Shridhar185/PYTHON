
import csv 
def addBooks(books):
    n = int(input("Enter the number of books: "))
    for i in range(n):
        bno = int(input("Enter book no: "))
        title = input("Enter Title: ")
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        books.append([bno, title, author, price])
    with open("books.csv", "w", newline='') as file:  #the "w" mode will override the contexts in files...remove old values in a file  
        writeObj = csv.writer(file)                    # the "a" mode jsut add new values to the file
        writeObj.writerows(books)

def readData():
    print("The books are: ")
    with open("books.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for book in reader:
            print(book)

def Search_by_author():
    flag = 0
    au = input("Enter Author to search: ")
    with open("books.csv", newline='') as file:
        readerObj = csv.reader(file)
        for book in readerObj:
            if au == book[2]:
                flag = 1
                print("Book found with details:\n", book)
        if flag == 0:
            print("No book by the author", au)

def Search_by_price():
    flag = 0
    try:
        pr = float(input("Enter Price to search: "))
        if pr <= 0:
            raise ValueError("Price should be greater than zero.")
    except ValueError as e:
        print(e)
        return
    with open("books.csv", newline='') as file:
        readerObj = csv.reader(file)
        for book in readerObj:
            if pr >= float(book[3]):
                flag = 1
                print("Book found with details:\n", book)
        if flag == 0:
            print("No book below the price", pr)

def Search_by_word():
    flag = 0
    word = input("Enter word to search in book title: ")
    with open("books.csv", "r", newline='') as file:
        readerObj = csv.reader(file)
        for book in readerObj:
            if word in book[1]:
                flag = 1
                print("Book found with details:\n", book)
        if flag == 0:
            print("No book with title containing word", word)

def main():
    books = []
    addBooks(books)
    readData()
     
    while True:
        print("\n1.Search By Author\n2.Search By price\n3.Search By word\n4.Exit\n")
        opt = int(input("Enter your option: "))
        if opt == 1:
            Search_by_author()
        elif opt == 2:
            Search_by_price()
        elif opt == 3:
            Search_by_word()
        elif opt == 4:
            break
        else:
            print("Enter valid Choice!")

if __name__ == '__main__':
    main()



 














