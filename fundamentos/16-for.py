# Book list
bookList = ["Game of Thrones", "The witcher", "Banana diary", "Percy Jackson"]

# 1 - Iterating through the list items with for
for book in bookList:
    print(book)

# 2 - As the condition is met, the loop will break
for book in bookList:
    if book == "Banana diary":
        break
    print(book)

# 3 - As the condition is met, the loop will go to the next itineration
for book in bookList:
    if book == "The witcher":
        continue
    print(book)

# 4 - Book rate:
bookTitle = input("Write book title:\n")
bookRate = int(input("How many ratings do you want to make? "))

total = 0
for i in range(bookRate):
    rate = float(input("Write the book rate:\n"))
    total += rate

if bookRate > 0:
    average = total / bookRate
else:
    average = 0

print(f"Average rate of the book {bookTitle} is: {average:.2f}")