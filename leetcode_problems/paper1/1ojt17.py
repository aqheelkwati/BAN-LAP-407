#  Write a program to find the count of alphabet alone in the given alphanumeric string for
# Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c38d2b2c1a11’
# Ex2: input = ‘abc23’ output=’a1b1c123’

input='abb24ccc8ddbbca1'
# input='abc23'
op=''
x=''
for i in range(len(input)):
    if not input[i].isalpha():
        op=op+input[i]
    else:
        x=x+input[i]
        if input[i] != input[i+1]:
            op=op+input[i]+str(len(x))
            x=''
print(op)


# op=''
# occurance=0
# for i in range(len(input)):
#     if not input[i].isalpha():
#         op=op+input[i]
#     else:
        
#         occurance+=1
#         if input[i] != input[i+1]:
#             op=op+input[i]+str(occurance)
#             occurance=0
# print(op)
