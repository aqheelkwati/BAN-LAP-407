# 13.Let’s assume there is function defined which expects only list as an argument, However there 
# is chance that sometimes function will be called with different type of data, Now Fix this 
# scenario to handle the other types without breaking the code
# Scenario 1: If the argument provided is a list then, Print inside the function as 
# “valid argument“
# Scenario 2: if the argument provided is a different data type, then Print a message saying 
# “ invalid argument,
#  You have provided data type (str/int) “
l=[]
s=''
t=()
d={}
def func(l):
    if type(l)==list :
        print("valid argument ")
    else:
        print(f'You have provided {type(l)}')
func(l)
func(t)
func(s)
func(d)