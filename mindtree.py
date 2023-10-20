"""1. Write a Python program to calculate the length of a string.
"""
# A = "Avinash"
# B = 0
# for i in A:
#     B += 1
# print(B)


"""3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String"""

# string = 'w3'
#
# if len(string) > 2:
#     print(string[0:2],string[-2:])
# else:
#     print("empty string")

"""4. Write a Python program to get a string from a given string where all occurrences of its 
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""

# A = 'restart'
# B = ''
# C = A[0]
# B += C
# for i in A[1:]:
#     if i == C:
#         B += "$"
#     else:
#         B += i
# print(B)

"""5. Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

# A1 = 'abc'
# A2 = 'xyz'
#
# A = A1[0:2] + A2[2]
# B = A2[0:2] + A1[2]
# print(A,B)

"""6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing', add 'ly' instead. If the string length of the
 given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

# A = 'abkling'
#
# if len(A) >= 3 and "ing" in A:
#     print(A+"ly")
# elif len(A) < 3:
#     print(A)
# else:
#     print(A + "ing")

"""7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
 If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'"""

# A = 'The lyrics is not that poor!'
# B = 'The lyrics is poor!'
# find_not = A.find("not")
# find_poor = A.find("poor")
# if find_not < find_poor:
#     D = A[:find_not] + "good!"
#     print(D)

"""8. Write a Python function that takes a list of words and return the longest word and the length of 
the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9"""

# A = "Avinash", "is", "great", "guy"


# def my_fun(n):
#     B = ""
#     C = 0
#     for i in n:
#         if len(i) > C:
#             B = i
#             C = len(i)
#     return B, C
#
#
# obj = my_fun(A)
# print(obj)


# def fun(*m):
#     G = ""
#     L = 0
#     for i in m:
#         if len(i) > L:
#             G = i
#             L = len(i)
#     return G
#
#
# j = fun("Avinash", "is", "great", "guy")
# print(j)


# A = "Avinash"
# B = ""
#
# D = A[-1] + A[1:-1] + A[0]
# print(D)

"""11. Write a Python program to remove characters that have odd index values in a given string.
"""
# A = "Avinash"
# B = ""
#
# for i in range(len(A)):
#     if i%3 == 0:
#         B +=A[i]
# print(B)


"""12. Write a Python program to count the occurrences of each word in a given sentence.
"""
# A = 'the quick brown fox jumps over the lazy dog.'
# B = A.split()
# C = {}
# for i in B:
#     if i in C:
#         C[i] += 1
#     else:
#         C[i] = 1
# print(C)

"""13. Write a Python script that takes input from the user and displays that input back in upper and lower cases."""
# A = 'the quick brown fox jumps over the lazy dog.'
# print(A.upper())
# print(A.lower())

"""14. Write a Python program that accepts a comma-separated sequence of words as input and prints 
the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red"""

# A = "red, white, black, red, green, black"
# B = A.split()
# C = sorted(B)
# print(C)

"""15. Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'"""

# def fun(i, j):
#     print(f"<{i}>{j}</{i}>")
#
# fun("i", "Python")

# first_value = float(input("Enter first value:"))
# second_value = float(input("Enter second value:"))
# operation = input("Enter a operation:")
#
# while operation == "+":
#     print(first_value + second_value)
#     first_value = float(input("Enter first value:"))
#     second_value = float(input("Enter second value:"))
#     operation = input("Enter a operation:")
# elif operation == "-":
#     print(first_value - second_value)
# elif operation == "*":
#     print(first_value * second_value)
# elif operation == "/":
#     if second_value != 0:
#         print(first_value/second_value)
#     else:
#         print("Invalid")

"""17. Write a Python function to get a string made of 4 copies of the last two characters of a specified
 string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses"""

# def my_fun(m,n):
#     if len(m)>= 2:
#         return m[-2:] * n
# obj = my_fun("avinash",4)
# print(obj)

"""21. Write a Python function to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters."""


# def my_fun(strings):
#     for i in strings[:4]:
#         if i.upper() == i:
#             return strings.upper()
#
#
# obj = my_fun("AVinash")
# print(obj)
