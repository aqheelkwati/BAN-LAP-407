# Given a list --
# list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
# use the filter() function to find the list of numbers that are multiple of either 2 or 5.
list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
x=filter(lambda x:x%2==0 or x%5==0,list_1)
print(list(x))