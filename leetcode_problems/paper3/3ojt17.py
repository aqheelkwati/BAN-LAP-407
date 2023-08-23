# 17.Write a function that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list. For example:
# >>> tail([1, 2, 3, 4, 5], 3)

# [3, 4, 5]
def sequence(l,n):
    s=len(l)-n #5-3=2
    op=[]
    for i in range(s,len(l)):
        op.append(l[i])
    return op
print(sequence([1, 2, 3, 4, 5], 3))
print(sequence('abcdefgh',4))