#start
#function
def triangle(a,b,c):
    if a+b > c or b+c > a or a+c > b:
        print("real triangle")
    else:
        print("not real triangle")

#user input
side_A = int(input("enter values for side A: "))
side_B = int(input("enter values for side B: "))
side_C = int(input("enter values for side C: "))

triangle(side_A,side_B,side_C)