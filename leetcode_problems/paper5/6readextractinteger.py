# 6. Read a given file and extract the integers from each line, concatenate all the
# integers present in the same line and print the sum of all these integers. eg: <File content>
# He is 32 yrs old and his son is 7 yrs old . She is 27 yrs old and her daughter is 2 yrs old . 
# Output : 599 ## calculation : Integers on Line 1 + Line 2 = 327 + 272 = 599
f=open('f1.txt','r')
l=f.readlines()
ans=0
for i in l:
    x=''
    for j in i:
        if j.isnumeric():
            x+=j
    ans+=int(x)
f.close()
print(ans)

