# A = [1, 2, 3, 4, 5]
# total = 0
#
# for i in A:
#     total = total + i
# print(total)

# A = [1, 2, 3, 4, 5]
# total = 1
# for i in A:
#     total = total * i
# print(total)

"""3. Write a Python program to get the largest number from a list."""
# A = [2, 3, 4]
# B = A[0]
# C = A[0]
# for i in range(len(A)):
#     if B < A[i]:
#         B = A[i]
#     else:
#         if C < A[i] and C < B:
#             C = A[i]
#
# print(C)

"""5. Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

# A = ['abc', 'xyx', 'aba', '1221']
# B = 0
#
# for i in A:
#     if i[0] == i[-1]:
#         B +=1
# print(B)

"""6. Write a Python program to get a list, sorted in increasing order by 
the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""

# A = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# B = sorted(A,key= lambda x: x[1])
# print(B)

"""7. Write a Python program to remove duplicates from a list.
"""
# A = [1, 2, 3, 4, 5,5,4]
# B = []
#
# for i in A:
#     if i not in B:
#         B.append(i)
# print(B)

"""8. Write a Python program to check if a list is empty or not."""

# A= [1,4]
#
# if A:
#     print("not empty")
# else:
#     print("empty")

# n= 5
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

"""10. Write a Python program to find the list of words that are longer than n from a given list of words."""

# my_list = ["avi","is","greatjnm","person"]
# A = []
# for i in my_list:
#     if len(i) > 5:
#         A.append(i)
# print(A)

"""11. Write a Python function that takes two lists and returns True if they have at least one common member."""

# def my_fun(A,B):
#     result = False
#     for i in A:
#          for j in B:
#                 if i == j:
#                     return True
#     return result
#
# A = [1, 2, 3, 4, 5,4]
#
# B = [5,4]
# obj = my_fun(A,B)
# print(obj)

"""12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

# my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# remove = [0,4,5]
# A = []
# for i in range(len(my_list)):
#     if i not in remove:
#         A.append(my_list[i])
# print(A)

"""13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""

# A = [[["*" for _ in range(6)] for _ in range(4)] for _ in range(3)]
#
# for i in A:
#     for j in i:
#         print(j)
#     print()

"""14. Write a Python program to print the numbers of a specified list after removing even numbers from it."""
# A = []
#
# for i in range(10):
#     if i%2 !=0:
#         A.append(i)
# print(A)

"""19. Write a Python program to calculate the difference between the two lists.
"""

# A=[1,2,3,4,5,6]
# B=[1,2]
# C = 0
#
# for i in A:
#     if i not in B:
#         C +=1
# print(C)

# A = ["Avi","patil"]
# B = " ".join(A)
# print(B)

"""22. Write a Python program to find the index of an item in a specified list.
"""
# A = [1, 2, 3, 4, 5, 6]
# B = []
# for i in range(1,len(A)):
#     if A[i] == 4 :
#         print(i)
#


"""24. Write a Python program to append a list to the second list.
o/p=[1, 2, 3, 4, 5, 'avi', 'B', 'C', 'd']
"""
# A = [1, 2, 3, 4, 5]
# B = ['avi', 'B', 'C', 'd']
# C = A.pop(B)
#
# print(C)


"""27. Write a Python program to find the second largest number in a list.
"""

# A = [1, 2, 3, 4, 5]
# B = A[0]
# C = A[0]
# for i in range(len(A)):
#     if B < A[i]:
#         B = A[i]
# for j in range(len(A)):
#     if C < A[j] and A[j] < B:
#         C = A[j]
# print(C)

"""28. Write a Python program to find the second smallest number in a list.
"""
# A = [-1,1, 2, 3, 4, 5]
# B = float(A[0])
# C = float(A[0])
#
# for i in range(len(A)):
#     if B > A[i]:
#         B = A[i]
# for j in range(len(A)):
#     if C > A[j] and A[j] != B :
#         C = A[j]
# print(B)
# print(C)
#
# smallest = float('inf')
# seco_msmallest = float('inf')
#
# for i in range(len(A)):
#     if smallest > A[i]:
#         smallest = A[i]
#
# for j in range(len(A)):
#     if seco_msmallest > A[j] and A[j] != smallest:
#         seco_msmallest = A[j]
#
# print("smalest value:",smallest)
# print("second smallest value:",seco_msmallest)
#


# A = [-1, 1, 2, 3, 4, 5]
# B = A[0]
# C = float('inf')  # Initialize C to positive infinity
#
# for i in range(len(A)):
#     if B > A[i]:
#         C = B  # Update C to the previous value of B
#         B = A[i]
#
# print("Smallest value:", B)
# print("Second smallest value:", C)

"""30. Write a Python program to get the frequency of elements in a list.
"""
# A = [0,1, 2,2,5, 3, 4, 3,5,6]
# B = {}
#
# for i in A:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
# print(B)
"""question """

"""31. Write a Python program to count the number of elements in a list within a specified range.
"""
# A = [0,1, 2,2,5, 3, 4, 3,5,6]
# B = 0
#
# for i in range(len(A)):
#     if A[i] < A[5]:
#         B += A[i]
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
#         B.append(j+str(i))
# print(B)

"""40. Write a Python program to split a list based on the first character of a word.
"""

# A = ["avi", "ramesh", "chama", "boutkar", "patil"]
# B ={}
#
# for i in range(0,len(A)):
#     for j in range(1,len(A)):
#         if char == A[i]

# A = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# B = []
#
# for i in A:
#     if isinstance(i,list):
#         for j in i:
#             B.append(j)
# print(B)

# A = [{1:2},{},{}]

# for i in A:
#     if len(i)> 0:
#         print("not Empty")
#         break
#     else:
#         print("empty")
#         break

# A = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# n = "c"
# B = []
# for i in A:
#     if i[0] == n:
#         B.append(i)
#     else:
#         pass
# print(B)

# ip = [0,1,2,3,4,5,6,7,8,9]
# n = 5
# op = []
# for i in ip:
#     if n < i:
#         op.append(i)
# print(op)

# Sample =[[1,2,3], [4,5,6], [1,1,0], [7,8,9]]
# op = []
#
# A = max(Sample,key= lambda x: (x[0],x[-1]))
# print(A)

# A = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# B = []
# C = []
# for i in A:
#     if i > 0:
#         B.append(i)
#
#     else:
#         C.append(i)
# B.extend(C)
# print(B)

# num = [1, 2, 3]
# color = ['red', 'white', 'black']
#
# for i,j in zip(num,color):
#     print(i,j)

# A = [1,2,3,4]
# B = "emp"
# C = []
#
# for i in A:
#     C.append(B + str(i))
# print(C)

# p=[1,2,3,4,5]
# print(*p)

# A = {}
# for i in range(5):
#     print(A,end="")

# x = [(4, 1), (1, 2), (6, 0)]
# A = min(x,key= lambda v : (v[1],v[0]))
# print(A)

# A = [1, 3, 5, 7, 9, 10]
# B = [2, 4, 6, 8]
#
# A.pop()
# A.extend(B)
# print(A)

# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# A = [C[i::2] for i in range(3)]
# print(A)

# sample_lists= ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
#
# for i,j in zip(sample_lists[0],sample_lists[1]):
#     dict = {"name" : i, "code":j }
#     print(dict)

# A = ["Avi","Patil","Ramesh"]
#
# for i in A:
#     for j in ("c",i):
#         print(j,end=",")

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
B = []
#
# for i in L:
#     for j in i:
#         if j not in B:
#             B.append(j)
# print(B)
A =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# p=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for i in range(1,len(A),5):
    B  = i*5
    print(B)






