#start
#function
def BMI(height,weight):
    bmi = weight/(height^2)
    print("your body mass index is: ",bmi)

#user input 
Height = int(input("Height in Meters: "))
Weight = int(input("Enter weight in kilograms: "))

BMI(Height,Weight)