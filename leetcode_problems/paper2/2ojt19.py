# Write a function which takes input string from the user as argument and the character also taken 
# by the user as the argument and remove all the occurences of that character from the string. 
# Also if the given character is not present in the string your function should raise the 
# exception stating that “Given character is not present in the string. Please try with a new one”
class NotPrsent(Exception):
    pass
s=input("Write any string: ")
c=input('Give a character present in that list: ')

# try:
#     op=''
#     if c.lower() not in s.lower():
#         raise NotPrsent
#     for char in s:
#         if char.lower()==c.lower():
#             continue
#         else:
#             op+=char
#     print(op)
try:
    if c.lower() not in s.lower():
        raise NotPrsent
    op=''.join(x for x in s if c!=x )
    print(op)

except NotPrsent as e:
    # print(e)
    print('Given character is not present in the string. Please try with a new one')