"""
2) WAP to find first 5 even numbers using lamda function
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.wpewebkit.service import Service

# A =  filter(lambda x: x%2==0,range(10))
# print(list(A))
#
# for i in range(10):
#     if i%2==1:
#         print(i)

"""
3) How many time "t" is coming on string
"""
#
# A = "avi at time having tea"
#
# B =[]
# for i in A:
#     if i == "t":
#         B.append(i)
# print(len(B))
#
# A = "avi at time having tea"
#
# B = 0
# for i in A:
#     if i == "t":
#         B += 1
# print(len(B))

"""
4) This program reads the contents of the file "Interview.txt,counts the number of uppercase letters in 
the file,and then prints the last character of the file and the total count of uppercase letters.
"""
# B = 0
# with open("Interview.text","r") as r:
#     upper_case = r.read()
#     for i in upper_case:
#         if i.isupper():
#             print(i)
#             B += 1
# print(B)

"""
5) Reverse the string
"""

# A = "avi at time having tea"
#
# B = reversed(A)
# print(list(B))
# C=""
#
# for i in A:
#     print(i)
#     C = i + C
# print(C)


"""
6) print table of 5
"""

# for i in range(10+1):
#     print(f"5*{i} = ",i*5)

"""
7) swap value
"""
# a=5
# b=4
#
# a,b=b,a
# print(a)
# print(b)

""" 
8) Find the count of numbers containing '6' in it from the sequence 1 to 1000.
Also print the numbers
"""
# count = 0
#
# for  i in range(1000+1):
#     if "6" in str(i):
#         count += 1
# print(count)


"""
9) count of the value of occurance
"""
# A = input("Enter trhe value:")


# InputStr = "aaaabbbccccc111111@"
# dict = {}
# for i in InputStr:
#      # if i already appears as key in dict, increment the count
#     if i in dict:
#         dict[i] += 1
#
#      # else i appears for the first time, add to dict
#     else:
#         dict[i] = 1
# print(dict)

"""
10) The provided code generates a list result containing the missing integers from 
the range between the minimum and maximum values of the inputs list.
"""

# A = [1,3,7,8,9]
# B = []
# for i in range(min(A), max(A)):
#     if i not in A:
#         B.append(i)
# print(B)

"""
11) Input :- "i am the input"
     Output:- "the input am i"
"""
# Input = "i am the input"
# C = Input.split()
# A = C[2::]
# B = C[:-2]
# reverse_B = reversed(B)
# s = tuple(A) + tuple(reverse_B)
# joined = " ".join(s)
# print(joined)

"""
12) Sort the dictionary on basis of values 
"""

# A = {1:10, 2:13, 3:14, 4:15, 5:9}
# sort_A = sorted(A.items())
# print(sort_A)
#
# B = sorted(sort_A, key= lambda x:x[1] )
# print(B)

""" 
13) how will be two mandatory and two optional parameter in function
"""
# def fun(A,B,C= None,D=None):
#     print(A,B,C,D)
#
# fun(1,2,3,4)

"""""
14)Input array=[13,0,17,0,5,0,9]
output = [13,17,5,9,0,0,0]
"""
# Input_array=[13,0,17,0,5,0,9]
# B= []
#
# for i in Input_array:
#     if i != 0:
#         B.append(i)
# C = Input_array.count(0)
# B.extend(3 * [0])
# print(B)

# service_obj = Service("")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("")
#
# driver.find_element(By.ID,"").send_keys()

"""16) You and your family are at restaurant to have dinner at happyhour offer.you get code coupon
code at this offer.if it matches "happy" word then  you will get free deserts.so find out how many free deserts
you will get for following code

example coupon_code= "happyishappy"
expected output = 2"""

# def dessert(coupon):
#     if  "happyishappy" in coupon:
#         no_occurance = coupon.count("happyishappy")
#         return no_occurance
#     else:
#         return 0

"""write a python program to multiply elements of two list save in new list"""

# string = "mississippi"
# p = ""
#
# A= set(string)
# print(str(A))
#
# for i in string:
#     if i not in p:
#         p= p + i
# print(p)

# strng_inp = "iworkatcelestialsystems"
# duplicate_chars = []
#
# # Approach 1 (Using Empty list)
# for i in strng_inp:
#     if strng_inp.count(i) > 1:
#         if i not in duplicate_chars:
#            duplicate_chars.append(i)
#
# print("".join(duplicate_chars))

# for a in strng_inp:
#     if a not in duplicate_chars:
#         duplicate_chars= duplicate_chars + a
# print(duplicate_chars)

# str = "great is india"
#
# lis = str.split()
# print(str)
# op = lis[::-1]
# print(op)
# result = " ".join(op)
# print(result)

# list = [23,45,67,2,3,4,5]
# print(list)
# # 1st approach
# # removing maximum element
#
# output = list.remove(max(list))
#
# print(max(list))
#
# Output = list.sort()

#
# print(max(list))

m = "*"
print(f"\t\t {m} \n\t{m}\t{m}\t{m} \n{m}\t{m}\t{m}\t{m}\t{m} " )
