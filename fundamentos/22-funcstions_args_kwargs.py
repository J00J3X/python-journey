"""
    *args - We use it when we don't know how many arguments a function will receive
    - The arguments are passed as a tuple
    **kwargs - Beside the values, we could pass the respective key for each argument too.
    - The arguments are like a dictionary
"""

# 1 - Sum of numbers
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"The sum is: {sum_total}")

sum(7)
sum(20,20,20,7)

# 2 - Courses apresentation
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Courses list:")
presentation(name="Python", category="Backend", level="Beginner")
presentation(name="C#", category="IA", level="Intermediate")
presentation(name=".NET", category="MVC", level="Expert")