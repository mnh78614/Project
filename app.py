#Create a calculator that asks the user for two numbers

m = "multiplication"
d = "division"
a = "addition"
s = "subtraction"


#function for multiplication
def multiplication():
    num1 = input("Okay, enter a number: ")
    num2 = input("Okay enter another number: ")
    print(float(num1) * float(num2))


#function for division
def division():
    num1 = input("Okay, enter a number: ")
    num2 = input("Okay enter another number: ")
    print(float(num1) / float(num2))

#function for addition
def addition ():
    num1 = input("Okay, enter a number: ")
    num2 = input("Okay enter another number: ")
    print(float(num1) + float(num2))

#fuction for subtraction
def subtraction ():
    num1 = input("Okay, enter a number: ")
    num2 = input("Okay enter another number: ")
    print(float(num1) - float(num2))

mathType = input("What kind of math do you want to do? [m], [d], [a], or [s]?")

if mathType == "m":
    multiplication()
elif mathType == "d":
    division()
elif mathType == "a":
    addition()
else:
    subtraction()


