"""Write a Python program that accepts the user's first and last name and prints
them in reverse order with a space between them."""
# import copy

# #approach - 1
# First_name = ["Avinash"]
# Last_name = ["Patil"]
# Full_name = First_name+Last_name
# print(Full_name[::-1])
#
# #approach2
# def full_name(*args):
#
#     print(args[::-1])
#
# obj=full_name("Avinash","PAtil")

"""6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates 
a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"""

# input_data = input("Enter sequence of comma-separated numbers:")
#
# list_num = input_data.split(",")
# tuple_num = tuple(input_data.split(","))
# print(list_num)
# print(tuple_num)

"""7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java"""

# input_data = input("Enter file name with Extension:")
#
# split_file  = input_data.split(".")
# sort_split = list(split_file)
# print("the extensions of file is :",sort_split[-1])
#
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))

"""8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]"""

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0])
# print(color_list[-1])

"""Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014"""

# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)

"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615"""

"""1st approach"""
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)
#
# """2nd approach"""
# n = int(input("Enter an integer (n): "))
#
# # Calculate nn and nnn by concatenating strings
# nn = int(str(n) + str(n))
# nnn = int(str(n) + str(n) + str(n))
# # Calculate the final result
# result = n + nn + nnn
# print("Result:", result)

"""12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module."""

# import calendar
#
# A = calendar.calendar(23)
# print(A)

"""16. Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference."""

# A = 20
#
# if A >= 17:
#     B= abs(A-17)
#     print(B*2)
# else:
#     C = abs(A-17)
#     print(C)

"""17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

# A= int(input("Enter Number:"))
#
# if A in range(100):
#     print("number is within 100")
# if A in range(100,1000):
#     print("number is within 1000")
# if A in range(1000,2000):
#     print("number is within 2000")

"""18. Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum."""

# A= int(input("Enter Value:"))
# B = int(input("Enter Value:"))
# # C = int(input("Enter Value:"))
# # D = A+B+C
# # if A != B != C:
# #     print(D)
# # else:
# #     print(3*D)
#
#
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))

"""19. Write a Python program to get a newly-generated string from a given string where "Is" has been added 
to the front. Return the string unchanged if the given string already begins with "Is".
"""

# A = "India Is Best Country IN th World"
#
# def get_new(Text):
#     if len(Text) >= 2 and Text[:2] == "Is":
#         return Text
#     return  "Is" + " "+Text
#
# input_string = "India Is Best Country IN the World"
# new_string = get_new(input_string)
# print(new_string)

"""20. Write a Python program that returns a string that is n (non-negative integer) 
copies of a given string."""
#
# def string_copy(original_string,n):
#     if n < 0:
#         return "string is having negative integer"
#     else:
#         return original_string *  n
#
# obj  = string_copy("hello india",3)
# print(obj)

"""21. Write a Python program that determines whether a given number (accepted from the user) is even or odd,
 and prints an appropriate message to the user."""

# def checking(number):
#     if number % 2 ==0:
#         return f"{number} this is even number"
#     else:
#         return f"{number} this is Odd number"
#
# obj = checking(int(input("Enter the Number:")))
# print(obj)

"""22. Write a Python program to count the number 4 in a given list."""

# A = [1,4,14,5,64,40,54,84]
# B = []
#
# for i in str(A):
#     if "4" in i:
#         B.append(i)
# print(B.count("4"))

"""23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
 Return n copies of the whole string if the length is less than 2."""

# def chalenge(original_string,n):
#
#     if len(original_string) >= 2 :
#         return original_string[:2] * n
#     else:
#         return original_string * n
# obj = chalenge("hello india",3)
# print(obj)

"""24. Write a Python program to test whether a passed letter is a vowel or not."""

# def vowel(letter):
#     if letter in "A,E,I,O,U,a,e,i,o,u":
#         return f"{letter}  is VOWEL letter"
#     else:
#         return f"{letter}  is Alphabet"
# obj = vowel("u")
# print(obj)

"""25. Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

# def value(list_value):
#     if list_value in range(10+1):
#         print("True")
#     else:
#         print("False")
# obj = value(-1)

"""26. Write a Python program to create a histogram from a given list of integers.
"""
# import matplotlib.pyplot as plt
#
# def create_histogram(data):
#     plt.hist(data, bins='auto', color='blue', edgecolor='black')
#
#     # Add labels and title
#     plt.xlabel('Value')
#     plt.ylabel('Frequency')
#     plt.title('Histogram Example')
#
#     # Show the histogram
#     plt.show()
#
# # Sample dataset (you can replace this with your data)
# data = [2, 5, 8, 3, 5, 7, 10, 5, 4, 6, 9, 5, 3, 6, 8, 5, 7, 4, 6, 3]
#
# # Create the histogram
# create_histogram(data)

"""27. Write a Python program that concatenates all elements in a list into a string and returns it.
"""

# A = [1,2,4,5,"avinash","patil"]
# B = "".join(str(B) for B in A)
# print((B))

# def concatenate_list_elements(input_list):
#     concatenated_string = "".join(str(element) for element in input_list)
#     return concatenated_string
#
# # Example usage:
# my_list = [1, 2, 3, "hello", "world"]
# result = concatenate_list_elements(my_list)
# print(result)

"""28. Write a Python program to print all even numbers from a given list of numbers in the same order 
and stop printing any after 237 in the sequence.
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]"""

# def even_num(*numbers):
#     for i in numbers:
#         if i % 2 ==0 :
#             print(i,end=",")
#         if i == 237:
#             break
#
# obj = even_num(386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527)

"""29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}"""

# color_list_1 = "White", "Black", "Red"
# color_list_2 = "Red", "Green"
#
# A = []
#
# for B in color_list_2:
#     if B in color_list_1:
#         A.append(B)
# print(A)

"""30. Write a Python program that will accept the base and height of a triangle and compute its area.
"""

# def area(height,base):
#     A = (height * base) / 2
#     return A
#
# obj = area(10,8)
# print(obj)

"""31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""
"""Not Clear"""

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# # Input two positive integers
# num1 = int(input("Enter the first positive integer: "))
# num2 = int(input("Enter the second positive integer: "))
#
# result = gcd(num1, num2)
# print(f"The greatest common divisor (GCD) of {num1} and {num2} is: {result}")

"""33. Write a Python program to sum three given integers. However, if two values are equal, 
the sum will be zero.
"""
# def value(a,b,c):
#     if a == b or b == c or c == a:
#         return 0
#     else:
#          B = a + b + c
#          return B
# obj = value(1,4,3)
# print(obj)

"""34. Write a Python program to sum two given integers. However, 
if the sum is between 15 and 20 it will return 20."""

# def value(a,b):
#     A = a + b
#     if A in range(15,20):
#         return 20
#     else:
#         return A
#
# obj = value(10,11)
# print(obj)

"""35. Write a Python program that returns true if the two given integer values are 
equal or their sum or difference is 5."""

# def value(a,b):
#     A = a +b
#     B = a - b
#     if a == b or A == 5 or B == 5:
#         return "True"
#     else:
#         return A
# obj = value(10,10)
# obj1 = value(2.5,2.5)
# obj3 = value(10,5)
# obj4 = value(10,20)
#
# print(obj)
# print(obj1)
# print(obj3)
# print(obj4)

"""36. Write a Python program to add two objects if both objects are integers.
"""
# my approach
# def value(a,b):
#     try:
#         a = int(a)
#         b = int(b)
#         A = a + b
#         return A
#     except:
#         return "value should be integer"
# obj = value(10,"b")
# print(obj)
#
# #2nd approach
# def value(a,b):
#     if isinstance(a,int) and isinstance(b,int):
#         return a + b
#     else:
#         return "error"
# obj = value(10,"B")
# print(obj)

"""37. Write a Python program that displays your name, age, and address on three different lines.
"""
# def info(name,age,address):
#     print(f"name:{name} \n age: {age} \n address:{address}")
#
# info("Avinash","28", "kpkd")

"""38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""

# def value(a,b):
#     return (a + b) * (a + b)
# obj = value(4,3)
# print(obj)

"""41. Write a Python program to check whether a file exists.
"""
# import os.path
# print(os.path.isfile('main.txt'))
# print(os.path.isfile('main.py'))

"""48. Write a Python program to parse a string to float or integer.
"""

# n = "246.2458"
# print(float(n))
# print(int(float(n)))

"""69. Write a Python program to sort three integers without using conditional statements and loops.
"""

# def value(a,b,c):
#     mini= min(a,b,c)
#     maxi =max(a,b,c)
#     middle = (a+b+c) - maxi - mini
#     return mini, middle, maxi
#
# obj = value(50,20,30)
# print(obj)

""" 81. Write a Python program to concatenate N strings.
"""
# A = ["Avinash", "Ramesh", "Patil"]
# B = " ".join(A)
# print(B)

"""82. Write a Python program to calculate the sum of all items of 
a container (tuple, list, set, dictionary)"""

# tuplle = (1,2)
# listt = [3,4]
# dicti = {1:5,2:6}
#
# A = sum(dicti)
# print(A)

"""83. Write a Python program to test whether all numbers in a list are greater than a certain number.
"""

# A = [20,10,15,30,40]
# B = int(input("enter number:"))
#
# for i in A:
#     if i > B:
#         print(i)
#     else:
#         print("value is greater than list")
#         break

"""84. Write a Python program to count the number of occurrences of a specific character in a string.
"""
# A = "Avinash is Great Always Fun"
# B = 0
# for i in A:
#     if i == "A" or i == "a":
#         B = B + 1
# print(B)

"""88. Given variables x=30 and y=20, write a Python program to print "30+20=50".
"""
# x=30
# y=30
# print(f" {x} + {y} :", x+y)

"""89. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" 
and do nothing if the value is not equal."""
#
# A= int(input("enter value:"))
# if A == 1:
#     print("First day of a Month!" )

"""90. Write a Python program to create a copy of its own source code.
# """
# A  = "Avinah is great guy"
#
# with open ('Interview.text','w') as writer:
#     writer.write(A)

"""91. Write a Python program to swap two variables.
"""
# a = 20
# b= 25
#
# a, b = b, a
# print(a,b)

"""94. Write a Python program to convert the bytes in a given string to a list of integers.
"""
# A = b'avi'
# print(list(A))

"""95. Write a Python program to check whether a string is numeric.
"""

# A = "avi"
# if A.isdigit():
#     print("value is numeric")
# else:
#     print("value is alphabet")
#
# ####################################################
#
# try:
#     i = float(A)
#     print("value is numeric2")
# except:
#     print("value is alphabet2")

"""
110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""

# A = [i for i in range(200) if (lambda i:i%15==0)(i)]
# print(A)

"""112. Write a Python program to remove the first item from a specified list."""

# A = [1,2,3,4,5,6,7,8,9]
# A.remove(A[0])
# print(A)

# second approach

# def remove_first_item(input_list):
#     if input_list:
#         input_list = input_list[1:]
#     return input_list
#
# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# result_list = remove_first_item(my_list)
# print(result_list)  # Output: [2, 3, 4, 5]

"""113. Write a Python program that inputs a number and generates an error message if it is not a number."""
# def num(number):
#     try:
#         number = int(number)
#         print(number)
#     except:
#         print("error: this is not number")
#
# num("the")

"""114. Write a Python program to filter positive numbers from a list."""

# A = [-1, -2, -3, 3, 2, 1]
# B = []
# for i in A:
#     if i >= 0:
#         B.append(i)
# print(B)

"""Write a Python program to determine if a variable is defined or not.
"""
# try:
#     x = 5
# except NameError:
#     print("variable is not define")
# else:
#     print("variable is  define")


"""Method resolution order"""
# 1)
# class A:
#   def method(self):
#     print("this is one")
# class B:
#   def method(self):
#     print("B.method() called")
#
# class C(A,B):
#   pass
#
# class D(C, B):
#   pass
#
# d = D()
# d.method()

# #2)
# class A:
#   def method(self):
#     print("A.method() called")
#
# class B:
#   pass
#
# class C(B, A):
#   pass
#
# c = C()
# c.method()

"""Abstraction"""

from abc import ABC, abstractmethod

# class sum(ABC):
#     @abstractmethod
#     def plus(self):
#         print("i am one")
#
# class add(sum):
#     def gum(self):
#         print("i am second")
#
# obbj = add()
# obbj.gum()
#
# from abc import ABC, abstractmethod
#
# class Sum(ABC):
#     @abstractmethod
#     def plus(self):
#         print("I am one")
#
# class Add(Sum):
#     def plus(self):
#         print("I am second")
#
# obj = Add()
# obj.plus()
#
# """-----------------------------------------------------------------"""
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# Uncomment the lines below to see how abstraction works
# shape = Shape()  # This will raise an error since Shape is an abstract class
# rectangle = Rectangle(5, 3)
# print("Rectangle Area:", rectangle.area())
# print("Rectangle Perimeter:", rectangle.perimeter())
# circle = Circle(4)
# print("Circle Area:", circle.area())
# print("Circle Perimeter:", circle.perimeter())

"""Encapsulation"""

#
# class Bank:
#     def __init__(self, account,balance):
#         self._account = account
#         self.__balance = balance
#
#     def Acount(self):
#         print(self._account)
#     def Balance(self):
#         print(self.__balance)
#
# obj = Bank(1001,10000)
# obj.Balance()

"""Assert and extend"""
# my_list = [1, 2, 3]
# new_elements = [4, 5, 6]
# my_list.extend([4])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

"""Packing and Unpacking"""

# first, *rest, last = [1, 2, 3, 4, 5]
# print(first)  # Output: 1
# print(rest)   # Output: [2, 3, 4]
# print(last)   # Output: 5
#
# def my_function(a, b, c):
#     print(a, b, c)
#
# values = [1, 2, 3]
# my_function(*values)  # Equivalent to my_function(1, 2, 3)


"""148. A Python list contains some positive integers.
Write a Python program to count the numbers that are greater than the previous number on the list.
([1, 4, 7, 9, 11, 5]) -> 4
([1, 3, 3, 2, 2]) -> 1
([4, 3, 2, 1]) -> 0
"""

# A = ([4, 3, 2, 1])
# B = 0
#
# for i in range(len(A)-1):
#     if A[i] < A[i+1]:
#         B += 1
#
# print(B)

"""147. A Python list contains three positive integers. 
Write a Python program to check whether the sum of the digits in each number is equal or not. 
Return true otherwise false.
Sample Data:
([13, 4, 22]) -> True
([-13, 4, 22]) -> False
([45, 63, 90]) -> True"""

# A = ([13, 4, 22])
#
#
# def myfun(n):
#     return sum(int(i) for i in str(abs(n)))
#
#
# def myfun2(m):
#     check_equality = myfun(m[0])
#
#     for l in m[1:]:
#         if check_equality != myfun(l):
#             return False
#     return True
#
#
# print(myfun2([13, 4, -22]))
"""------------------------------------------------------------------------------"""
# def rest(nums):
#     return nums[0] % 9 == nums[1] % 9 == nums[2] % 9
# print(rest([13, 4, -22]))

"""146. A Python list contains two positive integers. 
Write a Python program to check whether the cube root of the first number is equal to the square root of 
the second number.
Sample Data:
([8, 4]) -> True
([64, 16]) -> True
([64, 36]) -> False"""

# A = [64, 36]
#
# if A[0]**2 == A[1]**3:
#     print(True)
# else:
#     print(False)


