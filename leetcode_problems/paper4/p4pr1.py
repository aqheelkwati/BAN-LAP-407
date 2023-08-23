# 1. Sort the below list without using inbuilt function
# I = [2,3,-5,-7,9,4,6,-1,-8,0]
l=[2,3,-5,-7,9,4,6,-1,-8,0]
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j+1]<l[j]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)