# single inheritance

# class A:
#     def my_fun(self):
#         print("Hello")
#
# class B(A):
#     def my_fun1(self):
#         super().my_fun()
#         print("World")
#
# obj = B()
# obj.my_fun1()


# multiple inheritance

# class A:
#     def my_fun(self):
#         print("hello")
#
# class B:
#     def my_fun(self):
#         super().my_fun()
#         print("World")
#
# class C(B,A):
#     def my_fun(self):
#         super().my_fun()
#         print("new world")
#
# obj = C()
# obj.my_fun()


# multilevel inheritance
# class A:
#     def my_fun0(self):
#         print("hello")
#
#
# class B(A):
#     def my_fun1(self):
#         super().my_fun0()
#         print("world")


# class C(B):
#     def my_fun2(self):
#         super().my_fun1()
#         print("this is class")
#
#
# obj = C()
# obj.my_fun2()


"""map"""

"""Basic Mapping: Write a Python program to square each number in a list using the map() function."""

# no need to pass obj and iterator(list,tuple,dict) will assign to the fun

# def myfun(x):
#     return x ** 2
#
#
# A = [2, 3, 4, 5]
# mapping = map(myfun, A)
# print(list(mapping))

# def myfun(x):
#     return x.upper()
#
# iterator = ['avinash', 'patil', 'roshan']
#
# mapping = map(myfun,iterator)
# print(list(mapping))

"""String Lengths: Given a list of strings, 
use map() to create a new list containing the lengths of each string."""

# def myfun(x):
#     return len(x)
#
#
# container = ["avi", "ramesh", "patil"]
# mapping = map(myfun, container)
#
# print(list(mapping))

"""Temperatures Conversion: Convert a list of temperatures 
from Celsius to Fahrenheit using the formula Fahrenheit = (Celsius * 9/5) + 32."""


# def myfun(x):
#     return (x * 9 / 5) + 32
#
# liss= [10, 20, 16]
#
# mapping = map(myfun, liss)
# print(list(mapping))

"""filter"""

# files = ['document.txt', 'image.jpg', 'data.csv', 'script.py']
#
# A = '.txt'
#
# B = filter(lambda x:x.endswith(A),files)
#
# print(list(B))







