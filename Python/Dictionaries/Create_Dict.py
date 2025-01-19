#create Dictionary

# Method 1
# Using dict() constructor
# Creating an empty dictionary
my_dict = dict()
print(my_dict) # Output: {}

# Creating a dictionary with key-value pairs
my_dict = dict({1: 'apple', 2: 'ball'})
print(my_dict)  # Output: {1: 'apple', 2: 'ball'}

# Creating a dictionary with keyword arguments
my_dict = dict(a='apple', b='ball')
print(my_dict)  # Output: {'a': 'apple', 'b': 'ball'}

# Method 2
# Using curly braces {}
# Creating an empty dictionary
my_dict = {}
print(my_dict)  # Output: {}

# Creating a dictionary with key-value pairs
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)  # Output: {1: 'apple', 2: 'ball'}

# Creating a dictionary with keyword arguments
my_dict = {'a': 'apple', 'b': 'ball'}
print(my_dict)  # Output: {'a': 'apple', 'b': 'ball'}

# Method 3
# Using dict.fromkeys() method
# Creating an empty dictionary
my_dict = dict.fromkeys([])
print(my_dict)  # Output: {}

# Creating a dictionary with key-value pairs
my_dict = dict.fromkeys([1, 2], 'apple')
print(my_dict)  # Output: {1: 'apple', 2: 'apple'}

# Creating a dictionary with keyword arguments
my_dict = dict.fromkeys(['a', 'b'], 'apple')
print(my_dict)  # Output: {'a': 'apple', 'b': 'apple'}

# Method 4
# Using dict comprehension
# Creating an empty dictionary
my_dict = {k: None for k in []}
print(my_dict)  # Output: {}

# Creating a dictionary with key-value pairs
my_dict = {k: 'apple' for k in [1, 2]}
print(my_dict)  # Output: {1: 'apple', 2: 'apple'}

# Creating a dictionary with keyword arguments
my_dict = {k: 'apple' for k in ['a', 'b']}
print(my_dict)  # Output: {'a': 'apple', 'b': 'apple'}

# Method 5
# Using zip() function
# Creating an empty dictionary
my_dict = dict(zip([], []))
print(my_dict)  # Output: {}

# Creating a dictionary with key-value pairs
my_dict = dict(zip([1, 2], ['apple', 'ball']))  # Output: {1: 'apple', 2: 'ball'}
print(my_dict)  # Output: {1: 'apple', 2: 'ball'}   

# Creating a dictionary with keyword arguments
my_dict = dict(zip(['a', 'b'], ['apple', 'ball']))
print(my_dict)  # Output: {'a': 'apple', 'b': 'ball'}

# Method 6
# Using list comprehension
# Creating an empty dictionary
my_dict = {k: v for k, v in []}
print(my_dict)  # Output: {}

# Creating a dictionary with key-value pairs    
my_dict = {k: v for k, v in [(1, 'apple'), (2, 'ball')]}
print(my_dict)  # Output: {1: 'apple', 2: 'ball'}

# Creating a dictionary with keyword arguments
my_dict = {k: v for k, v in [('a', 'apple'), ('b', 'ball')]}
print(my_dict)  # Output: {'a': 'apple', 'b': 'ball'}

# Method 7
# Using a list of tuples

