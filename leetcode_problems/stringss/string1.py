#P1. Write a program to reverse the string
s = "MSys Technologies"

# s=s[::-1]
# print(s)
y=''
for i in range(len(s)-1,-1,-1):
    y=y+s[i]
print(y)