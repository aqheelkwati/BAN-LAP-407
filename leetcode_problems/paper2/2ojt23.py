# create 2 dictionaries as follows:
# dict1 = {'name': 'Msys', 'Place': 'Pune'}
# dict2 = {'EmpID': 0001, 'Salary': 50000}
# Perform following operations:
# a. create single dictionary by merging dict1 & dict2
# b. update the salary to 10%
# c. update age to 35
# d. extract & print all the values & keys separetly in tuple.
# e. delete the element with key 'Age' & print the dictionary elements.
dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': '0001', 'Salary': 50000}

# print({**dict1,**dict2})

#---------or-------------------------
# for i in dict2.keys():
#     dict1[i]=dict2[i]
# print(dict1)

#--------------or--------------------
dict1.update(dict2)
print(dict1)
# b. update the salary to 10%
dict1['Salary']=int(dict1['Salary']*1.1)
print(dict1)
# c. update age to 35
dict1.update({'age':35})
print(dict1)
# d. extract & print all the values & keys separetly in tuple.
print(tuple(dict1.keys()))
print(tuple(dict1.values()))
# e. delete the element with key 'Age' & print the dictionary elements.
x=dict1.popitem()
print(x,dict1.values())
x=dict1.popitem()















#x=dict(dict1.items() | dict2.items())