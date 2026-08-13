booksTuple = ("player one", "House of dragons",
             "The witcher", "Percy Jackson")
print(type(booksTuple))

# 1 - Get the first two itens
print(booksTuple[:2])

# 2 - Get the last item
print(booksTuple[-1])

# 3 - Get itens up to a certain position
print(booksTuple[:3])

# 4 - Get items from a given position onward
print(booksTuple[2:])

# 5 - Recovery one item by the name
print(booksTuple.index("player one"))