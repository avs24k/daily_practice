"""1. Write a Python program to calculate the length of a string.
"""

# A = "Avinash"
# B = 0
# for i in A:
#     B +=1
# print(B)

"""2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""
# A = "google.com"
# B = {}
# for i in A:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
# print(B)

"""3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String"""

# string = 'w3resource'
#
# if len(string)> 2-1:
#     print(string[0:2],string[-2:])
# else:
#     print("empty string")

# def myfun(n):
#
#     if len(n) < 2:
#         return "empty string"
#     else:
#         return n[:2],n[-2:]
#
# print(myfun('w'))

"""4. Write a Python program to get a string from a given string where all occurrences of its 
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""

# string = 'restart'
# output = ""
# first_char = string[0]
# output += first_char
#
# for i in string[1:]:
#     if i == first_char:
#         output += "$"
#     else:
#         output += i
# print(output)

"""5. Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

# s1 = 'abc'
# s2 = 'xyz'
#
# A = s2[:2] + s1[2:]
# B = s1[:2] + s2[2]
# print(A,B)

"""6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing', add 'ly' instead. If the string length of the
 given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

# string = 'abin'
#
# def fun():
#     if len(string)<3:
#         print(string)
#
#     elif "ing" in string:
#         print(string[:-3]+"ly")
#     else:
#         print(string + "ing")
# fun()

"""7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
 If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'"""

# s1 = 'The lyrics is not that poor! The lyrics is poor!'
#
# def fun():
#     if "not" and "poor" in s1:
#         A =s1.replace("poor","good")
#         print(A)
#
# fun()

"""8. Write a Python function that takes a list of words and return the longest word and the length of 
the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9"""

#
# def long_word(*n):
#     longest_word = ""
#     len_of_longest_word = 0
#     for i in n:
#         if len(i) > len_of_longest_word:
#             longest_word = i
#             len_of_longest_word = len(i)
#
#     return longest_word, len_of_longest_word
#
#
# obj = long_word("avinash", "patil", "klkjnkjnkjnjjk")
#
# print(obj)

"""9. Write a Python program to remove the nth index character from a nonempty string.
"""
# A = "Avinash"
# n = 3
# B = A[:n] + A[n+1:]
# print(B)

"""10. Write a Python program to change a given string to a newly string where 
the first and last chars have been exchanged.
op = hvinasA"""

# A = "Avinash"
# C = A[-1] + A[1:-1] + A[0]
# print(C)

"""11. Write a Python program to remove characters that have odd index values in a given string.
"""
# A = "Avinash"
# B = ""
#
# for i in range(len(A)):
#     if i%2==0:
#         B+= A[i]
# print(B)

"""12. Write a Python program to count the occurrences of each word in a given sentence.
"""
# A = 'the quick brown fox jumps over the lazy dog.'
# C = A.split()
# B = {}
#
# for i in C:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
# print(B)

"""13. Write a Python script that takes input from the user and displays that input back in upper and lower cases."""

# A = 'the quick brown fox jumps over the lazy dog.'
#
# print(A.upper())
# print(A.lower())

"""14. Write a Python program that accepts a comma-separated sequence of words as input and prints 
the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red"""
# Sample_Words = "red, white, black, red, green, black"
# sorted_words = Sample_Words.split()
# A= sorted(sorted_words)
# print(A)

"""15. Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'"""

# def html_fun(A, B):
#     print(f'<{A}>{B}</{A}>')
# html_fun('i', 'Python')

"""16. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}"""

# A = "python"
# print(f"[[{A}]]")

"""17. Write a Python function to get a string made of 4 copies of the last two characters of a specified
 string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses"""

# def sample(string1):
#     print(string1[-2:]*4)
# sample("avinash")

"""18. Write a Python function to get a string made of the first three characters of a specified string.
 If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt"""

# def my_fun(inp):
#     if len(inp) < 3:
#         print(inp)
#     else:
#         print(inp[0:3])
# my_fun("Av")

"""19. Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python"""

# A = "https://www.w3resource.com/python-exercises"
# B = A.rsplit("-",1)[0]
# print(B)

"""20. Write a Python function to reverse a string if its length is a multiple of 4.
"""
# A = "ruby"
# if len(A) % 4 == 0:
#     print(A[::-1])

"""21. Write a Python function to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters."""

# def to_uppercase(str1):
#     num_upper = 0
#     for letter in str1[:4]:
#         if letter.upper() == letter:
#             num_upper += 1
#     if num_upper >= 2:
#         return str1.upper()
#     return str1
#
# print(to_uppercase('Python'))
# print(to_uppercase('PyThon'))

# A = "PyThon"
# B = ""
#
# for i in A[:4]:
#     if i.upper() == i:
#         B+=i
# print(B)

# A = 'Aviinash'

# def myfun(n):
#     for i in n:
#         if i.upper() in n[:4]:
#             print(n.upper())
#             break
#         else:
#             print('nothing')
#             break
# myfun(A)

"""Write a Python program to check whether a string starts with specified characters.
"""
# A = "w3respurces.com"
#
# if "w3r" in A[0:]:
#     print("True")
# else:
#     print("False")

#print(A.startswith("w3r"))

"""Sample string: 'thequickbrownfoxjumpsoverthelazydog'"""

# Sample_string= 'thequickbrownfoxjumpsoverthelazydog'
# A = {}
# for i in Sample_string:
#     if i in A:
#         A[i] += 1
#     else:
#         A[i] = 1
# print(A)

# A = "The quick brown fox jumps over the lazy dog."
# B = A.split()
# print(B[::-1])

