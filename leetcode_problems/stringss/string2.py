
#P2. write a program to reverse the order of words:
#input1 = "Learning python is very easy"
#output = "easy very is python Learning"

input = "Learning python is very easy"
l=input.split(' ')
print(l)
l=l[::-1]
op=" ".join(l)
print(op)

# op=''
# x=' '
# for i in range(len(input)-1,-1,-1):
#     if input[i]==' ':
#         op=op+x[::-1]
#         x=' '
#     else:
#         x=x+input[i]
# print(op)