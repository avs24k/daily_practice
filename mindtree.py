"""1. Write a Python program to sum all the items in a list.
"""
# A = [1, 2, 3, 4, 5, 6]
# B = 0
# for i in A:
#     B += i
# print(B)

# A = [1, 2, 3, 4, 5, 6]
# B = 1
#
# for i in A:
#     B = B * i
# print(B)

"""3. Write a Python program to get the largest number from a list.
"""
# A = [1, 2, 3, 4, 6, 5]
# B = A[0]
#
# for i in range(len(A)):
#     if B < A[i]:
#         B = A[i]
# print(B)

"""3. Write a Python program to get the smallest number from a list.
# """
#
# A = [2, 3, 4, 6, 5]
# B = A[0]
#
# for i in range(len(A)):
#     if B > A[i]:
#         B = A[i]
# print(B)

"""5. Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

# A = ['abc', 'xyx', 'aba', '1221']
# B = 0
#
# for i in A:
#     if len(i) >= 2 and i[0]==i[-1]:
#         B += 1
# print(B)

"""6. Write a Python program to get a list, sorted in increasing order by 
the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""

# A = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# B = sorted(A,key= lambda  x : x[1])
# print(B)

"""7. Write a Python program to remove duplicates from a list.
"""
# A = [ 2, 3, 4, 6, 5,6,3,5]
# B = []
#
# for i in A:
#     if i not in B:
#         B.append(i)
# print(B)

"""8. Write a Python program to check if a list is empty or not.
"""

# A = [1, 2]
#
# if A:
#     print("not empty")
# else:
#     print("empty")

"""10. Write a Python program to find the list of words that are longer than n from a given list of words."""
# my_list = ["avi","is","greatjnm","person"]
# B = []
#
# for i in my_list:
#     if len(i) > 6:
#         B.append(i)
# print(B)

"""11. Write a Python function that takes two lists and returns True if they have at least one common member."""
# def my_fun(A,B):
#     result = False
#     for i in A:
#         for j in B:
#             if j == i:
#                 return True
#     return result
# obj = my_fun([1,2,3],[3,5,4])
# print(obj)


"""12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

# A = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# B = [0, 4, 5]
# C = []
# for i in range(len(A)):
#     if i in B:
#         C.append(A[i])
# print(C)

"""13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
# A = [[["*" for _ in range(6)] for _ in range(4)] for _ in range(3)]
# for i in A:
#     for j in i:
#         print(j)
#     print()

"""14. Write a Python program to print the numbers of a specified list after removing even numbers from it."""

# A = []
# for i in range(10):
#     if i%2 != 0:
#         A.append(i)
# print(A)

"""15. Write a Python program to shuffle and print a specified list"""

"""19. Write a Python program to calculate the difference between the two lists.
"""
# A=[1,2,3,4,5,6,7]
# B=[6, 7, 8, 2, 1, 3]
# C = []
#
# for i in A:
#     if i not in B:
#         C.append(i)
# print(C)

"""20. Write a Python program to access the index of a list.
"""
# n = 2
# A = [1,2,3,4,5,6]
# print(A[n])

"""22. Write a Python program to find the index of an item in a specified list.
"""

# A = [1,2,3,4,5,6]
# B = A.index(5)
# print(B)

"""23. Write a Python program to flatten a shallow list.
"""
# A = [[2,4,3],[1,5,6], [9], [7,9,0]]
# B = []
# for i in A:
#     for j in i:
#         B.append(j)
# print(B)

"""24. Write a Python program to append a list to the second list.
o/p=[1, 2, 3, 4, 5, 'avi', 'B', 'C', 'd']
"""
# A= ['avi', 'B', 'C', 'd']
# B = [1, 2, 3, 4, 5]
# A.extend(B)
# print(A)

"""27. Write a Python program to find the second largest number in a list.
"""

# A = [1, 2, 3, 4, 5, 6, 7]
# B = A[0]
# C = A[0]
#
# for i in range(len(A)):
#     if A[i] > B:
#         B = A[i]
# for j in range(len(A)):
#     if A[j] > C and A[j] < B:
#         C = A[j]
# print(C)

"""28. Write a Python program to find the second smallest number in a list.
"""









































