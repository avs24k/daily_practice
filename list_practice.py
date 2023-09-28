"""1. Write a Python program to sum all the items in a list.
"""
# A = [1, 2, 3, 4, 5]
# B = 0
# for i in A:
#     B = B + i
# print(B)

"""1. Write a Python program to multiply all the items in a list.
"""
# count = 1
#
# for i in range(1,5):
#     count = count * i
# print(count)

"""3. Write a Python program to get the largest number from a list.
"""
# A = [1, 2, 3, 4, 6, 5]
# B = A[0]
#
# for i in range(len(A)):
#     if A[i] > B:
#         B = A[i]
# print(B)

"""3. Write a Python program to get the smallest number from a list.
"""
# A = [ 2, 3, 4, 6, 5]
# B = A[0]
#
# for i in range(len(A)):
#     if A[i] < A[0]:
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
#     if i[0]==i[-1]:
#         B += 1
# print(B)

"""6. Write a Python program to get a list, sorted in increasing order by 
the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""

# A = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# B = sorted(A,key= lambda x:x[1])
# print(B)

"""7. Write a Python program to remove duplicates from a list.
"""
# A = [ 2, 3, 4, 6, 5,6,3,5]
# B = []
# C = []
#
# for i in A:
#     if i not in B:
#         B.append(i)
#     elif i not in C:
#         C.append(i)
# print(B)
# print(C)

"""8. Write a Python program to check if a list is empty or not.
"""
# A = []
# if  A:
#     print("not empty")
# else:
#     print("empty")

"""10. Write a Python program to find the list of words that are longer than n from a given list of words."""

# my_list = ["avi","is","greatjnm","person"]
# result = []
#
# for i in my_list:
#     if len(i) > 3:
#         result.append(i)
# print(result)

"""11. Write a Python function that takes two lists and returns True if they have at least one common member."""

# def common_data1(A,B):
#     result = False
#     for i in A:
#         for j in B:
#             if i == j:
#                 return True
#     return result
#
# print(common_data1([1,2,3,4],[5,6,7,8,9]))

"""12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

# my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# A = [0,4,5]
# B = []
# for i in range(len(my_list)):
#     if i not in A:
#         B.append(my_list[i])
# print(B)

"""13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
# Generating a 3x4x6 3D array filled with asterisks
# array_3d = [[[ '*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
#
# # Printing the 3D array
# for layer in array_3d:
#     for row in layer:
#         print(row)
#     print()

"""14. Write a Python program to print the numbers of a specified list after removing even numbers from it."""

# B = []
# for i in range(30+1):
#     if i%2 == 0 :
#         pass
#     else:
#         B.append(i)
# print(B)

"""15. Write a Python program to shuffle and print a specified list.
"""
# import random
#
# # Specified list
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # Shuffling the list
# shuffled_list = original_list.copy()  # Create a copy to preserve the original list
# random.shuffle(shuffled_list)
#
# # Printing the shuffled list
# print("Original List:", original_list)
# print("Shuffled List:", shuffled_list)

"""16. Write a Python program to generate and print a list 
of the first and last 5 elements where the values are square numbers between 1 and 30 (both included)"""

"""19. Write a Python program to calculate the difference between the two lists.
"""
# A=[1,2,3,4,5,6]
# B=[6, 7, 8, 2, 1, 3]
# c=[]
#
# for i in A:
#     if i not in B:
#         c.append(i)
# print(c)

"""20. Write a Python program to access the index of a list.
"""
# A = [1, 2, 3, 4, 5,6]
#
# for i in range(len(A)):
#     print(A[i],i)

"""21. Write a Python program to convert a list of characters into a string.
"""
# A = ["a","S"]
# B = "".join(A)
# print(B)

"""22. Write a Python program to find the index of an item in a specified list.
"""
# A = [1, 2, 3, 4, 5]
# # # # print(A.index(2))
# # #
# B = []
# for i in range(0,len(A)):
#     if A[i]== 0:
#         B.append(i)
# print(B)

"""23. Write a Python program to flatten a shallow list.
"""
# A = [[2,4,3],[1,5,6], [9], [7,9,0]]
# B = []
#
# for i in A:
#     for j in i:
#         B.append(j)
# print(B)

"""24. Write a Python program to append a list to the second list.
o/p=[1, 2, 3, 4, 5, 'avi', 'B', 'C', 'd']
"""
# A = [1, 2, 3, 4, 5]
# B = ["avi","B","C","d"]
# D = A + B
# print(D)
#
# C = []
# for i in A:
#     C.append(i)
# C.extend(B)
# print(C)

"""25. Write a Python program to select an item randomly from a list.
"""

# A = [1, 2, 3, 4, 5]
# for i in A:
#     if "5" in str(i):
#         print(i)
#         break

"""26. Write a Python program to check whether two lists are circularly identical.
"""

# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
#
# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print('Compare list1 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


"""27. Write a Python program to find the second largest number in a list.
"""
# B = A.remove(max(A))
# print(max(A))
# A = [1, 2, 3, 4, 3,5,6]
# C = A[0]
# F = A[0]
# for i in range(len(A)):
#     if C < A[i]:
#        C = A[i]
# for j in range(len(A)):
#     if A[j] > F and A[j] < C:
#         F = A[j]
# print(F)

"""28. Write a Python program to find the second smallest number in a list.
"""
# A = [-20,-16,0,1, 2, 3, 4, 3,5,6]
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

"""29. Write a Python program to get unique values from a list.
"""
# A = [0,1, 2,2,5, 3, 4, 3,5,6]
# B = []
# C = []
#
# for i in A:
#     if i not in B:
#         B.append(i)
#     elif i not in C:
#         C.append(i)
# print(B)
# print(C)

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
#
# print(B)

# A = [1,2,3,4,5,1,5,5]
# B = 0
# for i in range(len(A)):
#     if A[i]==5:
#         B +=1
#
# print(B)

"""31. Write a Python program to count the number of elements in a list within a specified range.
"""
# A = [12, 13, 14, 15, 16, 20]
# B = 0
# for i in A:
#     if 12 <= i <= 16:
#         B += 1
# print(B)
#
# def count_elements_in_range(input_list, start_range, end_range):
#     count = 0
#     for element in input_list:
#         if start_range <= element <= end_range:
#             count += 1
#     return count
#
# # Example usage
# input_list = [12, 5, 8, 20, 15, 30, 25, 10]
# start_range = 12
# end_range = 20
#
# result = count_elements_in_range(input_list, start_range, end_range)
# print(f"Number of elements in the range [{start_range}, {end_range}]: {result}")

""""35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

# A = ['p', 'q']
# B = []
# for j in range(1,6):
#     for i in A:
#       B.append(i+str(j))
# print(B)

"""37. Write a Python program to find common items in two lists.
"""
# A = [1,2,3,4,5,6,7]
# B = [6,7,8,9,10,5]
#
# common_items = []
#
# for i in A:
#     if i in B:
#         common_items.append(i)
# print(common_items)

"""38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""

# A = [0, 1, 2, 3, 4, 5]
# for i in range(0,len(A)-1,2):
#     A[i],A[i+1]=A[i+1],A[i]
#
# print(A)

"""39. Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350"""

# A = [11, 33, 50]
# B = "".join(map(str,A))
# print(B)

# A = [11, 33, 50]
# for i in A:
#     print(i,end="")


"""40. Write a Python program to split a list based on the first character of a word.
"""

# A = ["avi", "ramesh", "chama", "boutkar", "patil"]
# B ={}
#
# for i in A:
#
#     if i[0] in B:
#         B[i[0]].append(i)
#     else:
#         B[i[0]] = i
# print(B)


"""41.  String in Ascending Order"""


# A = ["avi", "ramesh", "chama", "boutkar", "patil"]

# for i in range(0,len(A)):
#     for j in range((i+1),len(A)):
#         if A[i] > A[j]:
#             temp = A[i]
#             A[i] = A[j]
#             A[j] = temp
# print(A)

"""41. Write a Python program to create multiple lists.

O/p = [],[],[],[],[],[],[]
"""

# for i in range(8):
#     A=[]
#     print(A*i)
# "------------------------------------------------"
# A = [i*[] for i in range(10)]
# print(A)

"""42. Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h"""
#
# A = ["a", "b", "c", "d", "e", "f"]
# B = ["d", "e", "f", "h", "g"]
# missing_value =[]
# Additional_value = []
#
# for i in A:
#     if i not in B:
#         missing_value.append(i)
# for j in B:
#     if j not in A:
#         Additional_value.append(j)
#
# print(missing_value)
# print(Additional_value)

"""43. Write a Python program to split a list into different variables.
"""
# A = ["Avi","Patil","Ramesh"]
# v1,v2,v3 =A
# print(v1)

"""44. Write a Python program to generate groups of five consecutive numbers in a list.
o/p=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
"""
# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# A = [[i*5+j for j in range(1,6)] for i in range(5)]
# print(A)
"""-------------------------------------------------------------------------------------------"""
# for i in range(1,20,5):
#     group = range(i,i+5)
#     print(list(group),end=",")

"""45. Write a Python program to convert a pair of values into a sorted unique array.
"""
# L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
#  (7, 8), (9, 10)]
# B = []
#
# for i in L:
#     for j in i:
#         if j not in B:
#             B.append(j)
# print("pair:",B)

"""46. Write a Python program to select the odd items from a list.
"""

# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(B[::2])

"""47. Write a Python program to insert an element before each element of a list.
"""

# A = ["Avi","Patil","Ramesh"]
#
# B = [j for i in A for j in ("C",i)]
# print(B)
#
# for i in A:
#     for j in ("C",i):
#         print(j,end=",")


"""48. Write a Python program to print nested lists (each list on a new line) using the print() function.
"""
# B = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
# v1,v2,v3 = B
# print('\n',v1,'\n',v2,'\n',v3)
#
# for i in B:
#     print(i)

"""49. Write a Python program to convert a list to a list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
 {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]"""

# sample_lists= ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# expected_Output = []
# for name,code in zip(sample_lists[0],sample_lists[1]):
#     dict = {"names":name,"code":code}
#     expected_Output.append(dict)
#
# for i in expected_Output:
#     print(i)

"""50. Write a Python program to sort a list of nested dictionaries.
"""
# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# A = sorted(my_list,key=lambda x:x['key']['subkey'],reverse=True)
# print(A)

"""Write a Python program to split a list every Nth element.
i/p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

O/p = ['a', 'd', 'g', 'j', 'm'],['b', 'e', 'h', 'k', 'n'],['c', 'f', 'i', 'l'],
"""

# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#
# A = [C[i::3] for i in range(3)]
# print(A)

# for i in range(3):
#     print(C[i::3],end=",")

"""Write a Python program to concatenate elements of a list.
"""

# color1 = ['red', 'green', 'orange']
# for i in color1:
#     print(i,end="")
#
# print("".join(color1))

"""-------------------------------------------------------------------------------------"""
# A = [1,2,4,6,8,9]
# for i in range(min(A),max(A)):
#     if i not in A:
#         print(i)

"""Write a Python program to check if all items in a given list of strings are equal to a given string.
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green","orange"]
o/p = "False"
o/p = "True"
"""

# color1 = ["green", "orange", "black", "white"]
# color2 = ["green1"]
#
# def my_fun(n,m):
#     result = False
#     for i in n:
#         for j in m:
#             if j in i:
#                 return True
#     return result
# obj = my_fun(color1,color2)
# print(obj)


"""58. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]"""

# A = [1, 3, 5, 7, 9, 10]
# B = [2, 4, 6, 8]
# C = A.pop()
# A.extend(B)
# print(A)
"""------------------------------------------------------"""
# A[-1:]=B
# print(A)

"""59. Write a Python program to check whether the n-th element exists in a given list.
"""
# def check(n):
#     if n in range(0,10):
#         print("True")
#     else:
#         print("False")
# check(11)

"""60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
"""
# x = [(4, 1), (1, 2), (6, 0)]
# A = min(x,key= lambda y:(y[1],y[0]))
# print(A)
"------------------------------------------------------------------------------------"
# x = [(4, 1), (1, 2), (6, 0)]
#
# # Initialize the minimum tuple with the first element of the list
# min_tuple = x[0]
#
# # Iterate through the remaining elements of the list
# for element in x[1:]:
#     if (element[1],element[0])<(min_tuple[1],min_tuple[0]):
#         min_tuple = element
# print(min_tuple)

"""61. Write a Python program to create a list of empty dictionaries.
"""
# A= [{} for i in range(1,10)]
# print(A)

"""62. Write a Python program to print a list of space-separated elements.
i/p=[1,2,3,4,5],  o/p-1 2 3 4 5"""

# A = [1,2,3,4,5]
# print(*A)

"""63. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']"""
# A = [1,2,3,4]
# B = "emp"
# C = []
#
# for i in A:
#     C.append("emp"+str(i))
# print(C)

"""64. Write a Python program to iterate over two lists simultaneously.
i/p : 
num = [1, 2, 3]
color = ['red', 'white', 'black']

o/p = 
1 red
2 white
3 black
"""
# num = [1, 2, 3]
# color = ['red', 'white', 'black']
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
# B= []
# C = []
# for i in A:
#     if 0!= i:
#         B.append(i)
#     else:
#         C.append(i)
# B.extend(C)
# print(B)

"""66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]"""

# A = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# B = max(A,key=lambda x:(x[0],x[-1]))
# print(B)

# num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(max(num, key=sum))

"""67. Write a Python program to find all the values in a list that are greater than a specified number.
i/p = [0,1,2,3,4,5,6,7,8,9]
n=5
o/p=[6,7,8,9]
"""

# for i in range(0,10):
#     if 5 <= i:
#         print(i+1)

"""68. Write a Python program to extend a list without appending.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]"""

# A = [10, 20, 30]
# B = [40, 50, 60]
# # # A[:0]=B
# # # print(A)
# # """----------------------"""
# B.extend(A)
# print(B)
#
# for i,j in zip(A,B):
#     print(i,j,end=",")

"""69. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]"""

# Sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# lis1=[]
#
# for i in Sample_list:
#     if i not in lis1:
#         lis1.append(i)
# print(lis1)

"""70. Write a Python program to find items starting with a specific character from a list.
Expected Output:
Original list:
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]"""

# B = []
# A = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
#
# for i in A:
#     if i[0] == "s":
#         B.append(i)
#
# print(B)

"""71. Write a Python program to check whether all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False"""

# A = [{},{},{}]
#
# for i in A:
#     if len(i)>0:
#         print("False")
#         break
#     else:
#         print("True")
#         break

"""72. Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]"""
#
# A = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# B = []
# for i in A:
#     if isinstance(i,list):
#         for j in i:
#             B.append(j)
#     else:
#         B.append(i)
# print(B)



"""73. Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]"""

# A = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# B =[]
# for i in A:
#     if i not in B:
#         B.append(i)
# print(B)

"""74. Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]"""

# from itertools import groupby
#
# original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# A = [list(group) for key,group in groupby(original_list)]
# print(A)

"""75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or
a given list of characters. Original list:[1, 1, 2, 3, 4, 4.3, 5, 1]
List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
Original String:
automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]"""
# A =[1, 1, 2, 3, 4, 4.3, 5, 1]
# B = {}
#
# for i in A:
#     if i in B:
#         B[i] +=1
#     else:
#         B[i]=1
# print(B)
#

"""STRING"""
































