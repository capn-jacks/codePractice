#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) 
# converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
# All other text should be returned unchanged.Then, in that same file, implement a function called main that prompts the user for input, 
# calls convert on that input, and prints the result.


def convert(orginal_txt):
    """ converts :) into an emoji"""
    return orginal_txt.replace(":)", "🙂",).replace(":(", "🙁")


def main(): 
    orginal_txt = input("are you feeling :) or :(")
    new_txt = convert(orginal_txt)
    print(new_txt)

main()
