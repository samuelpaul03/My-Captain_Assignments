#Python program to accept a filename from the user and print the extension

fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])