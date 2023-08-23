# 16.Let’s consider there are two files, one file contains testnames, other file contains testnames and status for each one. Generate dictionary with key’s as testname and value as status
# Input :

# FiIe1.txt:

# test1 test2
# File2.txt:

# test1-pass test2-fail
# Output :
# { "test1" : "pass", "test2" : ”fail”}

with open('file1.txt','r') as f1:
    testcase=f1.read().split()
print(testcase)
d={}
with open('file2.txt','r') as f2:
    l= f2.read().split()
    for line in l:
        # print(line.split('-'))
        test,status=line.split('-')
        if test in testcase:
            d[test]=status
print(d)


# print(type(testcase))
