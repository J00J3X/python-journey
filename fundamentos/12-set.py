booksSet = {"player one", "House of dragons",
             "The witcher", "Percy Jackson"}

print(type(booksSet))

# 1 - Get set length
print(len(booksSet))

# 2 - True and 1 are considered the same value
exampleSet = {"The witcher", True, 1, 9.3}
print(exampleSet)

# 3 - add one item from another set
booksSet.update(exampleSet)
print(booksSet)

# 4 - Remove one item from set
booksSet.remove(True)
booksSet.remove(9.3)
print(booksSet)