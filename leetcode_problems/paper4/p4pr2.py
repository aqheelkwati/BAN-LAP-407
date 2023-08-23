# 2. Define a function which returns a list contains only the palindrome strings from the list
# of provided string elements
# input : List of strings
# output : List of palindrome strings
s=['hello','hannah','kayak','rotator','deed','hi','clear','wow']
def palindromes(s):
    l=[]
    for i in s:
        if i==i[::-1]:
            l.append(i)
    return l
print(palindromes(s))
print([word for word in s if word==word[::-1]])