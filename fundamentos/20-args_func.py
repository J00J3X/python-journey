# 1 - Function to print the full name
def full_name(firstName, lastName):
    print(f"The name is: {firstName} {lastName}")

full_name("Jackson", "Percy")
full_name("Bruno", "Mars")

# 2 - Function to sum two numbers
def sum_numbers(a, b):
    return a + b

print(f"The sum is: {sum_numbers(60, 7)}")

# 3 - Function with default parameter
def address(country="Brasil"):
    print(f"I live in: {country}")

address()
address("Portugal")

# 4 - Function to rate books
def rate_book(num_ratings, book_title):
    total = 0
    for i in range(num_ratings):
        rate = float(input("Write the book rate:\n"))
        total += rate

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    print(f"The average of the book {book_title} is {average:.2f}")

rate_book(2, "Game of Thrones")