#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

variable = input("what is the answer to the answer of the whole wide undverse and everything?")

if variable in ["forty two", "42", "forty-two", "FORTY TWO"]:
    print("yes")
else:
    print("no")
