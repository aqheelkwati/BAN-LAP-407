# 2.Write a decorator function that will record the number of times a function is called. Your 
# decorator function should be called record_calls and call_count attribute that keeps track of 
# the number of times it was called.
def record_calls(func):
    
    def wrapper(x,y):
        wrapper.call_count+=1
        return f'The addition of given numbers is {func(x,y)}'
    wrapper.call_count=0
    return wrapper
@record_calls
def add(x,y):
    return x+y

print(add(2,3))
print(add(2,3))
print(add(2,3))
print(add(2,3))
print(add.call_count)