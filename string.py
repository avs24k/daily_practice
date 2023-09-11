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

