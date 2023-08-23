# Write Python program to perform left rotation of array elements by two positions.
a=[1,2,3,4,5]
# print(a[2:]+a[:2])
# OR
for i in range(2):
    x=a[0]
    for i in range(len(a)-1):
        a[i]=a[i+1]
    a[-1]=x
print(a)
