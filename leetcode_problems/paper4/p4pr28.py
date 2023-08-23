# Define the decorator function
def validate_division(func):
    def wrapper(num1, num2):
        # Check if the second argument is 0
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return None
        # If second argument is not 0, call the original function
        else:
            return func(num1, num2)
    return wrapper

# Define the division function and apply the decorator
@validate_division
def divide(num1, num2):
    return num1 / num2

# Test the function with different input arguments
print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))   # Output: Error: Cannot divide by zero! \n None