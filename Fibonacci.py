'''
 Write a Python program to get the Fibonacci series of given range.
'''
n=int(input("Enter range : "))
a,b=0,1
print(a,end=" ")
for i in range(n):
    print(b,end=" ")
    a,b=b,a+b
    
