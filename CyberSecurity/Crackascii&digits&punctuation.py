#this program is to print all possible passwords of a given system that uses a 4 letter  code (ASCII) and letters and punctuations  
#number of iterations are 94^4
#accessing numbers 0-9
from string import ascii_letters, digits, punctuation

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i,j,k,l)