from decorator import my_decorator, uppercase_decorator, split_string

@my_decorator
def my_function():
    print("Inside function")

my_function()

@uppercase_decorator
def text():
    return "HEllo World"

print(text())

@split_string
@uppercase_decorator
def example():
    return "Learning python and creating decorators"

print(example())