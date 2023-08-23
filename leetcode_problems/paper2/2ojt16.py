# Write a function which will take a string argument and reverse the words in the string. For 
# example – Input string -- “Hello World”. Output should be “olleH dlroW”.

# def reverse(s):
#     return s[::-1]

# reverse= lambda x:x[::-1]
# print(reverse('Hello World'))
def reverse(s):
    s=s.split()
    for i in range(len(s)):
        s[i]=s[i][::-1]
    print(' '.join(s))
reverse('Hello World')