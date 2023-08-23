# 26. You are given a string S. Your task is to find the indices of the start and end of string k in
# S The first line contains the string S.The second line contains the string k.
# Print the tuple in this format: (start _index, end _index). If no match is found, print (-1,
# -1).
# Sample Input Sample Output
# aaadaa
# aa
# (0, 1)
# (1, 2)
# (4, 5)
s='aaadaa'
k='aa'

def substring(s,k):
    size=len(k)                         
    l=[]
    for i in range(len(s)-size+1): #length-size+1 because we are slicing from given index to given+size index
        if k==s[i:i+size]:
            l.append((i,i+size-1))
            # print(s[i:i+size])
    return l
print(substring(s,k))