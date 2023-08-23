# 8. Write a function in Python that accepts a credit card number. It should return a string 
# where all the characters are hidden with an asterisk except the last four. For eg., 
# if the credit card no. is “4509876278910046”, then function should return“************0046”. 

cn='4509876278910046'

def creditnumber(s):
    op=''
    for i in range(len(s)-4):
        op+='*'
    return  op+s[len(s)-4:]
    
print(cn)
print(creditnumber(cn))

#.................OR............
print(('*'*(len(cn)-4))+cn[-4:])