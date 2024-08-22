#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ...

user_input = input("you are on fent. you will start slwoing down your words and tlaking very slowly. I have just administered the fent. what is your message to the world?")

#this is where the magic happens 
new_txt = user_input.replace(" ", "...")

print(new_txt)