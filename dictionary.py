"""1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""
from collections import Counter

# sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
#
# A = dict(sorted(sample_dict.items(),key=lambda  x:x[1],reverse=True))
# print(A)

"""2. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""

# A = {0: 10, 1: 20}
# A.update({2:30})
# print(A)

"""3. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""
# A = [{1:10, 2:20},{3:30, 4:40},{5:50,6:60}]
# B = {}
# for i in A:
#     B.update(i)
# print(B)

"""4. Write a Python script to check whether a given key already exists in a dictionary.
"""
# A = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for i in A:
#     if "5" in str(i):
#         print(True)

"""5. Write a Python program to iterate over dictionaries using for loops."""
# A = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for dict_key,dict_value in A.items():
#     print(dict_key,"-",dict_value)

"""6. Write a Python script to generate and print a dictionary that 
contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

# A = {i:i*i for i in range(1,5+1)}
# print(A)

"""7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and
 the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

# A = {i:i*i for i in range(1,16)}
# print(A)

"""8. Write a Python script to merge two Python dictionaries."""
# A = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# B = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# C = A.copy()
# B.update(C)
# print(B)
#
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)

"""9. Write a Python program to iterate over dictionaries using for loops."""
# B = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# for i,j in B.items():
#     print(i,j)

"""10. Write a Python program to sum all the items in a dictionary."""
# B = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# A = 0
# for i,j in B.items():
#     A += j
# print(A)

"""11. Write a Python program to multiply all the items in a dictionary."""
# B = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# A = 1
# for i,j in B.items():
#     A *= j
# print(A)

"""12. Write a Python program to remove a key from a dictionary."""
# B = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# if 2 in B:
#     del B[2]
# print(B)

"""13. Write a Python program to map two lists into a dictionary."""
# A = [1,2,3,4,5]
# B = [4,5,6,7,8]
#
# for i,j in zip(A,B):
#     C = {i:j}
#     print(C,end=",")

# C= dict(zip(A,B))
# print(C)

"""14. Write a Python program to sort a given dictionary by key."""
# B = {2: 1, 3: 4, 5: 9, 1: 16, 4: 25}
# A = sorted(B.items(),key= lambda  x:x[0])
# print(dict(A))

"""15. Write a Python program to get the maximum and minimum values of a dictionary."""
# B = {2: 1, 3: 4, 5: 9, 1: 16, 4: 25}
#
# A = max(B.keys(),key= lambda x:B[x])
# print(A)
#
# C = min(B.keys(),key = lambda x:B[x])
# print(C)

"""16. Write a Python program to get a dictionary from an object's fields."""


# class my_class():
#     def __init__(self):
#         self.x = "red"
#         self.y = "white"
#
#
# obj = my_class()
# print(obj.__dict__)

"""17. Write a Python program to remove duplicates from the dictionary."""
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
#
# result = {}
#
# for i,j in student_data.items():
#     if j not in result.values():
#         result[i] = j
# print(result)

"""18. Write a Python program to check if a dictionary is empty or not."""
# A = {1:2}
# if A:
#     print("not empty")
# else:
#     print("empty")

"""19. Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})"""

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# A = {}

# for i,j in d1.items():
#     if i in A:
#         A[i] += j
#     else:
#         A[i] = j
#
# for k,l in d2.items():
#     if k in A:
#         A[k] += l
#     else:
#         A[k] = l
#
# print(A)

"""20. Write a Python program to print all distinct values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

# A = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# B = set()
# for i in A:
#     for j in i.values():
#         B.add(j)
# print(B)

"""21. Write a Python program to create and display all combinations of letters, selecting each letter 
from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd"""

"""22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary."""

# B = {2: 1, 3: 4, 5: 9, 1: 16, 4: 25}
#
# A = sorted(B.items(),key=lambda x:x[1],reverse=True)
# C = A[:3]
# print(dict(C))

"""23. Write a Python program to combine values in a list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})"""

# A = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# B = Counter()
# for i in A:
#     B[i['item']] += i['amount']
# print(B)

"""24. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"""

# A = 'w3resource'
# B = {}
#
# for i in A:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
# print(B)






