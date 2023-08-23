# •Below logic is failing with an error message, Instead of auto generated Error, Please display
# the user defined message saying “Error : Cannot concatenate String and Number”
# print(“msys” + 2007)
try:
    # print('msys')
    print("msys"+2007)
except TypeError as e:
    print('Cant concatinate a string with an integer')
else:
    pass
finally:
    print("Done")