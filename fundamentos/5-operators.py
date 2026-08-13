value1 = int(input("Type the first number:\n"))
value2 = int(input("Type the second number:\n"))

# Arithmetical
sum     = value1 + value2
sub     = value1 - value2
div     = value2 / value1
mult    = value1 * value2
mod     = value1 % value2
exp     = value1 ** value2

print(f"Power of number {value1} in {value2} is: {exp}")
print(f"Remainder of {value1} in {value2} is: {mod}")

# Comparation
bigger          = value1 > value2
smaller         = value1 < value2
equal           = value1 == value2
different       = value1 != value2 
bigger_equal    = value1 >= value2
smaller_equal   = value1 <= value2

print(f"The values {value1} and {value2} are equal? {equal}")
print(f"The value {value1} is bigger or equal to {value2}? {bigger_equal}")

# Atribuition
value1 += 1 # value1 = value1 + 1
value1 -= 1 # value1 = value1 - 1
value1 *= 1 # value1 = value1 * 1
value1 /= 1 # value1 = value1 / 1
