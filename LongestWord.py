'''
 Write a Python function that takes a list of words and returns the length
of the longest one.

'''
n=int(input("Enter number of words you want to enter : "))
words=[]
line=""
for i in range(n):
    line=input("Enter word ")
    words.append(line)
count=0
ans=""
for i in words:
    if count<=len(i):
        count=len(i)
        ans=i
    else:
        continue
print("The length of longest word is : ",count)
