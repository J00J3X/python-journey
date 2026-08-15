# Function to calculate the power of a number
power = lambda num:num **2

# Function to verify if the num is pair
is_even = lambda x:x % 2 == 0

# Function to div
div_num = lambda x, y: x/y

# Function to invert a string
reverse_string = lambda s: s[::-1]

print(power(3))
print(power(4))
print(is_even(3))
print(is_even(30))
print(div_num(10, 2))
print(reverse_string("Banana"))

# Funcstions related to the library
bookList = ["Game of Thrones", "The witcher", "Banana diary", "Percy Jackson"]
ratings = {
    "Game of Thrones": [9.9, 8.9, 9.6],
    "Game of Bones": [8.9, 3.9, 1.6],
    "Game of Tones": [7.9, 4.9, 6.6],
    "Game of Gomes": [6.9, 5.9, 8.6],
}

# Function to calculate the average rate of a book
average_rating = lambda book_title: sum(ratings[book_title] / len(ratings[book_title]))
 
print(f"Average rate of Game of Tones: {average_rating("Game of Tones")}")
