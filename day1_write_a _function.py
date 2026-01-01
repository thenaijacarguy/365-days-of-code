# Question: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# I tried a number of iterations but i couldnt pass all 6 test cases so i checked the internet and it turned out i got some brackets and logic incorrectly.

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
   
year = int(input())
print(is_leap(year))
