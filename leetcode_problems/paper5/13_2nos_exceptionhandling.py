# 13. Write a python program to take 2 inputs(numbers) from user. Divide the greater
# number by the smaller number. Validate the user inputs, it should be integer type
# only . If the input is not integer, raise exception and catch it. Also, if divisor is 0, catch
# the exception raised. 

def twonos():
    
    try:
        x=int(input())
        y=int(input())
        mx=max(x,y)
        mn=min(x,y)
        ans=mx/mn
    except ValueError as e:
        print("input should be of integer type only... ")
    except ZeroDivisionError as e:
        print("Cannot devide anything by zero")
    else:
        print(ans)
while 1:
    twonos()