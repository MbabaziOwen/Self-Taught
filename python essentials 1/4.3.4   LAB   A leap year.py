"""
our task is to write and test a function which takes one argument (a year) 
and returns True if the year is a leap year, or False otherwise.
"""
#start
def isleapyear(year):
    if  (year%4 ==0 and year%100 != 0)or(year%400 == 0) :
        return True
    else:
        return False
    
print(isleapyear(int(input("enter a year: "))))    