import pprint

booksDict = {
    "The Witcher":{
        "title": "The Wticher",
        "yearLaunch": 1998,
        "imbRating": 8.8,
        "genre": ["Medieval", "Fantasy", "Romance"]
    },
    "Game of Thrones":{
        "title": "Game of Thrones",
        "yearLaunch": 1958,
        "imbRating": 9.8,
        "genre": ["Medieval", "Dark-Fantasy", "Romance"]
    },
     "Percy Jackson":{
            "title": "Percy Jackson",
            "yearLaunch": 2000,
            "imbRating": 9.2,
            "genre": ["Medieval", "Hero-Fantasy", "Mitologic"]
        },
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(booksDict)


# 1 - Get info inside a nested dictionary
print(booksDict["Game of Thrones"]["genre"])

# 2 - Add new item
booksDict["Game of Thrones"]["author"] = "Jonathan KRefta"
print(booksDict["Game of Thrones"])

# 3 - Delte dictionary
del booksDict["Game of Thrones"]
pp.pprint(booksDict)