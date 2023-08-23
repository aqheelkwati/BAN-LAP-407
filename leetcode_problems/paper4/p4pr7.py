# 7 In the given string, remove the special characters 
# and add a space instead of that “Msys&Technologies@Chennai*
import re
x="Msys&Technologies@@@@@9Chennai*"
op=re.sub(r'[^a-zA-Z0-9]',' ',x)
# op=re.sub('[^a-zA-Z0-9]+',' ',x)
print(op)
#............or.................
import re
def remove_special_characters(string):
    res = re.sub(r"\W", " ", string)
    return res
# string = input("Enter the string : ")
print(remove_special_characters(x))

print(re.sub(r'[\W\d]+',' ',x))
#..................or.........
# y=''
# for char in x:
#    if char.isalpha():
#     y+=char
#    else:
#     y+=' '
# print(y)
