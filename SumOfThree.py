'''
Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.
'''
n1=int(input("Enter number 1 :  "))
n2=int(input("Enter number 2 : "))
n3=int(input("Enter number 3 : "))
sum=n1+n2+n3
if n1==n2 or n1==n3 or n2==n3:
    print("Sum is 0 as two of the three numbers are equal")
else:
    print("Sum is ",sum)
    
