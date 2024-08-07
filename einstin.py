#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main ():
    #Calculates the fuckin energyyyy
    m = int(input("what is the weight bro?"))
    c = 300000000
    emc2 = m*c**2
    print(f"the amount of energy according to albert einstain is {emc2}")

main()
