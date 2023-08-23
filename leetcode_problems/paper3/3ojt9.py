# leap year

def leap(y):
    if y%100!=0:
        if y%4==0:
            return 'leap year'
        else:
            return 'not a leap year'
    else:
        if y%400==0:
            return 'leap year'
        else:
            return 'not a leap year'
print(leap(2024))
print(leap(2028))
print(leap(2032))
print(leap(2036))
print(leap(1600))
print(leap(2000))
print('----------------not a leap year----------')
print(leap(2021))
print(leap(2022))
print(leap(2023))
print(leap(1900))