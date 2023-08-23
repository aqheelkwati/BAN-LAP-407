# You have given a string str1 = "abcbaefabcabchijkl"
# your task is to find the combination of given word without repetition, present in the string , given 
# word 'abc'
# o/p = 7
# explaination :
# abc, cba,
# cba,
# bca, acb
# cab, bac
str1 = "abcbaefabcabchijkl"
word ='abc'
n=len(word)
count=0
for i in range(len(str1)-n):
    x=str1[i:i+n]
    # print(x,word,end=' ')
    # print(all([c for c in list(x)if c in word]))
    
    # if 'a'in x and 'b' in x and 'c' in x:
    # if sorted(word)==sorted(x):
    if all(c in x for c in word):
        # print(str1[i:i+n])
        count+=1
print(count)

