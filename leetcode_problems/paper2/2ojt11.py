# Write a python function with name reverse_vowel that takes one string as an argument and
# reverse the order of vowels present in the string. The function should return the string having
# reversed order of vowels. For example – If the input string which is given as argument is‘Hello’
# then the output string should be ‘Holle’. You need to reverse the vowel irrespective of lowercase or
# # uppercase.
# def reverse_vowel(s):
#     l=[]
#     op=''
#     for char in s:
#         if char in 'aeiouAEIOU':
#             l.append(char)
#     l=l[::-1]
#     # 1st for loop can be avoided by [char for char in s if char in 'aeiouAEIOU']
#     i=0
#     for char in s:
#         if char in 'aeiouAEIOU':
#             op+=l[i]
#             i+=1
#         else:
#             op+=char
#     print(op)
# reverse_vowel('hello')
# reverse_vowel('hEllo')
# reverse_vowel('aeiouAEIOU')

x='hello'
l=0
r=len(x)-1
x=list(x)
print(x)
while l<r:
    if x[l] not in 'aeiouAEIOU':
        print(x[l])
        l+=1  
        continue
    if x[r] not in 'aeiouAEIOU':
        print(x[l])
        r-=1
        continue
    
    x[l],x[r]=x[r],x[l]
    l+=1
    r-=1
print(''.join(x))