#P8. Write a program to perform the following activity
# s = "a4k3b2"
#output = "aeknbd"
s = "a4k3b2"
op=''
for i in range(0,len(s)-1,2):
    op=op+s[i]+ chr(ord(s[i])+int(s[i+1]))

print(op)