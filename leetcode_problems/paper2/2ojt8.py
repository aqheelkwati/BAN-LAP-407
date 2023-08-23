# 8. Take the input marks from user using input() function and find out the grade of the students.
#  Note the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, 
#  (70-61) – B2, (60-51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure  
# user should input the marks in the range 0<=marks<=100, if user will input some other marks in 
# should print invalid marks.
marks=int(input('Enter marks: '))
if marks>100 or marks<0:
    print('Invalid marks')
else:
    if marks >=91:
        print('Your garde is A1')
    elif marks >=81:
        print('Your garde is A2')
    elif marks >=71:
        print('Your garde is B1')
    elif marks >=61:
        print('Your garde is B2')
    elif marks >=51:
        print('Your garde is C1')
    elif marks >=40:
        print('Your garde is C2')
    else:
        print('You have failed ')