'''
Write a Python program to test whether a passed letter is a vowel or
not.
'''
n=input("Enter a character : ")
if n.startswith("a") or n.startswith("e") or n.startswith("i") or n.startswith("o") or n.startswith("u"):
    print("The character is a vowel")
else:
    print("The character is not a vowel")
