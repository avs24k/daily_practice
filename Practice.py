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


# employee_data.py

# employees = { 101: "John Doe",102: "Jane Smith",103: "Michael Johnson",104: "Emily Brown"}
#
# key= [101,102,103]
# for keys in key:
#     print(employees[keys])


"""
2) WAP to find first 5 even numbers using lamda function
"""

# A = filter(lambda InputStr: InputStr%2==0,range(10))
# print(list(A))

"""
3) How many time "t" is coming on string
"""
# stri = "india is the best country"
# count = 0
#
# for i in stri:
#     if i == "t":
#         count = count + 1
#
# print("frequency of letter t is :",count)


"""
4) This program reads the contents of the file "Interview.txt,counts the number of uppercase letters in 
the file,and then prints the last character of the file and the total count of uppercase letters.
"""

# count = 0
# with open('Interview.text','r') as text_file:
#     upper_case = text_file.read()
#     for i in upper_case:
#         if i.isupper():
#             print(i,end=",")
#             count = count + 1
# print("\ntotal number of upper case is ",count)


"""5) Reverse the string"""

# strng = "i love my India"
# s = ""
# for i in strng:
#     s = i + s
# print(s)

# OR

# strng = "i love my India"
# A = reversed(strng)
# B=tuple(A)
# C =",".join(B)
# print(C)


"""
6) print table of 5
"""
# A = 5
# for i in range(10+1):
#     B = i * A
#     print("5 *",i,"=",B)

"""
7) swap value
"""
# x=5
# y=6
# x,y=y,x
# print(x,y)

""" 
8) Find the count of numbers containing '6' in it from the sequence 1 to 1000.
Also print the numbers
"""

# count = 0
# for i in range(1000+1):
#     if "6" in str(i):
#         count= count +1
# print(count)


"""
9) count of the value of occurance
"""

# approach:1

# str = "you are welcome to python programming are welcome to python programming"
# str_split = str.split()
# dict = {}
# for i in str_split:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i]= 1
# print(dict)


# approach:2
# str = "you are welcome to python programming are welcome to python programming"
# str_split = str.split()
# count = 0
# for i in str_split:
#     count = str_split.count(i)
#     print(i,count)

# approach:3
# from collections import Counter
# A = Counter(str_split)
# print(A)


# approach:4

# InputStr = "aaaabbbccccc111111@"
# dict = {}
# for i in InputStr:
#     # if I already appear as key in dict, increment the count
#     if i in dict:
#         dict[i] += 1
#
#     # else i appears for the first time, add to dict
#     else:
#         dict[i] = 1

# printing result
# print(dict)

"""
10) The provided code generates a list result containing the missing integers from 
the range between the minimum and maximum values of the inputs list.
"""

# inputs = [6,3,5,1,2,10]
# A = []
#
# for i in range(min(inputs),max(inputs)+1):
#     if i not in inputs:
#         A.append(i)
# print(A)

"""
11) Input :- "i am the input"
     Output:- "the input am i"
"""

# s="I am the input"
# split_s= s.split()
# B = split_s[2::]
# C= split_s[:-2]
# reverse_C=reversed(C)
# S = tuple(B) + tuple(reverse_C)
# join_String =",".join(S)
# print(T)

"""
12) Sort the dictionary on basis of values 
"""
# #approch1 :
# dict1 = {'a':5, 'b':3, 'c':4, 'd':1, 'e':2}
# sort_value = sorted(dict1.items())
# A = sorted(sort_value,key=lambda items:items[1])
# print(A)
#
# #approch 2:
#
# students = [('Alice', 25), ('Bob', 20), ('Charlie', 18), ('David', 22)]
# B= sorted(students,key=lambda x:x[0])  #sorted based on name, key= means ('Alice', 25) and ('Bob', 20)
# print(B)
#
# #approch 3:
# people = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 18},
#     {'name': 'David', 'age': 22}
# ]
#
# C= sorted(people,key = lambda x:x['age']) #sorted by age
# print(C)

""" 
13) how will be two mandatory and two optional paramter in function
"""
# def sum(a,b,c=None,d=None):
#     return a + b + c + d
# print(sum(2,3,c=4,d=10))

"""
14)Input array=[13,0,17,0,5,0,9]
output = [13,17,5,9,0,0,0]
"""
# array=[13,0,17,0,5,0,9]
#
# B=[v for v in array if v != 0]
# no_Xero = array.count(0) #this will give count of zero in array i.e.3
# B.extend([0]*no_Xero) ##extend will add the value in the end of list, for extend values should be in list
# print(B)

"""
15) Syste Info
"""

# import sys
# import os
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# cwd = os.getcwd()
# print(cwd)
# print(sys.)

"""16) You and your family are at restaurant to have dinner at happyhour offer.you get code coupon
code at this offer.if it matches "happy" word then  you will get free deserts.so find out how many free deserts
you will get for following code

example coupon_code= "happyishappy"
expected output = 2"""

# approach:1
# def count_free_deserts(coupon_code):
#     # Check if the word "happy" is present in the coupon code
#     if "happy" in coupon_code:
#         # Count the occurrences of the word "happy" in the coupon code
#         num_occurrences = coupon_code.count("happy")
#         return num_occurrences
#     else:
#         # If the word "happy" is not present, no free desserts
#         return 0
#
# # Example usage:
# coupon_code = input("Enter the coupon code: ")
# num_free_deserts = count_free_deserts(coupon_code)
# print(f"You get {num_free_deserts} free dessert(s)!")
#
# #approach:2
# coupon_code = "happyishappy"
# A = [
#     {"Dish": "Biryani", "code": "happyishappy"},
#     {"Dish": "Pulao", "code": "No_code"},
#     {"Dish": "chay", "code": "happyishappy"}
# ]

# for i in A:
#     if coupon_code == i["code"]:
#         B=i["code"].count(coupon_code)
#         print(B)

"""write a python program to multiply elements of two list save in new list"""
# list1 = [2, 4, 6, 8, 10]
# list2 = [2, 3, 4, 5, 6]
#
# res_list=[]
#
# for i in range(0, len(list1)):
#     res_list.append(list1[i] * list2[i])
# print(res_list)

# list1 = [2, 4, 6, 8, 10]
# list2 = [2, 3, 4, 5, 6]
#
# res_list=[]
#
# for i,j in zip(list1,list2):
#     res_list.append(i*j)
# print(res_list)

"""write python program to swap odd index numbers with even index numbers"""

# list = [1,2,3,4,5,6,7,8,9,10]
# list[0::2],list[1::2]=list[1::2],list[0::2]
#
# print(list)

""" remove spaces from input string without inbuilt function.
input = "remove spaCes from this stRing 123 "
output = "removespacesfromthisstring123" """

# input = "remove spaces from this string 123 "
#
# result = ''
# # iterating the string
# for i in input:
#     # if the character is not a space
#     if i != ' ':
#         result = result + i
# print("String after removing the spaces :", result)
#
# =======================================================================================================================

"""Python Program To Remove Duplicates From A Given String:"mississippi"""
# string = "mississippi"
# p = ""
# for char in string:
#     if char not in p:
#         p = p + char
# print(p)

"""Write a Python program to get a string from a given string where all occurrences of its first
char have been
    return max_char

---------------------------------------------------------------------------------
changed to '$', except the first char itself.
Sample String : 'restartthecomputer'
# Expected Result : 'resta$$$h$comp$$$'"""

# sample_string = 'restartthecomputer'
#
# lis = []
# s= 'restartthecomputer'
# for ch in s:
#     if ch in lis:
#         lis.append('$')
#     else:
#         lis.append(ch)
# print(''.join(lis))

"""------------------------------------------------------------------------------
"""
# input = "restartthecomputer"
# dup_str = ""
#
# for i in input:
#     if i not in dup_str:
#         dup_str = dup_str + i
#     else:
#         dup_str= dup_str + "$"
# print(dup_str)

"""------------------------------------------------------------------------------------
""""""python program to display Maximum frequency character in String"""

# def max_freq_char(ip_str):
#
#     freq = {}
#
#     for i in ip_str:
#         if i in freq:
#           freq[i] = freq[i] + 1
#         else:
#             freq[i] = 1
#     max_char = max(freq.items(),key= lambda x:x[0])
#     return max_char
# print(max_freq_char('iworkatcelestialsystems'))

"""Find all duplicate character of a string “iworkatcelestialsystems” Given any string,
the script should find all the duplicate characters which are similar to each other
 and print the character.

Example: “iworkatcelestialsystems”
Output: etials"""

# strng_inp = "iworkatcelestialsystems"
# duplicate_chars = []
#
# # Approach 1 (Using Empty list)
# for i in strng_inp:
#     if strng_inp.count(i) > 1:
#         print(i)
#         if i not in duplicate_chars:
#            duplicate_chars.append(i)
#
# print("".join(duplicate_chars))
#
#
# # Approach 2 (using Empty String)
# duplicate = ""
# for i in strng_inp:
#     if strng_inp.count(i)>1:
#         if i not in duplicate:
#             duplicate= duplicate+ i
# print(duplicate)

"""-----------------------------------------------------------------------------------------------------
"""
"""
Given an array, write a script to find Second largest number, without using in -built functions

Ex: [30, 15, 25, 20, 5]
Output: second Largest number is 25
"""

# input = [30,15,25,20,5]
# temp = 0
# for i in range(0,len(input)):
#     for j in range(i+1,len(input)):
#         if input[i] > input[j]:
#             temp = input[i]
#             input[i] = input[j]
#             input[j] = temp
# for i in  range(1,len(input)):
#     print(input[i],end=",")
# #
# print("the second largest number is ",input[-2])


"""
In the Gregorian calendar, three conditions are used to identify leap years:
The yearcan be evenly divided by 4, is a leap year, unless: The year can be evenly divided by 100, 
it is NOT a leap year, unless: The
year is also evenly divisible by 400. Then it is a leap year.This means that in the Gregorian calendar, the
years 2000 and 2400 are leap years,while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Given a
year, determine whether it is a leap year.If it is a leap year, return the Boolean True, otherwise return False.
"""

# def find_leap_year(year):
#     leap = False
#     if year % 400 == 0:
#         leap = True
#     elif year % 4 ==0 and year != 100:
#         leap = True
#     else:
#         return leap
#
# year = int(input("enter year : "))
# print(find_leap_year(year))
#

# list = [23,45,87,90,65]

"----------------------------------------------------------------------------------------------------"
# str = "great is india"
#
# lis = str.split()
# print(str)
# op = lis[::-1]
# print(op)
# result = " ".join(op)
# print(result)
#
# number = input("Enter the number")
# temp =number
# rever = 0

# while number > 0:
#     digit = number % 10
#     rever = rever * 10 + digit
#     number = number // 10
# if temp == rever:
#     print("this number is palindrome")
# else:
#     print("this is not palindrome")


# list = [1,2,3,4,5,6,7]
#
# list.sort()
#
# print("the second element of list is ",list[-2])
#
#
# list = [23,45,5,34,76,56]
#
# list.remove(max(list))
#
# print(max(list))


"""to find 2nd max element of list"""

# list = [23,45,67,2,3,4,5]
# print(list)
# # 1st approach
# # removing maximum element
#
# output = list.remove(max(list))
#
# print(max(list))

# 2nd approach sorting the list
# Output = list.sort()
#
# print(max(list))


# ========================================================================================================================
"""Calculate the sum of all numbers from 1 to a given number"""

# n = int(input("Enter the Number"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"the sum of numbers upto {n} is :",sum)

# ===========================================================================================================================
"""Write a program to print multiplication table of a given number"""
# num = int(input("enter the number"))
#
# for i in range(1,11):
#      print(f"{num} x {i} :",num * i )


# ======================================================================================================================

# def triangle_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* " ,end= "")
#         print("\n")
#
#     for i in range(1,n+1):
#         print(" " * (n-i) + " *" * i)
#
#
#
#
# n = int(input("enter rows"))
# triangle_pattern(n)

"-----------------------------------------------------------------------------------------------------------"
