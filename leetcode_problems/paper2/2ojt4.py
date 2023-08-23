# In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out
# all the keys in a list named as ‘list_keys’ and list out all the values in a list named as 
# ‘list_values’.Also find out the value of key ‘Australia’ in the list and as it is not 
# existing in the list print ‘NA’ as its value.
C={'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'}
list_keys=list(C.keys())
list_values=list(C.values())
print(list_keys,'\n',list_values)

val=C.get('Australia','NA')
print(val)
print(C.get('hello')) # prints None (default)
