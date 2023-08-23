# Write a Python program to remove the parenthesis area in a string using Regular
# Expression
# Sample data : ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
# Expected Output:
# Example
# MSys
# github
# keka
input= ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
# def func(s):
#     for i in s:
#         if '(' not in s:
#             print(s)
#             break
#         else:
#             index=s.index('(')
#             print(s[:index])
#             break
# for i in input:
#     func(i)
import re
for i in input:
    print(re.sub(r'\([\w.]+\)',' ',i))