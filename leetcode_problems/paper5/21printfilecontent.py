# 21. Write a program that takes one or more filenames as arguments and prints all
# the lines which are longer than 40 characters. Note :Use generator to solve this
# question. 

def filename(*arg):
    for i in arg:
        f=open(f"{i}",'r')
        x=f.readlines()
        f.close()
        for j in x:
            if len(j)>40:
                print('from',i)
                print(j)
filename('f1.txt','f2.txt','f3.txt')