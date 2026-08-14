# Book info
# title       = input("Write the book title:\n")
# yearLaunch  = int(input("Write the year launch:\n"))
# rating      = float(input("Write the book rate:\n"))

# Verify if the book is recommended
# if rating > 8.0 and yearLaunch > 2015:
#     print(f"The book {title} is very good. Recommended to watch")
# else:
#     print(f"The book {title} doesn't have a good rate yet")

value1 = float(input("Write the first value:\n"))
value2 = float(input("Write the second value:\n"))
operation = input("Write an operation to do: (+ - * /)\n")

if      operation == "+":
        result = value1 + value2
elif    operation == "-":
        result = value1 - value2
elif    operation == "*":
        result = value1 * value2
elif    operation == "/":
        if value2 != 0:
                result = value1 / value2
        else:
            print("Error")
            result = 0
else:
        print("Invalid operator")
        result = 0

print(result)