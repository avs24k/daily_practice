"""1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero."""

# def myfun(n):
#     try:
#         A = 10/n
#         return A
#     except ZeroDivisionError as e:
#         return e
#
# print(myfun(0))

"""2. Write a Python program that prompts the user to input an integer and raises a ValueError exception
 if the input is not a valid integer."""

# def myfun(n):
#     try:
#         return int(n)
#     except ValueError as e:
#         return e
# print(myfun("avi"))

"""3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist."""

# def file_handle(path):
#     try:
#         with open('path', 'r') as readble:
#             A = readble.readlines()
#             print(A)
#     except FileNotFoundError as e:
#         print(e)
# file_handle("/hthhll")

"""4. Write a Python program that prompts the user to input two numbers 
and raises a TypeError exception if the inputs are not numerical."""

# def fun(n):
#     while True:
#         try:
#             value = int(input(n))
#             return value
#         except Exception as e:
#             return e
# print(fun("Enter Value: "))

"""5. Write a Python program that opens a file and handles a PermissionError exception 
if there is a permission issue."""

# def fun(path):
#     try:
#         with open(path,'w') as writable:
#             a = writable.read()
#             print(a)
#     except PermissionError as e:
#         print(e)
# fun('path.txt')

"""6. Write a Python program that executes an operation on a 
list and handles an IndexError exception if the index is out of range."""

# def myfun(n):
#     try:
#         for i in str(n):
#             return int(i[0]+i[8])
#     except IndexError as e:
#         return "error:",e
#
# print(myfun([1,2,3,4,4]))

"""7. Write a Python program that prompts the user to input a number and handles a 
KeyboardInterrupt exception if the user cancels the input."""

# Try to execute the following block of code, which may raise exceptions.

# Prompt the user to input a number and attempt to convert it to an integer, storing it in the 'n' variable.
# try:
#     n = int(input("Input a number: "))
#     # If the user input is successfully converted to an integer, print the entered number.
#     print("You entered:", n)
# # Handle the KeyboardInterrupt exception, which occurs when the user cancels the input (typically by pressing Ctrl+C).
# except KeyboardInterrupt:
#     print("Input canceled by the user.")

"""8. Write a Python program that executes division and handles an ArithmeticError exception 
if there is an arithmetic error."""

# try:
#     A = 10/0
#     print(A)
# except ArithmeticError as e:
#     print(e)

""""""