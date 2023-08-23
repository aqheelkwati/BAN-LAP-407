# Write a program to multiply two given number without using “*” operation and any in built
# function

def multiply(x,y):
    total=0
    for i in range(abs(x)):
        total+=abs(y)
    if (x<0 and y>0) or (x>0 and y<0):
        print(-total)
    else:
        print(total)

multiply(-10,-2)
multiply(10,0)

