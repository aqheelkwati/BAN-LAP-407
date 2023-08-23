# Write a method number_of_prime_numbers() which takes two input arguments num1 and
# num2 and should return the total number of prime numbers in the range. The numbers num1 and
# num2 are inclusive of the range. Also add all the numbers in an empty list and return the sum 
# of the list. So finally your function will return two things, first will be the count of prime 
# numbers and the other will be the sum of all the prime numbers in the given range.

def num_of_prime_numbers(x,y):
    l=[]
    for num in range(x,y+1):
        if num>1:
            for j in range(2,int(num**0.5)+1):
                if num%j==0:
                    break
            else:
                l.append(num)
    return len(l),sum(l)
print(num_of_prime_numbers(10,50))