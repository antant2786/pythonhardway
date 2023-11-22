# this imports the argv module from sys
from sys import argv

# this is setting the name of variables you need to include when running the script
script, filename = argv

# this is setting a variale for "txt" and using it to open "filename"
txt = open(filename)

# 
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
