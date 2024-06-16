'''
Write python program that swap two number with temp variable and
without temp variable.
'''
print("Using Temp variable")
a=int(input("Enter variable A : "))
b=int(input("Enter variable B : "))
print("A is ",a," B is ",b)
print("After swapping")
temp=a
a=b
b=temp
print("A is ",a," B is ",b)
print("--------------------------------")
print("Without Temp variable")
a=int(input("Enter variale A : "))
b=int(input("Enter variable B : "))
a=a+b
b=a-b
a=a-b
print("After swapping")
print("A is ",a," B is ",b)
