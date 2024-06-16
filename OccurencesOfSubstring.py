'''
Write a Python program to count occurrences of a substring in a string
'''
line=input("Enter a String : ")
subline=input("Enter a Substring that is within the String : ")
frequency=line.count(subline)
print("Occurence of ",subline," is ",frequency)
