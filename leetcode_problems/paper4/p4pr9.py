# 9 Given a string “abcde”, Display the output as “a1b2c3d4e5”
# x='abcde'
# def func(x):
#     y=''
#     for i in range(len(x)):
#         y+=x[i]+str(i+1)
#     print(y)

# func(x)

string = input("Enter the string : ").lower()


val = ord('a')


res = ""
for char in string:
    res += char+str((ord(char)%val)+1)
 
print(res)