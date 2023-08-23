# Write a program to replace duplicate adjacent alphabets from given string with ‘_’.
# For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’
s='abcdaaa hssbbye'
# op=''
# pre=''
# for char in s:
#     if char==pre:
#         op+='_'
#     else:
#         op+=char
#         pre=char
# print(op)

#----------or------
s='abcdaaa hssbbye'
op=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        op+='_'
    else:
        op+=s[i]
print(op)
