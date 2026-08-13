booksList = ["player one", "House of dragons",
             "The witcher", "Percy Jackson"]

# 1 - List length
print(len(booksList))

# 2 - Retrieve one item by index
print(booksList.index("House of dragons"))

# 3 - Append one item at the end
booksList.append("Prince of Persia")
print(booksList)

# 4 - Sort list
booksList.sort()
print(booksList)

# 5 - Copy items from one list to another
booksCopy = booksList.copy()
booksCopy.remove("The witcher")
print(booksCopy)

# 6 - Remove every item from the list
booksList.clear()
print(booksList)