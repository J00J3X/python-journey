# 1 - Function to print a message
def welcome():
    print("Welcome to the library system!")

# for i in range(10):
#    welcome()
# 2 - Function to calculate rate average
def calculate_average():
    num_ratings = int(input("How many ratings do you want to make:\n"))
    total = 0
    for i in range(num_ratings):
        rate = float(input("Write the film rate:\n"))
        total += rate

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    return average

print(f"The rate average is: {calculate_average():.2f}")

# 3 - Function to register a book:
def create_book():
    title       = input("Write the book title:\n")
    yearLaunch  = int(input("Write the book year launch:\n"))
    bookPrice   = float(input("Write the book price:\n"))
    rating      = float(input("Write the book rate:\n"))
    print(f"{title} ({yearLaunch}) - $$ {bookPrice:.2f}")

create_book()
create_book()