#### Cant reduce length of list
l=[1,4,7,2,9,5]
# def delete(l):
#     index=int(input())
#     if not 0<=index<=len(l):
#         print("Invalid index")
#     for i in range(index,len(l)-1):
#         l[i]=l[i+1]
    
# while 1:
#     delete(l)
#     print(l,len(l))

l=[1,4,7,2,9,5]
def delete(l):
    index=int(input())
    if not 0<=index<=len(l):
        print("Invalid index")
    for i in range(index,len(l)-1):
        l[i]=l[i+1]
    return (l[:-1])
print(delete(l))