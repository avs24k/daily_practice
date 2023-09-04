#
# """find missing element"""
# A = [1,2,3,4,5,6,8]
# #
# B = None
# C = []
# #
# for i in range(len(A)+1):
#     if i not in A:
#         B = i
# print(B)
#
# B = [i for i in A if i not in C ]
# print(C)
# #
# # A = [1, 2, 3, 4, 5, 6, 8]
# #
# # missing_element = None
# # for i in range(1, len(A) + 2):  # Range includes 1 to len(A)+1 to cover the missing element
# #     if i not in A:
# #         missing_element = i
# #         break
# #
# # print("Missing element:", missing_element)

"""find the sum of elements
A = [1, 2, 3, 4, 5], o/p = 1+2+3+4+5=15
"""

# A = [1, 2, 3, 4, 5]
# B = 0
# for i in range(1,len(A)+1):
#     B += i
#
# print(B)

"""find the 2nd maximum number"""
# A = [1, 2, 3, 10,11, 5]
# A.sort()
# A.remove(max(A))
# print(A[-1])

"""find maximum number"""
# A = [1, 2, 3, 10,11, 5]
# B = sorted(A)
# print(B[-1])

# A = [30, 2, 3,40, 10, 5]
# max = A[0]

# for i in range(1,len(A)):
#     if A[i]> max:
#         max = A[i]
# print(max)

# for i in A:
#     if i > max:
#         max = i
# print("max value:",max)

"""length of the list"""

# A = [30, 2, 3,40, 10, 5]
#with built in function
#print(len(A))

#without built in functon
# count = 0
# for i in A:
#     count = count + 1
# print(count)

"""swap first and last element of list
i/p = [1, 2, 3] , o/p = [3, 2, 1]
"""
# ip = [1, 2, 4, 3]
#
# ip[0],ip[-1]= ip[-1],ip[0]
# print(ip)
#
# input_list = [1, 2,4, 3]
# if len(input_list) >= 2:  # Ensure there are at least 2 elements in the list
#     input_list[0], input_list[-1] = input_list[-1], input_list[0]
#
# print(input_list)

"""swap any two elements in list
i/p = [1,2,3,4,5,6], o/p=[1,2,5,4,3,6]
"""
# ip = [1,2,3,4,5,6]
#
# pos1,pos2 = 2,-1
#
# ip[pos1],ip[pos2]=ip[pos2],ip[pos1]
# print(ip)

"""remove Nth occurrence of the given word 
input = ["avinash","is","great"]
word = "is", N= 2
o/p = ["avinash","great"]
"""
# input = ["avinash","is","great"]
# N = 1
# input.remove(input[N])
# print(input)

"""Find an element in list"""
# ip = [1,2,3,4,4,4,4,4,5,6,6]
# ele = 0
# for i in ip:
#     if "4" in str(i):
#         ele = ele +1
# print(ele)

"""reverse a list"""
# ip = [1, 2, 3, 4, 5, 6, 6]
# A = ip[::-1]
# print(A)

"""how to copy a list"""
# ip = [1, 2, 3, 4, 5, 6, 6]
#
# cp= []
# cp1 = []
# cp3 = ip[:]
# cp4 = list(ip)
#
# cp.append(ip)
# cp1.extend(ip)
#
# print(cp)
# print(cp1)
# print(cp3)
# print(cp4)

"""count an occurrence of an element in list"""
# ip = [1, 2, 3, 3, 3, 3, 4, 5, 6, 6]
# op = {}
#
# for i in ip:
#     if i in op:
#         op[i] += 1
#     else:
#         op[i]=1
#
# print(op)

"""find the sum of list"""
# ip = [1, 2, 3, 4, 5, 6, 6]
# A = sum(ip)
# print(A)
#
# op= 0
# for i in range(0,len(ip)):
#     op = op + ip[i]
#
# print(op)

"""multiply all number in list"""
# ip = [1, 2, 3, 4, 5, 6, 6]
# op= 1
#
# for i in range(1,len(ip)):
#     op = op * ip[i]
#
# print(op)

"""min and largest value """
# ip = [1, 2, 3, 4,7, 5, 6, 6]

"""------------------------------------------------------------------------------------------"""
# ip.sort()
# print("min",ip[0])
# print("max",ip[-1])
#

"""------------------------------------------------------------------------------------------"""

# count = ip[0]
# for i in ip:
#     if ip[i] > count:
#         count = ip[i]
# print(count)

"""Python | Ways to find length of list"""

# string = "avinash is best"
# count = 0
#
# for i in string:
#     count = count+1
# print(count)

"""Maximum of two numbers in Python"""
# ip = [1, 2, 3, 4,7, 8,5, 6, 6]
# count = ip[0]
# second_max = ip[0]
# for i in range(len(ip)):
#     if ip[i]>count:
#         count=ip[i]
#     elif ip[i]> second_max and ip[i]<count:
#         second_max = ip[i]
#
# print("max digit:",count)
# print("second max digit:",second_max)

"""Python | Ways to check if element exists in list"""
# ip = [1, 2, 3, 4,7, 8,5, 6, 6]
# check = 0
#
# for i in ip:
#     if "6" in str(i):
#         check+=1
# print(check)

"""Python program to count Even and Odd numbers in a List"""
# ip = [1, 2, 3, 4,7, 8,5, 6, 6]
# even = 0
# odd = 0
#
# for i in ip:
#     if i % 2 ==0:
#         even +=1
#     elif i % 1 == 0:
#         odd +=1
# print("total count of even values:",even)
# print("total count of odd values:",odd)

"""python program to remove all even number"""
# ip = [1, 2, 3, 4,7, 8,5, 6, 6]
#
# for i in ip:
#     if i % 2 ==0:
#         ip.remove(i)
#
# print(ip)

"""print duplicate from list"""

# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# duplicate = []
# unique = []
#
# for i in list:
#     if i not in duplicate:
#         duplicate.append(i)
#     elif i not in unique:
#         unique.append(i)
# print(duplicate)
# print(unique)

"""missing values"""

# ip = [1, 2, 4,8,6]
#
# count = []
#
# for i in range(1,len(ip)+4):
#     if i not in ip:
#         count.append(i)
# print(count)

"""remove nth number of word"""

# mylist= ["geeks", "for", "geeks"]
# word="geeks"
# n= 2
# count = 0
#
# for i in range(0,len(mylist)):
#     if mylist[i] == word:
#         count = 1 + count
#         if count == n:
#             del mylist[i]
#
# print(mylist)

"""13- Program to count the occurrence of an element in a list?
Input: mylist=[15,6,7,10,12,10,20,10]
x=10
Output: 3
10 appeared 3 times in the given list"""

# mylist=[15,6,7,10,12,10,20,10]
# count = 0
#
# for i in mylist:
#     if "10" in str(i):
#         count += 1
# print(count)

"""21- Print HELLO for the given string “AHCECLWLXO”.
# """
# str = "AHCECLWLXO"
# print(str[1::2])

# str1 = "ahceclwlxo"
# print(str1[1::2].upper())

"""24- Ask the user to enter two number (int) a and b, return true if
a) either one is 6

b) or if their sum is 6

c) or the difference is 6"""

# def num(a,b):
#     if a==b==6 or a + b == 6 or a-b==6:
#         return True
#     else:
#         return False
# obj =num(2,6)
# print(obj)

"""26- Given 2 strings, a and b, return a new string made of the first char of a and the last char of b. 
If either string is length 0, use ‘@’ for its missing char.
Ex. (“last”, “chars”) → “ls”
Ex. (“yo”, “java”) → “ya”"""

# def my_string(my_string1,my_string2):
#     print(my_string1[0] + my_string2[-1])
#
# my_string("avi","patil")
#
#
# def fristlast(s1,s2):
#     if len(s1)>0 and len(s2)>0:
#         return s1[0]+s2[-1]
# #elif len(s1<0) or len(s2)<0:
#     elif len(s1)>0 and len(s2)<=0:
#         return str(s1[0])+'@'
#     elif len(s1)<=0 and len(s2)>0:
#         return '@'+str(s2[-1])
#     elif len(s1)<=0 and len(s2)<=0:
#         return '@@'
# print(fristlast('last','chars'))

"""27- Ask the user to input a string and an integer n, return a string made of the first and last n chars from the string. The string length will be at least n.
Ex1:(“Hello”, 2) → “Helo”
Ex2:(“Chocolate”, 3) → “Choate”
Ex3:(“Chocolate”, 1) → “Ce”
Ex4:(“Hello”, 1) → “Ho”"""

# def my_string(my_strig1,num):
#     print(my_strig1[:num] + my_strig1[-num:])
#
# my_string("avinash",3)

"""28- Given a string, return true if “bad” appears starting at index 0 or 1 in the string, 
The string may be any length, including 0.
Ex1:(“badxx”) → true
Ex2:(“xbadxx”) → true
Ex3:(“xxbadxx”) → false"""


# def practive2(s):
#     if s.index('bad')==0 or s.index('bad')==1:
#         return True
#     else:
#      return False
#
# print(practive2("badxx"))
# print(practive2("xbadxx"))
# print(practive2("xxbadxx"))

"""29- Ask user to input a string, return a new string where for every char in the original, there are two chars.
Ex1: (“The”) → “TThhee”
Ex2: (“AAbb”) → “AAAAbbbb”
Ex3: (“Hi-There”) → “HHii–TThheerree”"""

# my_string = "The"
# A = list(my_string)
# C = []
# for i in range(0,len(A)):
#     B = A[i]*2
#     C.append(B)
# D = "".join(C)
# print(D)

"""30- Return the number of times that the string “code” appears anywhere in the given string
Ex1: (“aaacodebbb”) → 1
Ex2: (“codexxcode”) → 2
Ex3: (“codexxcodexxcode”) → 3"""

# string = "codexxcodexxcode"
#
# print(string.count("code"))

"""31- For the given below strings, Return true if the string “cat” and “dog” appear the same number of times.
Ex1: (“catdog”) → true
Ex2:(“catcat”) → false
Ex3:(“1cat1cadodog”) → true
Ex4:(“catnotdog”) → true"""

# animal = "catcatcat"
#
# if animal.count("cat") > 1:
#     print("True")
# else:
#     print("False")

"""32- Return the sum of the numbers in the array,a: Return 0 for an empty array.
b: Number 13 is very unlucky, so it does not count and numbers that 
come immediately after a 13 also do not count."""

"""33- Given a number n, create and return a new int array of length n, containing the numbers 0, 1, 2, … n-1.
The given n may be 0, in which case just return a length 0 array.
Ex1:(4) → [0, 1, 2, 3]
Ex2:(1) → [0]
Ex3:(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""

# n= 10
# b = []
# for i in range(1,n+1):
#     b.append(i)
# print(b)

"""
35- Return the sum of the numbers in the array, except ignore sections of numbers starting with a 
6 and extending to the next 7.
(every 6 will be followed by at least one 7). Return 0 for no numbers."""

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

for i in range(len(A)):
    if A[i]!=6:
     count = count + i

print(count)