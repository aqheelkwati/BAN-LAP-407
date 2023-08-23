# Need to find minimum number of new chair purchase for work area with simulated set of array 
# values.
# C - A new employee comes to work area and new chair need to purchase
# R - Employee from work area goes to meeting room and free up the chair
# U - Employee comes from meeting room and occupy the chair
# L - Leaves the work area and free up the chair
# Input :
# n = 3
# simulated value : ['CCRLU', 'CRLCUC', 'CCCC']
# Output:
# 2
# 2
# 4
def new_chair(s):
    new=0
    available=0
    for i in s: #'CCRLU'
        # print(i)
        if i=='U' or i=='C':
            # print(new,available)
            if available>0:
                available-=1
            else:
                new+=1
        else:
            available+=1
        # print(new,available)
    print(new)

    
l=['CCRLU', 'CRLCUC', 'CCCC']
# new_chair('CCRLU')
for i in l:
    new_chair(i)