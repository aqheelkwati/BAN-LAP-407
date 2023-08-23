# delete element at given index of an array

def delete_ele(arr,index):
    if index < 0 or index >= len(arr):
        print("Invalid Index")
    # TO shift each element to its left
    for i in range(index,len(arr)-1):
        arr[i]=arr[i+1]
    #[0,1,3,4,5,5]

    arr.pop()
    return arr
l=[0,1,2,3,4,5]
print(delete_ele(l,2))