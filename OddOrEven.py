'''
Write a Python program to find whether a given number is even or odd,
print out an appropriate message to the user.

'''
n=int(input("Enter a number : "))
while n<=0:
    n=int(input("Enter a number above zero : "))
    if n>0:
        break
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")
