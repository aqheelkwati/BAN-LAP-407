n=int(input())

s=n-1
for i in range(1,n+1,2):
    for j in range(s):
        print(' ',end='')
    s=s-1
    for j in range(i): 
        print('a',end='')
    print()