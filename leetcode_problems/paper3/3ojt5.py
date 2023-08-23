# 5.Write a function that accepts an iterable and returns a new iterable with all items from the
#  original iterable except for duplicates.
# Ex. uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
# [1, 2, 3]
l=[1, 2, 2, 1, 1, 3, 2, 1]
t=(1, 2, 2, 1, 1, 3, 2, 1)
s={1, 2, 2, 1, 1, 3, 2, 1}
def unique_only(i):
    originaltype=type(i)
    i=set(i) # to remove duplicate
    i=originaltype(i)     # to convert it back to its original type
    return(i)
print(unique_only(l))
print(unique_only(t))
print(unique_only(s))
