# 1 - Listing values from 0 to 10 that are smaller than 4
listNumbers = [i for i in range(10)]
print(listNumbers)

# Book list
bookList = ["Game of Thrones", "The witcher", "Banana diary", "Percy Jackson"]

# 2 - books that have letter 'e' in the title
booksWithE = [book for book in bookList if 'e' in book.lower()]
print(booksWithE)

# 3 - Books that I read
booksReaded = [book for book in bookList if book != "Percy Jackson"]
print(booksReaded)

# 4 - Finding a book through the title
while True:
    searchTitle = input("Wirite the book title to search in the list(or leave to end):\n")
    if searchTitle.lower() == "leave":
        print("Program interrupted")
        break

    foundBooks = [book for book in bookList if searchTitle.lower() in book.lower()]
    if foundBooks:
        print(f"Book(s) founded with the title: {searchTitle}")
        for foundBook in foundBooks:
            print(foundBook)
    else:
        print(f"Any book was found with the title {searchTitle}. Try again")