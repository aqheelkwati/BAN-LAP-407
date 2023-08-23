# 22. Print the following rhombus pattern . eg. If input is 4, 
# it should print the following output .
#    1
#   2 2
#  3 3 3
# 4 4 4 4
#  3 3 3
#   2 2
#    1

n=4
spaces=n-1
for i in range(1,n+1):
    for j in range(spaces):
        print(' ',end='')
    spaces-=1
    for j in range(i):
        print(i,end=' ')
    print()

spaces=1
for i in range(n-1,0,-1):
    for j in range(spaces):
        print(" ",end='')
    spaces+=1
    for j in range(i):
        print(i,end=' ')
    print()