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
# A = [1, 3, 4, 5, 6, 7]
# B = float("inf")
# C = float("inf")
#
# for i in range(len(A)):
#     if A[i] < B:
#         B=A[i]
# for j in range(len(A)):
#     if A[j] > B and A[j] < C:
#         C=A[j]
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

# A = [0,1, 2,2,5, 3, 4, 3,5,6]
# B = {}
#
# for i in A:
#     if i in B:
#         B[i] += 1
#
#     else:
#         B[i] = 1
# print(B)

"""31. Write a Python program to count the number of elements in a list within a specified range.
"""

# A = 0
# for i in range(10):
#     if 3 <= i <=8:
#         A +=1
# print(A)


""""35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

# A = ['p', 'q']
# B = []
# for i in A:
#     for j in range(5):
#         B.append(i+ str(j))
# print(B)

"""37. Write a Python program to find common items in two lists.
"""

# A = [1,2,3,4,5,6,7]
# B = [6,7,8,9,10,5]
#
# C = []
# for i in A:
#     if i in B:
#         C.append(i)
# print(C)

"""38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""
# A = [0, 1, 2, 3, 4, 5]

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
#     if i[0] in B:
#         B[i[0]].append(i)
#     else:
#         B[i[0]] = i
# print(B)

"""41.  String in Ascending Order"""
# A = ["avi", "ramesh", "chama", "boutkar", "patil"]
#
# for i in range(8):
#     print([]*i,end=",")

"""42. Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h"""
# A = ["a", "b", "c", "d", "e", "f"]
# B = ["d", "e", "f", "h", "g"]
# C = []
# D = []
#
# for i in A:
#     if i not in B:
#         C.append(i)
# for j in B:
#     if j not in A:
#         D.append(j)
#
# print(C)
# print(D)

"""43. Write a Python program to split a list into different variables.
"""
# A = [1,2]
# A1,A2 = A
# print(A1)

"""44. Write a Python program to generate groups of five consecutive numbers in a list.
o/p=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
"""

# for i in range(1,15,5):
#     A = range(i, (i+5))
#     print(list(A),end=",")


"""45. Write a Python program to convert a pair of values into a sorted unique array.
"""

"""46. Write a Python program to select the odd items from a list.
"""
# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(B[::2])

"""47. Write a Python program to insert an element before each element of a list.
"""

# A = ["Avi","Patil","Ramesh"]
# for i in A:
#     for j in ("C",i):
#         print(j,end=",")


"""48. Write a Python program to print nested lists (each list on a new line) using the print() function.
"""
"""49. Write a Python program to convert a list to a list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
 {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]"""

# A = ["#000000", "#FF0000", "#800000", "#FFFF00"], ["Black", "Red", "Maroon", "Yellow"]
# C = []
# for i,j in zip(A[0],A[1]):
#     dic = {"color_name":i,"color_code":j}
#     print(dic)


"""50. Write a Python program to sort a list of nested dictionaries.
"""

# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
#
# A = sorted(my_list,key= lambda x:x["key"]["subkey"])
# print(A)

# A = [1,2,4,6,8,9]
# B  = []
#
# for i in range(1,10):
#     if i not in A:
#         B.append(i)
# print(B)

# A = [1, 3, 5, 7, 9, 10]
# B = [2, 4, 6, 8]
# A.pop()
# A.extend(B)
# print(A)

"""60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
"""
# x = [(4, 1), (1, 2), (6, 4)]
# A = min(x,key= lambda x:x[1])
# print(A)

# for i in range(10):
#     print({}, end=",")

"""62. Write a Python program to print a list of space-separated elements.
i/p=[1,2,3,4,5],  o/p-1 2 3 4 5"""

# p=[1,2,3,4,5]
# print(*p)

# A = [1,2,3,4]
# B = "emp"
# C = []
#
# for i in A:
#     C.append(B + str(i))
# print(C)

# num = [1, 2, 3]
# color = ['red', 'white', 'black']
#
# for i, j in zip(num,color):
#     print(i,j)


# A = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# B = []
# C = []
#
# for i in A:
#     if i > 0:
#         B.append(i)
#     else:
#         C.append(i)
# B.extend(C)
# print(B)

"""66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]"""

# A = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# B = max(A,key= lambda x:(x[0],x[-1]))
# print(B)


"""67. Write a Python program to find all the values in a list that are greater than a specified number.
i/p = [0,1,2,3,4,5,6,7,8,9]
n=5
o/p=[6,7,8,9]
"""
# A = [0,1,2,3,4,5,6,7,8,9]
# B = []
# for i in A:
#     if i > 5:
#         B.append(i)
# print(B)
#
# B = []
# A = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
#
# for i in A:
#     if i[0] == "a":
#         print("Items start with a from the said list:",i)
#
#     elif i[0] == "b":
#         print("Items start with b from the said list:",i)


# A = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# B = []
#
# for i in A:
#     if isinstance(i,list):
#         for j in i:
#             B.append(j)
#     else:
#         B.append(i)
# print(B)

"""
1) Duplicate values in list
"""
# List  = [1,1,2,2,3,3,4,5]
# unique = set()
# duplicate= []
# for i in List:
#     if i in unique:
#         duplicate.append(i)
#     else:
#         unique.add(i)
#
# print(duplicate)

# List1  = [1,1,2,2,3,3,4,5]
# A = []
# B = []
# for i in List1:
#     if i not in A:
#         A.append(i)
#     else:
#         B.append(i)
# print(B)


"""
2) WAP to find first 5 even numbers using lamda function
"""

# A = filter(lambda x:x%2==0, range(10))
# print(list(A))

"""
3) How many time "t" is coming on string
"""
# stri = "india is the best country"
# count = 0
#
# for i in stri:
#     if "a" in i:
#         count += 1
# print(count)

"""
4) This program reads the contents of the file "Interview.txt,counts the number of uppercase letters in 
the file,and then prints the last character of the file and the total count of uppercase letters.
"""

# upper_case = 0
#
# with open("Interview.text","r") as reading_file:
#     file = reading_file.read()
#     for i in file:
#         if i.isupper():
#             print(i)
#             upper_case += 1
# print(upper_case)


"""
5) Reverse the string
"""

# strng = "i love my India"
#
# print(strng[::-1])
#
# strng = "i love my India"
# s = ""
# for i in strng:
#     s = i + s
# print(s)



"""
6) print table of 5
"""
# for i in range(1,11):
#     print(f"5 * {i} =",5*i)

"""
7) swap value
"""

# a = 2
# b = 3
#
# a,b =b,a
#
# print(a,b)
""" 
8) Find the count of numbers containing '6' in it from the sequence 1 to 1000.
Also print the numbers
"""
# count = 0
#
# for i in range(1000):
#     if "6" in str(i):
#         count += 1
# print(count)

"""
9) count of the value of occurance
"""

# str = "you are welcome to python programming are welcome to python programming"
# split_str = str.split()
# A = {}
# for i in split_str:
#     if i in A:
#         A[i]+= 1
#     else:
#         A[i] = 1
# print(A)

"""
10) The provided code generates a list result containing the missing integers from 
the range between the minimum and maximum values of the inputs list.
"""

# inputs = [6,3,5,1,2,10]
# op = []
#
# for i in range(min(inputs),max(inputs) ):
#     if i not in inputs:
#         op.append(i)
# print(op)

"""
11) Input :- "i am the input"
     Output:- "the input am i"
"""
# A = "i am the input"
# V = A.split()
# B = V[:-2]
# C = V[2::]
# F = reversed(B)
# D = tuple(B) + tuple(F)
# print(D)

"""
12) Sort the dictionary on basis of values 
"""
# #approch1 :
# dict1 = {'a':5, 'b':3, 'c':4, 'd':1, 'e':2}
# B = sorted(dict1.items())
# A = sorted(B,key= lambda x:x[1])
# print(A)

# people = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 18},
#     {'name': 'David', 'age': 22}
# ]
#
# A = sorted(people, key= lambda x:x["age"])
# print(A)

""" 
13) how will be two mandatory and two optional paramter in function
"""
# def my_fun(A,B,C=None,D=None):
#     print(A+B + C)
# my_fun(1,2,C =3,D =4)

"""write a python program to multiply elements of two list save in new list"""
# list1 = [2, 4, 6, 8, 10]
# list2 = [2, 3, 4, 5, 6]
# A = []
#
# for i,j in zip(list2,list1):
#     A.append(i * j)
#
# print(A)

""" remove spaces from input string without inbuilt function.
input = "remove spaCes from this stRing 123 "
output = "removespacesfromthisstring123" """

# input = "remove spaCes from this stRing 123 "
# op = ""
# for i in input:
#     if i != '':
#         op +=i
# print(op)
#
# input_string = "remove spaCes from this stRing 123 "
# output_string = ""
#
# for char in input_string:
#     if char != ' ':
#         output_string += char
#
# print("Input string:", input_string)
# print("Output string:", output_string)

"""Python Program To Remove Duplicates From A Given String:"mississippi"""

# A = "mississippi"
# B = ""
#
# for i in A:
#     if i not in B:
#         B += i
# print(B)

# Sample String : 'restartthecomputer'
# # Expected Result : 'resta$$$h$comp$$$'

# String = 'restartthecomputer'
# B = []
#
# for i in String:
#     if i in B:
#         B.append("$")
#     else:
#         B.append(i)
# print("".join(B))
# C = ""
# for i in String:
#     if String.count(i) > 1:
#         C += "*"
#     else:
#         C += i
#
# print(C)

"""python program to display Maximum frequency character in String"""
# A = "avinash patil is best is"
# B = A.split()
# C = {}
#
# for i in B:
#     if i in C:
#         C[i] +=1
#     else:
#         C[i] = 1
# print(C)

Example= "iworkatcelestialsystems"
"""Output: etials"""

# duplicate = ""
# unique = ""
#
# for i in Example:
#     if i not in duplicate:
#         duplicate += i
#
# print(duplicate)



#
# for i in Example:
#     if i in duplicate:
#         duplicate += i
#     else:
#         unique += i
# print(duplicate)
#
# A = ""
# for i in Example:
#     if Example.count(i) == 1:
#         if i not in A:
#             A += i
# print(A)



# def triangle_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* " ,end= "")
#         print("\n")
#
#     for i in range(1,n+1):
#         print(" " * (n-i) + " *" * i)
#
# n = int(input("enter rows"))
# triangle_pattern(n)

# n = 6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()























