"""1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
 between 1500 and 2700 (both included)."""

# A=[]
#
# for i in range(1500,2700):
#     if (i%7==0) and (i%5==0):
#         A.append(i)
# print(A)

"""Write a Python program to generate a list of numbers
 between 100 and 500 (both included) that are multiples of 6."""
# A=[]
# for i in range(100,500):
#     if i%6==0:
#         A.append(i)
# print(A)

"""Write a Python program to find the sum of all the even numbers between 50 and 100.
"""

# A = 0
#
# for i in range(50,100):
#     if i%3==0:
#         A+=i
# print(A)

"""Write a Python program to generate a list of the squares of numbers between 1 and 10.
"""
# A = []
# for i in range(1,10):
#     C = i**2
#     A.append(C)
# print(A)

"""Write a Python program to find the greatest common divisor (GCD) of two 
numbers using the Euclidean algorithm."""
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# num1 = 48
# num2 = 18
# print(gcd(num1, num2))

"""Factorial calculation"""
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# number = 5
# print(factorial(number))

"""check Palidrome
i/p - "racecar,,,,o/p- "racecar"""

# s = "racecar"
# print(s[::-1])

"""count vowels"""
# A= "AUIEOauioe"
# B = 0
#
# for i in "Avinash":
#     if i in A:
#         B+=1
# print(B)

"""3. Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the
guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit."""

# while True:
#
#     if int(input("enter:")) == 8:
#         print("well guessed!")
#     else:
#         print("try again")

"""Question: Write a Python program that generates a random secret word from a predefined list of words.
 The user needs to guess the secret word. If the user's guess is incorrect, they are prompted to 
 guess again until they guess the correct word.On a successful guess, the program should display a 
 "Congratulations!" message and then exit."""

# A = ["avi","roshni","vicky","roshan"]
#
# while True:
#     if input("Enter a name:") in A:
#         print("Congratulations")
#         break
#     else:
#         print("Try Again")

"""4. Write a Python program to construct the following pattern, using a nested for loop.
o/p -
*  
* *  
* * *  
* * * *  
* * * * *  
* * * *  
* * *  
* *  
* 
 """

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

"""5. Write a Python program that accepts a word from the user and reverses it.
"""
# A = input("enter:")
# print(A[::-1])

"""6. Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Number_of_even_numbers = 0
# Number_of_odd_numbers = 0
#
# for i in numbers:
#     if i%2==0:
#         Number_of_even_numbers += 1
#     else:
#         Number_of_odd_numbers +=1
#
# print("Number_of_even_numbers:",Number_of_even_numbers)
# print("Number_of_odd_numbers:",Number_of_odd_numbers)

"""8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5"""

# for i in range(0,9):
#     if (i==6) or (i==3):
#         continue
#     print(i)

"""9. Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34"""

# x,y=0,1
#
# while y< 50:
#     print(y)
#     x,y = y,y+x


