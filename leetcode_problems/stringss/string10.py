#P10. program to merge characters of 2 strings into single string by taking characters alternatively
#input:
# s1 = "ravi"
# s2 = "teja"
#output = "rtaevjia"
s1 = "ravi"
s2 = "teja"
s3=''
i,j=0,0
while i<len(s1) and j<len(s2):
    s3=s3+s1[i]+s2[j]
    i+=1
    j+=1
s3=s3+ s1[i:] # To add remaining characters of s1(if any) to s3 
s3=s3+ s2[j:] # To add remaining characters of s2(if any) to s3
print(s3)