'''
Write a python program to sum of the first n positive integers.
'''
n=int(input("Enter a number : "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("Sum is ",sum)
