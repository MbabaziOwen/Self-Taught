#this program is to print all possible passwords of a given system that uses a 4 digit code 

#accessing numbers 0-9
from string import digits

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i,j,k,l)