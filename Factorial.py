'''
Write a Python program to get the Factorial number of given number.
'''
n=int(input("Enter a number : "))
product=1
for i in range(n,0,-1):
    product=product*i
print("The factorial of number ",n," is ",product)
