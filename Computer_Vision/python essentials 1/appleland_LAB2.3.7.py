"""Here is a short story:

Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:

    create the variables: john, mary, and adam;
    assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
    having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
    now create a new variable named total_apples equal to the addition of the three previous variables.
    print the value stored in total_apples to the console;
    experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
"""
#start
#assign number of apples
john,mary,adam = 3,5,6

#printing the all in a line
print("john =",john,"apples, mary =",mary,"apples, adam =",adam,"apples")

#variable for total applest
total_apples = john+mary+adam
print(total_apples,"apples")


