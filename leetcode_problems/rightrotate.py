l=[10,20,30,40,50,60,70]
n=int(input())
for i in range(n):
    x=l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
    
    l[-1]=x
print(l)