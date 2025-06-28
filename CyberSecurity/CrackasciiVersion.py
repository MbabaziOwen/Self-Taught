#this program is to print all possible passwords of a given system that uses a 4 letter  code (ASCII) 
#number of iterations are 52^4
#accessing numbers 0-9
from string import ascii_letters

for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                print(i,j,k,l)