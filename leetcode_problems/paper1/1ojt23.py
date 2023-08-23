# 23. Find the highest sum of the string by removing the duplicates for each iteration 
input='1211123'
# input=''
sum=0
if input:
    sum=int(input[0])
for i in range(1,len(input)):
    if input[i]==input[i-1]:
        continue
    else:
        sum+=int(input[i])
print(sum)

# or
# def highest_sum(string):
#     prev_char = ''
#     sum = 0
#     for char in string:
#         if char == prev_char:
#             continue
#         else:
#             sum += int(char)
#             prev_char = char
#     return sum
# print(highest_sum(input))