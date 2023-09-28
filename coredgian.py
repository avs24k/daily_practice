"""LIST"""
import random

"""1. Write a Python program to sum all the items in a list.
"""
# A = [1, 2, 3, 4, 5]
# B = 1
#
# for i in A:
#     B *= i
# print(B)

"""3. Write a Python program to get the largest number from a list.
"""
# A = [1, 2, 3, 4, 5]
# B = A[0]
#
# for i in range(len(A)):
#     if A[i] > B:
#         B = A[i]
# print(B)

"""3. Write a Python program to get the smallest number from a list.
"""

# A = [1, 2, 3, 4, 5]
# B = A[0]
# for i in range(len(A)):
#     if B > A[i]:
#         B = A[i]
# print(B)

"""5. Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

# A = ['abc', 'xyz', 'aba', '1221']
# B = 0
#
# for i in A:
#     if len(i) >= 2 and i[0]==i[-1]:
#         B +=1
# print(B)

"""6. Write a Python program to get a list, sorted in increasing order by 
the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""
#
# A = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# B = sorted(A,key= lambda x:x[1])
# print(B)


"""7. Write a Python program to remove duplicates from a list.
"""
# A = [ 2, 3, 4, 6, 5,6,3,5]
# B = []
# for i in A:
#     if i not in B:
#         B.append(i)
# print(B)

# A = [2, 3, 4, 6, 9]
# B = []
# for i in range(min(A),max(A)):
#     if i not in A:
#         B.append(i)
# print(B)
#
# A = [2, 3, 4, 6, 9]
# B = []
# for i in range(10):
#     if i not in A:
#         B.append(i)
# print(B)

"""10. Write a Python program to find the list of words that are longer than n from a given list of words."""

# my_list = ["avi","is","greatjnm","person"]
# n = 5
# B = []
# for i in my_list:
#     if len(i) > n:
#         B.append(i)
# print(B)

"""11. Write a Python function that takes two lists and returns True if they have at least one common member."""
# A = [1,2,3,4,5]
# B = [5,6,7,8,9]
#
# def my_fun(n,m):
#     result = False
#     for i in n:
#         for j in m:
#             if j == i:
#                 return True
#     return result
# obj = my_fun(A,B)
# print(obj)

"""12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

# A = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# B = [0,4,5]
# C = []
#
# for i in range(len(A)):
#     if i not in B:
#         C.append(A[i])
# print(C)

"""13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
# A = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
# for i in A:
#     for j in i:
#         print(j)
#     print()

"""14. Write a Python program to print the numbers of a specified list after removing even numbers from it."""
# A = []
# for i in range(20):
#     if i % 2 != 0:
#         A.append(i)
# print(A)

"""15. Write a Python program to shuffle and print a specified list.
"""
# A = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# random.shuffle(A)
# print(A)

"""19. Write a Python program to calculate the difference between the two lists.
"""
# A = [1, 2, 3, 4, 5, 6]
# B = [6, 7, 8, 2, 1, 3]
# diff = []
# for i in A:
#     if i not in B:
#         diff.append(i)
#
# print(diff)

"""20. Write a Python program to access the index of a list.
"""
# A = [1, 2, 3, 4, 5, 6]

# for i,j in enumerate(A):
#     print(i,j)
#
# print(A.index(5))
# print(A[3])
# # B = []
# # for i in range(len(A)):
# #     if A[]

"""21. Write a Python program to convert a list of characters into a string.
"""
# A = ["a","S"]
# B = ''
#
# print("".join(A))
#
#
# for i in A:
#     B += i
# print(B)

"""22. Write a Python program to find the index of an item in a specified list.
"""
# A = [1, 2, 3, 4, 5, 6]
# for i in range(1,len(A)):
#     if A[i] == 5:
#         print(i)

# A = [[2,4,3],[1,5,6], [9], [7,9,0]]
# B = []
# for i in A:
#     for j in i:
#         B.append(j)
# print(B)

"""27. Write a Python program to find the second largest number in a list.
"""
# A = [1, 2, 3, 4, 5, 6]
# B = A[0]
# C = A[0]
#
# for i in range(len(A)):
#     if A[i] > B:
#         B = A[i]
# for j in range(len(A)):
#     if C < A[j] < B:
#         C = A[j]
# print(C)

"""28. Write a Python program to find the second smallest number in a list.
"""
# A = [1, 2, 3, 4, 5, 6]
# B = float("inf")
# C = float("inf")
#
# for i in range(len(A)):
#     if A[i] < B:
#         B = A[i]
# for j in range(len(A)):
#     if B < A[j] < C:
#         C = A[j]
# print(C)

"""29. Write a Python program to get unique values from a list.
"""

# A = [0,1, 2,2,5, 3, 4, 3,5,6]
# B = []
#
# for i in A:
#     if i not in B:
#         B.append(i)
#
# print(B)

"""30. Write a Python program to get the frequency of elements in a list.
"""
# A = [0, 1, 2, 2, 5, 3, 4, 3, 5, 6]
# B = {}
#
# for i in A:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
# print(B)

"""31. Write a Python program to count the number of elements in a list within a specified range.
"""
# A = [0, 1, 2, 2, 5, 3, 4, 3, 5, 6]
# B = 0
# for i in A:
#     if 2  < i < 6:
#         B += 1
# print(B)

""""35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

# A = ['p', 'q']
# B = []
#
# for i in range(1,6):
#     for j in A:
#         B.append(j + str(i))
# print(B)

"""37. Write a Python program to find common items in two lists.
"""
# A = [1, 2, 3, 4]
# B = [6, 7, 8, 4]
# C = []
# for i in A:
#     if i in B:
#         C.append(i)
#
# print(C)

"""38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""

"""39. Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350"""

# A = [11, 33, 50]
# for i in A:
#     print(i,end="")

"""40. Write a Python program to split a list based on the first character of a word.
"""
# A = ["avi", "ramesh", "chama", "boutkar", "patil"]
# B ={}
#
# for i in A:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
# print(B)

"""41.  String in Ascending Order"""

# A = ["avi", "ramesh", "chama", "boutkar", "patil"]

"""42. Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h"""
#
# A = ["a", "b", "c", "d", "e", "f"]
# B = ["d", "e", "f", "h", "g"]

"""44. Write a Python program to generate groups of five consecutive numbers in a list.
o/p=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
"""

# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# C = []
#
# for i in range(1, 20, 5):
#     A = range(i, i+5)
#     print(list(A), end=",")

"""45. Write a Python program to convert a pair of values into a sorted unique array.
"""
"""47. Write a Python program to insert an element before each element of a list.
"""

# A = ["Avi", "Patil", "Ramesh"]
# B = []
# for i in A:
#     for j in ("C",i):
#         B.append(j)
# print(B)

"""49. Write a Python program to convert a list to a list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
 {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]"""

# A = ["Black", "Red","Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
#
# for i,j in zip(A[0],A[1]):
#     dict = {"name":i,"color":j}
#     print(dict)

# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
#
# A = sorted(my_list,key= lambda x:x["key"]['subkey'])
# print(A)

# x = [(4, 1), (1, 2)]
# A = min(x ,key=lambda y:y[1])
# print(A)

# for i in range(10):
#     print({})
#
# A = [{} for i in range(10)]
# print(A)

"""63. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']"""

# A = [1,2,3,4]
# B = []
#
# for i in A:
#     B.append("emp" + str(i))
# print(B)

"""64. Write a Python program to iterate over two lists simultaneously.
i/p : 
num = [1, 2, 3]
color = ['red', 'white', 'black']"""

# color = ['red', 'white', 'black']
# num = [1, 2, 3]
#
# for i,j in zip(num,color):
#     print(i,j)


"""65. Write a Python program to move all zero digits to the end of a given list of numbers.
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]"""

# A = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# B = []
# C = []
# for i in A:
#     if i > 0:
#         B.append(i)
#     else:
#         C.append(i)
# B.extend(C)
# print(B)

# A = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# B = max(A,key= lambda x: (x[0],x[-1]))
# print(B)

"""STRING"""
"""1. Write a Python program to calculate the length of a string.
"""

# A = "Avinash"
# B = 0
#
# for i in A:
#     B += 1
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
#
# A = 'w3resource'
#
# if len(A) > 2:
#     print(A[0:2],A[-2:])
# else:
#     print("Empty string")

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

# A = 'abc'
# B = 'xyz'
#
# C = A[0:2] + B[2:]
# D = B[0:2] + A[2:]
# print(C,D)

"""6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing', add 'ly' instead. If the string length of the
 given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

# A = "abcing"
#
# if len(A) < 3:
#     print(A)
# elif "ing" in A:
#     print(A[:-3] + "ly")
# else:
#     print(A + "ing")

"""7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
 If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'"""

# A = "avinash", "patil", "klkjnkjnkjnjjk"
# B = ''
# C = 0
#
# for i in A:
#     if len(i) > len(B):
#         B = i
#         C = len(B)
# print(B,C)

# A = "avinash"
# B = ""
# for i in A:
#     B = i + B
# print(B)

# A = "Avinash"
# B = A[:3] + A[4:]
# print(B)

# A = "Avinash"
# print(A[-1] + A[1:-2] + A[0])

"""11. Write a Python program to remove characters that have odd index values in a given string.
"""
# A = "Avinash"
# B = ""
#
# for i in range(len(A)):
#     if i%2 != 0:
#         B += A[i]
# print(B)

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
# A = "Avinash"
# print(A.upper(),A.lower())
"""21. Write a Python function to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters."""

A = "AVinash"

for i in A[:4]:
    if A.upper() == i:
        print(A.upper())

























