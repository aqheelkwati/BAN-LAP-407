# 27. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid
# but "[)", "({[)]" and "{{{" are invalid
input=["()", "()[]{}", "[)", "({[)]" ,"{{{" ,'(()]]}']
paren={')':'(','}':'{',']':'['}

def parentheses(x):
    l=[]    #({[()]})
    for i in x:
        if i not in paren:
            l.append(i)
        else:
            if l and paren[i]==l[-1]:
                l.pop()
            else:
                return False
    # print(l)
    if not l :
        return True
    else:
        return False

# Testing each input.....................
for i in input:
    print(i,parentheses(i))
    print()