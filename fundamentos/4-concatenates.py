bookTitle   = input("Write book title:\n")
yearLaunch  = int(input("Write the launch year of the book:\n"))
bookRate    = float(input("Write the book rate:\n"))

print("Book Data")
print("===================")
# Option 1
#print("Book title:",bookTitle)
#print("Year Launch:",yearLaunch)
#print("Book Rate",bookRate)

# Option 2
print("Book title:", bookTitle, "\nYear Launch:", yearLaunch, "\nBook Rate:", bookRate)

# Option 3
print(f"Book title: {bookTitle}\n"
      f"Year Launch: {yearLaunch}\n"
      f"Book Rate: {bookRate}\n"
    )