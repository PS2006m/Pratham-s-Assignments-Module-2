'''
Write a Python program to count the number of characters (character
frequency) in a string
'''
line=input("Enter a String : ")
char=input("Enter a character to search in String : ")
frequency=line.count(char)
print("Frequency of ",char," is ",frequency)
