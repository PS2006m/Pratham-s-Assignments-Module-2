'''
Write a Python program to count the occurrences of each word in a
given sentence
'''
line=input("Enter a String : ")
char=""
for i in line:
    char=char+i
    if char.count(i)>1:
        continue
    print("Frequency of ",i," is ",line.count(i))
