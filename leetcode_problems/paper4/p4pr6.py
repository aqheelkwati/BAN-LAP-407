
# 6.Define the logic for generating the email id based on username and department Get the username and department as a input and create a email id from it
# input :
# username : msys department: automation
# output:
# msys.automation@gmaiI.com
# Note : Generated email id should contain @ and should end with .com
username=input('username: ')
department=input('department: ')
def gmailgen(u,d):
    s='@gmail.com'
    return u+'.'+d+s
print(gmailgen(username,department))