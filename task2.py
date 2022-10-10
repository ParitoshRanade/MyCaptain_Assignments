"""
The input of the program should be a filename along with its extension and the output will be the extension.
"""

file_name = input("Input the Filename : ")
ext = file_name.split(".")
print("The extension of the file is ", ext[1])
