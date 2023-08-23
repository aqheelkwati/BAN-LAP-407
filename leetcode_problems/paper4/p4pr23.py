# 23.Write a logic for calculating the time taken for executing the python function

import time
start=time.time()
x=0
for i in range (100):
    x+=1
    print(x)
end=time.time()
print(end-start)