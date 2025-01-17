'''What is a ValueError?
A ValueError is a built-in exception in Python.
It is raised when a function receives an argument of the correct type but an inappropriate value.
'''
'''What Does raise Do?
The raise keyword is used to manually trigger an exception.
When raise is encountered, Python stops the execution of the current code block and looks for an exception handler (try-except).
Example:
raise ValueError("This is a custom error message!")'''

# Example: ValueError
# Define a function to validate the input string

def validate_input(string):
    """Validate if the input string is in uppercase."""
    if string != string.upper():
        raise ValueError(f"Input '{string}' is not in uppercase. Please use all capital letters.")

def discount(c, d):
    """Check for discount code in the first three characters."""
    code = "DIS"
    if (c[:3] == code) or (d[:3] == code):
        print("Discount")
    else:
        print("No Discount")

# Input handling with validation
try:
    a = input("Enter first string: ")
    validate_input(a)  # Validate input for uppercase
    
    b = input("Enter second string: ")
    validate_input(b)  # Validate input for uppercase
    
    discount(a, b)  # Check for discount
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)

