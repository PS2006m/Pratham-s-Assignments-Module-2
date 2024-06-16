'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string
'''
str1=input("Enter String 1 : ")
str2=input("Enter String 2 : ")
if len(str1)<2 or len(str2)<2:
    print("Both strings must have at least two characters.")
else:
    line1=str2[:1]+str1[1:]
    line2=str1[:1]+str2[1:]
    combined_string=line1+" "+line2
    print(combined_string)  
