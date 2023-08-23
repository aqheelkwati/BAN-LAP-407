l1=['siya','priya','jiya']
l2=[170,120,130]

def sort_by_height(l1,l2):
    for i in range(len(l2)-1):
        for j in range(len(l2)-1):
            if l2[j]>l2[j+1]:
                l2[j],l2[j+1]=l2[j+1],l2[j]  
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1
print(sort_by_height(l1,l2))

# print('x0a'.digit())
a='msys'
b='msys'
print(a is b)
print(a == b)