# 5. Can we order a dictionary? How?

# Yes, it is possible to order a dictionary in Python based on its keys or values.

# To order a dictionary by keys, you can use the sorted() function with the items()
# method of the dictionary as follows:
my_dict = {'a': 3, 'c': 1, 'b': 2}
x=dict(sorted(my_dict.items()))
print(x)    # {'a': 3, 'b': 2, 'c': 1}

#To order a dictionary by values, you can use the sorted() function with a lambda 
# function that specifies the value to be sorted on:
y=dict(sorted(my_dict.items(), key=lambda x : x[1]))
print(y)    #{'c': 1, 'b': 2, 'a': 3}
y=dict(sorted(my_dict.items(), key=lambda x : x[1],reverse=1))
print(x.values())
print(y)
print(min(max(False,2,1),True)) 