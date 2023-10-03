"""1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included)."""
import random

#
# A = []
# for i in range(1500,2700):
#     if (i%7==0) and (i%5==0):
#         A.append(i)
#
# print(A)

"""3. Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again 
until the guess is correct, on successful guess,
 user will get a "Well guessed!" message, and the program will exit."""


# random_number = random.randint(1, 10)
#
# while True:
#     A = int(input("Enter a num:"))
#
#     if random_number == A:
#         print("well guessed!")
#         break
#     else:
#         print("randon number is", random_number)
#         print("try again")

"""4. Write a Python program to construct the following pattern, using a nested for loop.
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


# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()
# for k in range(5,0,-1):
#     for l in range(k):
#        print("*",end="")
#     print()

"""5. Write a Python program that accepts a word from the user and reverses it."""
# A = input("Enter a word:")
# print(A[::-1])
# B = ''
# for i in A:
#     B = i + B
# print(B)

"""6. Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even = 0
# odd = 0
#
# for i in numbers:
#     if i%2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even)
# print(odd)

"""7. Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]"""

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
#
# A = [type(i) for i in datalist]
# print(A)

"""8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5"""

# for i in range(0,6):
#     if i == 6 or i == 3:
#         continue
#     print(i)

"""9. Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34"""

# x, y = 0, 1
#
# while y < 50:
#     print(y)
#     x, y = y, x + y

"""10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of 
the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz"""

