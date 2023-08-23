# 9. For the given sentence, return the average word length. sentence = "I need to work very 
# hard to learn more about algorithms in Python!" Note: Remember to remove punctuation first. 

sentence = "I need to work,,, very... hard to learn more about algorithms in Python!"

def average(s):
    ss=''
    avg=0
    for i in s:
        if i.isalpha() or i==' ':
            ss+=i
    # l=ss.split(' ')  #['I', 'need', 'to',.....] 
    # for i in l:
    #     avg+=len(i)
    # # print(sum(avg))
    # return avg//len(l)
    l=[len(x) for x in ss.split(' ')]
    return sum(l)//len(l)
print(average(sentence))

