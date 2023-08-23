# 1.what is the difference between list and tuple:
# Tuple:
# Tuple is an ordered immutable data type in which individual elements are separated by comma and enclosed inside parentheses.
# syntax---
# variable name=(e1,.....eN)
# t=(12,23,[12,34],(bye,12))

List:
list is a mutable order collection  data type in which individual elements are separated with comma and enclosed with a pair of square brackets.
We can store any type of data in a list.
example---
L=[1,2,3,4]

➨Between list and tuple,tuple is faster, because tuple is stored in a block of memory but list has a large memory, means list stored in two block of memory one is fixed size and another one is variable size for storing data that’s why list is slower than tuple.

2.Lambda Function():
These are the anonymous single line functions.
Syntax:
Lambda args: expression

Ex:
adding=lambda a:a+10
print(adding(90))


3.What is monkey patching and what is the use of monkey patch?
Monkey patching is used for modifying or updating a class or module at the runtime  in python code.
Monkey patching is the technique of dynamic modification of a piece of code at the run time. Actually by doing monkey patch we change the behavior of code but without affecting the original source code.

Example:
# new_monk.py  
class A:  
 def hello(self):  
      print (" The hello() function is being called")  

#main.py
import new_monk  
def monkey_f(self):  
   print ("monkey_f() is being called")  
new_monk.A.hello = monkey_f  
obj = new_monk.A()  
obj.hello() 


4. What is the importance of PEP rules 
 PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

Why is PEP important?
Naming conventions:
When we write the code, we need to assign names to many things such as variables, functions, classes, packages, and a lot more things. Selecting a proper name will save time and energy. When we look back to the file after some time, we can easily recall what a certain variable, function, or class represents. Developers should avoid choosing inappropriate names.

Code layout:
The code layout defines how much the code is readable. In this section, we will learn how to use whitespace to improve code readability.

Indentation:
Unlike other programming languages, the indentation is used to define the code block in Python. The indentations are the important part of the Python programming language and it determines the level of lines of code. Generally, we use the 4 spaces for indentation.

5.Can we order a dictionary? How? 
Yes, we can order a dictionary in Python, dictionaries are also used to maintain the insertion order of their items. This means that the order in which key-value pairs are added to the dictionary is preserved. 
Ex:# Define a dictionary     
dictionary = {'c': 2, 'a': 1, 'b': 3}     		    
orderd = dict(sorted(dictionary .items()))          
print(orderd) 		  	        
#output: {'a': 1, 'b': 3, 'c': 2}





6.write a python program to right rotate a list by n.
def rightRotate(lists, num):
	output_list = []
	for item in range(len(lists) - num, len(lists)):
		output_list.append(lists[item])
	for item in range(0, len(lists) - num):
		output_list.append(lists[item])

	return output_list
rotate_num = 3
list_1 = [10, 20, 30, 40, 50, 60,70]

print(rightRotate(list_1, rotate_num))

7.Difference between append and extend.
append():
It is used for adding the element in last,even though we pass collection data type it will consider the entire collection as a single line.
Ex:
L=[78,89]
L.append(100)--[78,89,100]

extend():
It is used for adding the element in the last list but it is adding only the collection data type.
L=[11,22]
L.extend([‘vicky’,’niki’])--[11,22,’vicky’,’niki’]

8. Create a dictionary where the key is an even number from the given list and the value 
will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2] 
input_= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
set_=set(input_)
list_1=[]
list_2=[]
for i in set_:
  c= input_.count(i)
  list_1.append(i)
  list_2.append(c)
z=zip(list_1,list_2)
print(dict(z))


9.Write a function swap_element that contains two args which will be the position of 
elements present in the list. The function must swap the elements present in those 
positions. 
Input: [1,2,3,4,5,6,7,8] function: swap_element(arg1, arg2) 

def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list
List =  [1,2,3,4,5,6,7,8] 
pos1, pos2 = 1, 4
print(swapPositions(List, pos1-1, pos2-1))


10. Write the output of the program: 
match = ‘version’, input=’Upgraded_image_version_8.0.4.3’ 
if match in input: 
print(‘YES’) 
else: 
print(‘NO’)

import re

match = 'version'

input1 ='Upgraded_image_version_8.0.4.3'

x = re.findall(match,input1)

if str(*x) == match:
    print("Yes")
else:
    print("No")
11.Rewrite the program to get proper output
Match = 'version'
input=8
print(Match+input)

Match = 'version'
input=8
print(Match+str(input))
#output–version8

12. How is memory management done in python?
Python memory manager is responsible for managing memory allocation and deallocation to various processes that are under execution in python.
Every python process has two types of memory allocated to it.
1.static memory 
2.heap memory

1.Static memory:
Whenever a new function or class is declared it is very common to have some variable declaration inside them, these declarations are associated with the function itself and do not change in the runtime. They occupy a fixed memory size. Hence these are stored in the stack area.
Python memory manager maintains a stack of such function blocks. When a function is called its function block is pushed onto this stack and on return, the same block is popped from the stack.
Example:
def function_name():
    var1 = 1
    var2 = []
    var3 = "abc"
   
Heap memory:
The second type of memory available in a program is called heap memory. The heap memory is separate from the static stack memory, as this memory can be dynamically requested and
released in runtime. 

Example:
number = int(input("Enter a number"))
array = [0] * number
# the variable 'array' is stored in heap memory


13. Give a real time example for multithreading. Is it a good idea to use multi-thread to 
speed your Python code? 
def addition(a,b):
    return a+b
if __name__=='__main__':
    print(addition(3,5))
    print(__name__)
Yes it is a good idea to use multi-thread to speed up your python code,but python doesn't allow multi-threading.
Multithreading is more than one thread running serially at the same time within the process with shared memory.

14. When do you use generators in python? Give an example 
Generator:
In creating a python generator, we use a function.
A generator in python makes use of the 'yield' keyword.
Python generator saves the states of the local variables every time 'yield' passes the loop in python.
A generator does not need a class in python.
Generators are less memory efficient compared to iterators.
Generators are useful when we want to produce a large sequence of values.
Example:
def hello():
    print("hello")
    yield 67,"hai"
    print("after 1st yield")
    yield 90
h2=hello()
print(h2)#hello
print(next(h2))#(67,'hai')
print(next(h2))#after 1st yield--90
print(next(h2))#error(stop iteration)



15.Give the scenarios, when you will get ‘ValueError’ 
import math
x = int(input('Please enter a positive number:\n'))
try:
    print(f'Square Root of {x} is {math.sqrt(x)}')
except ValueError as ve:
    print(f'You entered {x}, which is not a positive number.')

Python valueError is raised when a function receives  an argument of the correct type but is inappropriate.
We can use try-except block to handle valueError exceptions.


16. Write a program to multiply two given number without using “*” operation and any in built
function
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
multi=0
for i in range(0,n2):
    multi+=n1
print(multi)


17. Write a program to find the count of alphabet alone in the given alphanumeric string for
Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c3d2b2c1a11’
Ex2: input = ‘abc23’ output=’a1b1c123’
res = ""
string = input("Enter the string : ")
n = len(string)
i = 0
while i < n:
    char = string[i]
    if char.isdigit():
        res += char
        i += 1
    else:
        j = i+1
        count = 1
        while char == string[j]:
            count += 1
            j += 1
        res += char
        res += str(count)
        i = j
print(res)

18. Write a python program where for every two hours it prints the pattern without using
sleep function
**********
********
******
***
*
import time
n = 10
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    start_time = time.time()
    while time.time() - start_time < 7200:   # 2 hours * 3600 seconds per hour
        pass

19. Write a program using decorators to print the traffic signal messages
Expected output -
RED : STOP
YELLOW : SLOW DOWN
GREEN : GO
def traffic_signal_decorator(func):
    def wrapper():
        print("RED : STOP")
        func()
        print("YELLOW : SLOW DOWN")
        func()
        print("GREEN : GO")
    return wrapper
@traffic_signal_decorator
def traffic_signal():
    pass
traffic_signal()


20.Write a python program for sort the given below list based last character of each word 
names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit']

def sortSur(nameList):
	l2 = []
	for i in nameList:
		l2.append(i.split())
	nameList = []
	for i in sorted(l2, key=lambda x: x[-1]):
		nameList.append(' '.join(i))
	return nameList
nameList = ["Prabhu", "Rahul", "Arunesh", "Sonali", "Rakshit"]
print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))

21. How do you open a file of large size, say around 10GB? So that program should not
Crash
with open('large_file.txt', 'rb') as f:
    chunk_size = 1024 # read 1KB at a time
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break

22. Write a function where month and year are taken as arguments which returns the output
with all the dates of saturdays occuring the month


import calendar
def date_saturdays(month, year):		#creating a fun with r arg month & year
    saturdays = []				# an empty list is used to collect the dates.
    _, num_days = calendar.monthrange(year, month) #we have to pass 2 arg but we need only month here so to ignore another arg we use _,
    for day in range(1, num_days + 1):
        if calendar.weekday(year, month, day) == calendar.SATURDAY:
            saturdays.append(day)
    return saturdays


saturdays = date_saturdays(4, 2023)
print(saturdays)





23. Find the highest sum of the string by removing the duplicates for each iteration
input=’1211’
input_="1211"
c=" ".join(input_).split(" ")
a=0
store=[]
while a<len(c):
    access=sum(set(list(map(int,c[a:]))))
    store.append(access)
    a=a+1
print(max(store))

24. Write a python script to copy files from a directory D1 based on timestamp(current_date)
to another directory D2 and delete the source directory D1. Whenever the script is called
this program must run.   
import os
source = 'D:\D1'
destination = 'D:\D2'
files = os.listdir(source)
for file in files:
    source_path = os.path.join(source, file)
    destination_path = os.path.join(destination, file)
    os.rename(source_path, destination_path)
print(f'Source path is: {source_path}')
print(f'Destination path is: {destination_path}')

25. Write a program to send a mail notification to customers regarding the arrival of goods
on a daily basis. The admin email has a separate domain email address owned by your
company.Do not forget to add cc candidates in customer’s mail.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_from = 'vinz223665@gmail.com'
email_password = 'ugyltbuxtnpmzijl'
email_subject = 'Daily Goods Arrival Notification'
email_body = 'Hello,\n\nThis is to inform you that new goods have arrived in our store today.\n\nThank you for your continued patronage.\n\nBest regards,\nVinayak'
recipients = ['vishalhirandagi33@gmail.com']
# cc_recipients = ['rsrinivas@msystechnologies.com','meghumeghu3@gmail.com']
cc_recipients = ['vinayakhavannavar@msystechnologies.com','promod456@gmail.com']
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = ', '.join(recipients)
msg['Cc'] = ', '.join(cc_recipients)
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, email_password)


server.sendmail(email_from, recipients + cc_recipients, msg.as_string())
print('Email notification sent successfully!')
server.quit()

26. You are given a string S. Your task is to find the indices of the start and end of string k in S
The first line contains the string S.The second line contains the string k.
Print the tuple in this format: (start _index, end _index). If no match is found, print (-1,-1).
Sample Input 
aaadaa
 aa 
Sample Output 
(0, 1) 
(1, 2) 
(4, 5)
S = input("Enter string S: ")
k = input("Enter string k: ")
start_index = S.find(k)
if start_index == -1:
    print((-1, -1))
else:
    end_index = start_index + len(k) - 1
    print((start_index, end_index))
    while True:
        start_index = S.find(k, start_index + 1)
        if start_index == -1:
            break
        end_index = start_index + len(k) - 1
        print((start_index, end_index))







27. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("({}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("[)"))


28.Write a Python program to remove the parentheses area in a string using Regular
Expression
Sample data : ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
Expected Output:
Example
MSys
github
Keka

import re
items = ["example(.com)", "MSys", "github (.com)", "keka (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))

29. Write a regular expression to find the html tags that are more than 4 letters.
Note: Html tags can be found inside <> characters and closing html tags can be found in
the same format after / character. </>
i.e.: <param> </param>
import re
tag = input("enter the tag: ")
x = re.findall("<\w{5,}[^>]*>|<\/\w{5,}[^>]*>",tag)
print(x)






30. How does the context manager work in python? Explain the internal methods. Write a
custom sample context manager.
context manager:- a context manager is an object that defines a runtime context executing within the 'with' statement
suppose a block of code raises an exception or if it has a complex algorithm with multiple return paths, it becomes difficult to close a file in all the places. generally in other languages when working with files try, except, and finally are used to ensure that the file resource is closed after usage even if there is an exception. python provides an easy way to manage resources: context managers.
the with keyword is used when it gets evaluated it should result in an object that performs context managemen
with open('data.txt') as f:
     data = f.readlines()
     print(int(data[0])

internal methods
“__init__ method:” :  an object is created with filename and with mode when it is executed

“ __enter__ method :” :  enter method opens the file in write mode(setup operation) and returns a file object 

“ __exit__ method:” :  exit methods takes care of closing the file on exiting the with a block(teardown operation)






