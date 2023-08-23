#P11. Write a program to find the number of occurances of each character present in the given string:
# input1 = "ABCABCABBCDE"
#output = A-3, B-4, C-3, D-1, E-1

input = "ABCABCABBCDE"
x=''
for i in input:
    if i not in x:
        x+=i
        print(f"{i} - {input.count(i)}",end=", ")
