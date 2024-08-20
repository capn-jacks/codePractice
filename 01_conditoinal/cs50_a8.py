#Basically create a calculator 

#asks the user to unput values to calculate 
expression = input("Enter an expression for me to calculate!(+,-,*,/)")

#the actually calculating shit
x,y,z = expression.split()

#converting the string into integers 
x = int(x)
z = int (z)

if y == "+":
    result = x+z
elif y == "-":
    result = x-z
elif y == "*":
    result = x*z
elif y == "/":
    result = x/z
else:
    print("enter a valid operation synmbol")

print("{:.1f}".format(result))