'''
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''
string=input("Enter a String : ")
i=string.find("notpoor")
print(i)
if i!=-1:
    string=string.replace("notpoor","good")
print(string)
