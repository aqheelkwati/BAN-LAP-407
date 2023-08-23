# import math
import schedule

def pattern():
    print(
    '''********** 
******** 
****** 
***''')

schedule.every(2).hours.do(pattern)

while 1:
    schedule.run_pending()