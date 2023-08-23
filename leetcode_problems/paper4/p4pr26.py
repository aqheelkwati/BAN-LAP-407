#    26.Print the pattern Pattern for the input : 3
#   *1 
#   21*
#   *123
n=int(input('enter a number:'))
x='*'
for i in range(1,n+1):
    x+=str(i)
    if i%2 != 0:
        print(x)
    else:
        print(x[::-1])
