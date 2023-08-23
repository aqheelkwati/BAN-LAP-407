# 18.Write sample code for reproducing the below errors and print the user defined messages with the use of exception handling concept

# •IndexError,TypeError,AttributeError,ValueError
a=[1,2,3]
try:
    x='hello'
    y=x[1]              
    # y=x[10]           #index error
    # y+=1              #type error
    # print(int('a'))   #value error
    # print(a.upper())     # attributeerror
except IndexError as e:
    print('index error')
except TypeError as e:
    print("It is a type error")
except ValueError as e:
    print(" wrong value is given for typecasting")
except AttributeError as e:
    print("it is an attribute error")
else:
    print(y)
finally:
    print("Done")