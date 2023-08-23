#P9. Write a program to remove duplicate elements from a given string:
# s = "ABCDABBCDABBBCCCDDEEEF"
#out = "ABCDEF"
s = "ABCDABBCDABBBCCCDDEEEF"
op=''
for i in s:
    if i in op:
        continue
    op=op+i
print(op)
