#P7. write a program for the following requirement:
# s1 = "a4b3c2"
#output = "aaaabbbcc"

s1 = "a4b3c2"
op=''
for i in range(0,len(s1)-1,2):
    op=op+(s1[i]*int(s1[i+1]))
print(op)