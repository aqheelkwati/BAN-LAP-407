'''Q13. Give a real time example for multithreading. Is it a good idea to use multi-thread to
speed your Python code?'''


# 21. How do you open a file of large size, say around 10GB? So that program should not 
# Crash

# 22. Write a function where month and year are taken as arguments which returns the output 
# with all the dates of saturdays occuring the month
def list_of_saturday(month,year):
    num_days = calendar.monthrange(year, month)[1]
    saturday = []
    for day in range(1,num_days+1):
        weekday = calendar.weekday(year, month, day)

        if weekday == 5:
            saturday.append(day)
    return saturday

list = list_of_saturday(1,2023)
# print(list)

# 24. Write a python script to copy files from a directory D1 based on timestamp(current_date) 
# to another directory D2 and delete the source directory D1. Whenever the script is called 
# this program must run. 


# 25. Write a program to send a mail notification to customers regarding the arrival of goods 
# on a daily basis. The admin email has a separate domain email address owned by your 
# company.Do not forget to add cc candidates in customer’s mail. 

# 28. Write a Python program to remove the parenthesis area in a string using Regular 
# Expression 
# Sample data : ["example (.com)", "MSys", "github (.com)", "keka (.com)"] 
# Expected Output: 
# Example 
# MSys 
# github 
# Keka

# 29. Write a regular expression to find the html tags that are more than 4 letters. 
# Note: Html tags can be found inside <> characters and closing html tags can be found in 
# the same format after / character. </> 
# i.e.: <param> </param> 

# 30. How does the context manager work in python? Explain the internal methods. Write a 
# custom sample context manager.