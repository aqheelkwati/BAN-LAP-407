# 1.Write a program in which two strings are given and determine if they share a common 
# substring.A substring may be as small as one character. The function returns either 
# “YES” or “NO”.
# def substring(s1,s2):
#     for char in s1:
#         if char in s2:
#             return 'Yes'
#     return 'No'
# print(substring('hello','world'))
# print(substring('abc','def'))

# for a substring of least 2 character
# def substring(s1,s2):
#     for i in range(len(s1)-1):
#         for j in range(len(s2)-1):
#             # print (s1[i:i+2],s2[j:j+2])
#             if s1[i:i+2]==s2[j:j+2]:
#                 return True
#     return False
# print(substring('hello','world'))
# print(substring('abcd','cdef'))

def substring(s1,s2):
    for i in range(len(s1)-1) :
        if s1[i:i+2] in s2:
            return 'Yes'
    return 'No'
print(substring('hello','world'))
print(substring('abcd','cdef'))