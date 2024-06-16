'''
Write a Python function to reverses a string if its length is a multiple of
4.
'''
string=input("Enter a String : ")
line=string
if len(string)%4==0:
    line=string[::-1]
print(line)
