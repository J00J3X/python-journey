# Book list
bookList = ["Game of Thrones", "The witcher", "Banana diary", "Percy Jackson"]

# 1 - Iterating through the list items with while 
index = 0;
while index < len(bookList):
    print(bookList[index])
    index += 1

# 2 - As the condition is met, the loop will end
while index < len(bookList):
    if bookList[index] == "The witcher":
        break
    print(bookList[index])
    index += 1

# 3 - As the condition is met, the loop will go to the next itineration
while index < len(bookList):
    if bookList[index] == "The witcher":
        index += 1
        continue
    print(bookList[index])
    index += 1

# 4 - Book rate with while
bookTitle   = input("Write book title:\n")
bookRate    = int(input("How many ratings do you want to make? "))

total = 0
count = 0

while count < bookRate:
    rate = float(input("Write the book rate:\n"))
    total += rate
    count += 1

if bookRate > 0:
    average = total / bookRate
else:
    average = 0

print(f"Average rate of the book {bookTitle} is: {average:.2f}")