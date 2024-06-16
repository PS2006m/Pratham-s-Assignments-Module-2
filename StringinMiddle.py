'''
Write a Python function to insert a string in the middle of a string
'''
string=input("Enter String 1 : ")
middle=input("Enter String to be entered in middle : ")
string=string[:int(len(string)/2)]+middle+string[int(len(string)/2):]
print("After inserting in middle of String is ",string)
