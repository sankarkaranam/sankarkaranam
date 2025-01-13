global_function = "I am a global function"
def my_function(): # Function definition
    local_function = "I am a local function"
    print(local_function)
    print(global_function)

my_function() # Function call
# Output: I am a local function
print(global_function)
# Output: I am a local function
#         I am a global function

# Function with arguments
def greet(name):
    print("Hello, " + name + "!")
greet("John") # Output: Hello, John!

# Function with default arguments
def greet(name = "John"):
    print("Hello, " + name + "!")
greet() # Output: Hello, John!


# Function with return value
def add(a, b):
    return a + b
result = add(2, 3)
print(result) # Output: 5

# Function with multiple return values
def square_and_cube(x):
    return x*x, x*x*x
result = square_and_cube(3)
print(result) # Output: (9, 27)

# Function with variable number of arguments
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
result = add(1, 2, 3)
print(result) # Output: 6

# Function with variable number of keyword arguments
def print_student(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)
print_student(name = "John", age = "21", city = "New York")
# Output: name: John
#         age: 21
#         city: New York

# Function with variable number of arguments and keyword arguments
def print_student(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key + ": " + value)
print_student("John", "21", "New York", name = "John", age = "21", city = "New York")
# Output: John
#         21
#         New York
#         name: John
#         age: 21
#         city: New York

# Nested functions
def outer_function():
    print("Outer function")
    def inner_function():
        print("Inner function")
    inner_function()    
outer_function()
# Output: Outer function
#         Inner function

# Function as argument
def greet():
    return "Hello"
def call_func(func):
    print(func())
call_func(greet) # Output: Hello

# Function as return value
def outer_function():
    def inner_function():
        return "Inner function"
    return inner_function
func = outer_function()
print(func()) # Output: Inner function

# Lambda function
add = lambda a, b: a + b
result = add(2, 3)
print(result) # Output: 5

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
result = factorial(5)
print(result) # Output: 120

# Function annotations
def add(a: int, b: int) -> int:
    return a + b
result = add(2, 3)
print(result) # Output: 5
print(add.__annotations__) # Output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

# Function with docstring
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + "!")
greet("John")
print(greet.__doc__) # Output: This function greets to the person passed in as parameter

# Function with default arguments
def greet(name = "John"):
    print("Hello, " + name + "!")
greet() # Output: Hello, John!

# Function with keyword arguments
def greet(name):
    print("Hello, " + name + "!")
greet(name = "John") # Output: Hello, John!
