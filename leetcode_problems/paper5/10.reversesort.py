# 10. Sort the list of integers in descending order without using inbuilt functions .
l = [56,2,13,1,78,4,6]

#bubble sort
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print(l)