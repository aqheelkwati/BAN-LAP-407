# Given an Integer n, count the total number of times 1 is appearing in all non-negative integers 
# less than or equal to n.
# Ex – n = 13, output should be 6
# method – 1 is coming 6 times starting from number 0 till 13 in ‘1’, ‘10’, ‘11’, ‘12’, ‘13’. 
# Also note 1 is coming 2 times in 11. That is why 6 is the output

def count_num(n):
    count=0
    for num in range(1,n+1):
        num=str(num) #12
        for digit in num:
            # print(digit)
            if int(digit)==1:
                count+=1
    print(count)

count_num(13)
count_num(1)
count_num(12)
count_num(11)
count_num(10)