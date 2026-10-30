
import sys

if len(sys.argv) > 1:
    string = sys.argv[1]
else:
    string = input("Enter a string: ")

if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
