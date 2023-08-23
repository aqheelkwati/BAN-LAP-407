#     *
#    *-*
#   *___*
#  *_____*

n=3
for i in range(n+1):
    print((n-i)*' ',end='')
    print('*', end='')
    print('_'*i,end='')
    print("_"*(i-1),end='')
    if i:
        print("*",end='')
    print()

# ______OR________
n=3
s=n
u=1
for i in range(n+1):
    for j in range(s):
        print(' ',end='')
    s-=1
    if not i:
        print('*',end='')
    else:
        print('*',end='')
        print('_'*u,end='')
        print('*',end='')
        u+=2
    print()     