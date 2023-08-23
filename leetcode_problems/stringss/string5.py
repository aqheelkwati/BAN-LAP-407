#P5. Write a program to print characters at the odd position and even position for a given string
# s1 = "MSys Technologies Software Company"

s1 = "MSys Technologies Software Company"
def oddchar(s):
    print("printing odd positioned(not index) characters")
    for i in range(0,len(s),2):
        print(s[i],end=' ')
    print()
def evenchar(s):
    print("printing even positioned(not index) characters")
    for i in range(1,len(s),2):
        print(s[i],end=' ')
oddchar(s1)
evenchar(s1)