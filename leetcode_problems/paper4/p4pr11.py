# 11.Define Calculator logic in such a way that addition and subtraction functions should be in 
# one python file and multiplication and division should be in another python file, 
# Access these functions and utilize them inside the main file.
from add_sub import *
from mul_div import * 
v1=int(input('val 1:'))
v2=int(input('val 2:'))
op=input('operator:')
if op=='+':
    print(addition(v1,v2))
elif op=='-':
    print(substraction(v1,v2))
elif op=='*':
    print(multiplication(v1,v2))
else:
    print(division(v1,v2))

