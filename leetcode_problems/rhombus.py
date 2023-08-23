n=int(input('enter any number:'))
x=''
s=n-1
for i in range(1,n+1):
    for j in range(s):
        print(' ',end='')
    s=s-1
    
    if x=='':
        x+=str(i)
        # print(' '*(n-i))
        print(x)
    else:
        x=x+str(i)
        x=str(i)+x
        print(x)
s=1
for i in range(n-1):
    for j in range(s):
        print(' ',end='')
    s=s+1
    x=x[1:-1]
    print(x)