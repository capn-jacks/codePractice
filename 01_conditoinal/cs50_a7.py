#In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

#prompt the user to enter the file name and type
file = input("enter file name: ").lower().strip()

#Determine the type of the the file names. 
if file.endswith(".gif"):
    print("image/.gif")
elif file.endswith(".jpg"):
    print("image/.jpg")
elif file.endswith(".jpeg"):
    print("image/.jpeg")
elif file.endswith(".png"):
    print("image/.png")
elif file.endswith(".pdf"):
    print("application/.pdf")
elif file.endswith(".txt"):
    print("text/plain")
else: 
    print("application/octet-stream")
    
