"""1. Write a Python program to find a list of integers with exactly two occurrences of nineteen
and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True"""
import time

# def my_fun(lst):
#     if lst.count(5) >= 3 and lst.count(19) >= 2:
#         return True
#     else:
#         return False
#
#
# obj = my_fun([19, 19, 5, 5, 5, 5, 5])
# print(obj)

"""2. Write a Python program that accepts a list of integers and calculates the length and the fifth element.
 Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False"""

# def my_fun(lst):
#     if len(lst) == 8 and lst.count(lst[4]) == 3:
#         return True
#
#
# obj = my_fun([11, 12, 14, 13, 14, 13, 15, 14])
# print(obj)

"""4. We are making n stone piles! The first pile has n stones. 
If n is even, then all piles have an even number of stones. 
If n is odd, all piles have an odd number of stones. Each pile must more stones than the 
previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]"""

# A = []
# n = 3
# for i in range(n):
#     B = n + 2*i
#     A.append(B)
# print(A)


# A = {'Ethernet1/4':['10G','25G','40G','100G'],'Ethernet1/5':['10G'],'Ethernet1/6':['100G']}
# B= {}
# for i,j in A.items():
#     for k in j:
#         if k in B:
#             B[k] += i
#         else:
#             B[k] = i
# print(B)

# arr = ["flower", "flow", "flight"]
# B = ""
# for i in arr:
#     A = i.split()
#     print(A)

"""5. Write a Python program to check the nth-1 string is a proper substring of the nth string 
in a given list of strings.
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True"""

""""6. Write a Python program to test a list of one hundred integers between 0 and 999,
 which all differ by ten from one another. Return True otherwise False.
Input:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 
 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 
 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 
 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
Output:
True
Input:
[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420,
 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860,
  880, 900, 920, 940, 960, 980]
Output:
False"""

# A = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
#  200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390,
#  400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600,
#  610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790,
#  800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
#
# B = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420,
#  440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860,
#   880, 900, 920, 940, 960, 980]

# for i in range(0,len(B)-1):
#     if B[i+1] - B[i]==10:
#         print("True")
#         break
#
#     else:
#         print("False")
#         break


"""7. Write a Python program to check a given list of integers where the sum of the first i integers is i.
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False"""

"""8. Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]"""

# A = "W3resource Python, Exercises."
# B = A.split()
# C = []
# D = []
# for i in B:
#     if i.isspace():
#         D.append(i)
#     # elif i not in C:
#     #     D.append(i)
#
# print(D)

# A = "W3resource Python, Exercises."
# B = A.split()
# D = []
# Z = [B, D]
#
# for char in A:
#     if char.isspace():
#         D.append(char)
#
# print(Z)

"""9. Write a Python program to find a list of integers containing exactly four distinct values, 
such that no integer repeats twice consecutively among the first twenty entries.
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False"""
# A = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]


#
# for i in range(len(A)-1):
#     print(A[i+1])


# def has_consecutive_repeats(lst):
#     for i in range(len(lst) - 1) :
#         if lst[i] == lst[i + 1]:
#             return False
#     return True
#
# # Test cases
# input1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# input2 = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# input3 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#
# output1 = has_consecutive_repeats(input1)
# output2 = has_consecutive_repeats(input2)
# output3 = has_consecutive_repeats(input3)

# print(output1)  # True
# print(output2)  # False
# print(output3)  # False

# def has_four_distinct_values(lst):
#     if len(set(lst)) == 4:
#         return True
#     else:
#         return False
#
#
# # Test cases
# input1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# input2 = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# input3 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#
# output1 = has_four_distinct_values(input1)
# output2 = has_four_distinct_values(input2)
# output3 = has_four_distinct_values(input3)
#
# print(output1)
# print(output2)
# print(output3)

# A = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
#
# B = []
#
# for i in A:
#     if i not in B:
#         B.append(i)
#
# if len(B) == 4:
#     print("True")
# else:
#     print("False")


"""10. Given a string consisting of whitespace and groups of matched parentheses, 
write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']"""

"""11. Write a Python program to find the indexes of numbers in a given list below a given threshold.
Original list:
[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Threshold: 100
Check the indexes of numbers of the said list below the given threshold:
[0, 1, 2, 3, 7, 8, 9, 10]
Original list:
[0, 12, 4, 3, 49, 9, 1, 5, 3]
Threshold: 10
Check the indexes of numbers of the said list below the given threshold:
[0, 2, 3, 5, 6, 7, 8]"""

# A = [0, 12, 4, 3, 49, 9, 1, 5, 3]
#
# B = []
#
# for i in range(len(A)):
#     if A[i] < 10:
#         B.append(i)
# print(B)

"""12. Write a Python program to check whether the given strings are palindromes or not. 
Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]"""

# def palidrom(lst):
#     for i in lst:
#         return i[0:] == i[::-1]
#
#
# A = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# obj = palidrom(A)
# print(obj)


# def rest(strs):
#     return [s == s[::-1] for s in strs]
#
#
# strs = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# print(rest(strs))


"""decorators"""


# def outer(new):
#     def inneer():
#         B = new_fun()
#         Add = 5 + B
#         return Add
#
#     return inneer
#
# @outer
# def new_fun():
#     return 10
#
#
# obj = outer()
# print(obj())

# def log_args_and_return(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         print(f"{func.__name__} returned: {result}")
#         return result
#     return wrapper
#
# @log_args_and_return
# def add(a, b):
#     return a + b
#
# add(2, 3)


# def decor(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#
#     return wrapper
#
#
# @decor
# def say_hello():
#     return "Hello"
#
#
# obj = say_hello()
# print(obj)


# def decor(func):
#     def wrapper(*args):
#         startt_time = time.time()
#         result = func(*args)
#         end_time = time.time()
#         print(f"{func.__name__} took {end_time - startt_time:f} seconds")
#         return result
#
#     return wrapper

# @decor
# def meassure_time():
#     return time.sleep(3)
#
# obj = meassure_time()
# print(obj)


"""13. Write a Python program to find strings in a given list starting with a given prefix.
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']"""

# A = [( 'ca',('cat', 'car', 'fear', 'center'))]
#
# for i in A:
#     start = i[0]
#     tpple = i[1]
#     for j in tpple:
#         if start in j:
#             print(j)


"""14. Write a Python program to find the length of a given list of non-empty strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]"""

# A = ['cat', 'car', 'fear', 'center']
# C = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# B = [len(i) for i in C]
# print(B)

"""15. Write a Python program to find the longest string in a given list of strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter"""

# A = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# B = []
# for i in A:
#     if len(i) > len(B) :
#         B = i
# print(B)

"""16. Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]"""

# A = [("o",('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
#
# B = []
# for i in A:
#     word = i[0]
#     tpple = i[1]
#     for j in tpple:
#         if word in j:
#             B.append(j)
# print(B)

"""17. Write a Python program to create a string consisting of non-negative integers up to n inclusive.
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"""
# for i in range(1,16):
#     print(str(i),end=" ")

"""18. An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each
 row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed 
on them, but they are useful as arrays in computing.
Write a Python program to find the indices of all occurrences of target in the uneven matrix.
Input:
[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
Output:
[[0, 4], [1, 0], [1, 3], [4, 1]]
Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
Output:
[[0, 1], [0, 3], [2, 2]]"""

# def find_indices_in_ragged_matrix(matrix, target):
#     indices = []
#     for row_index, row in enumerate(matrix):
#         if isinstance(row, (list, tuple)):  # Check if the row is iterable
#             for col_index, element in enumerate(row):
#                 if element == target:
#                     indices.append([row_index, col_index])
#     return indices
#
# # Example usage:
# input1 = ([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19
# input2 = ([1, 2, 3, 2], [], [7, 9, 2, 1, 4], 2)
#
# output1 = find_indices_in_ragged_matrix(input1[0], input1[1])
# output2 = find_indices_in_ragged_matrix(input2[0], input2[1])
#
# print(output1)  # Output: [[0, 4], [1, 0], [1, 3], [4, 1]]
# print(output2)  # Output: [[0, 1], [0, 3], [2, 2]]


# input3 = ([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19
#
# for index_value,row in enumerate(input3):
#     if isinstance(row,(tuple,list)):
#         for matrix_index,column in enumerate(row):

























