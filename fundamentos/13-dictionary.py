bookTheWitcher = {
    "title": "The Wticher",
    "yearLaunch": 1998,
    "imbRating": 8.8,
    "genre": ["Medieval", "Fantasy", "Romance"]
}
print(bookTheWitcher)
print(len(bookTheWitcher))
print(type(bookTheWitcher))

# 1 - Recovery one item from dictionary
print(bookTheWitcher["genre"])
print(bookTheWitcher.get("imbRating"))

# 2 - Get just dictionary keys
print(bookTheWitcher.keys())

# 3 - Get just dictionary values
print(bookTheWitcher.values())

# 4 - Get dictionary itens with key and value
print(bookTheWitcher.items())

# 5 - Add items in dictionary
bookTheWitcher["author"] = "George R. Martim"
print(bookTheWitcher)

# 6 - Update dictionary items
bookTheWitcher.update({"imbRating": 9.1})
print(bookTheWitcher)

# 7 - Remove items from dictionary
bookTheWitcher.pop("author")
print(bookTheWitcher)