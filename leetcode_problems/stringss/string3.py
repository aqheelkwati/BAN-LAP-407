#P3. Write a program to perform the following task?
# input2 = "One two three four five six seven"
#output2 = "One owt three ruof five xis seven"

input = "One two three four five six seven"
l=input.split(' ')
for i in range(1,len(l),2):
    l[i]=l[i][::-1]
op=' '.join(l)
print(op)