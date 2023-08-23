# 16.Write a function split_in_half that splits a list in half and returns both halves.
# >>> split_in_half([1, 2, 3, 4])
# ([1, 2], [3, 4])

def split_in_half(l):
    mid=len(l)//2

    return (l[:mid],l[mid:])

print(split_in_half([1, 2, 3, 4,]))
