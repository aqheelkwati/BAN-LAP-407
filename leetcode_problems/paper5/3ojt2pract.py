# 2.Write a decorator function that will record the number of times a function is called. Your 
# decorator function should be called record_calls and call_count attribute that keeps track of 
# the number of times it was called.
def record_calls(func):
    def wrapper(*args, **kwargs):
        print(args,kwargs)
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper
@record_calls
def my_function(x, y):
    return x + y

print(my_function(1, 2))  # Output: 3
print(my_function(2, 3))  # Output: 5
print(my_function.call_count)  # Output: 2
