def bs(l,e):
    low=0
    high=len(l)-1
    
    while low<=high:
        mid=(low+high)//2
        if l[mid]==e:
            return l[mid],mid
        elif e<l[mid]:
            high=mid-1
        else:
            low=mid+1
arr = [2, 4, 6, 8, 10, 12, 14, 16]
element = 10
print(bs(arr,element))