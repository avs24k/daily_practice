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
#
#
# class C(B):
#     def my_fun2(self):
#         A.my_fun0(self)
#         print("this is class")
#
#
# obj = C()
# obj.my_fun2()


"""map"""
import pytest

import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

# def my_fun(n,m):
#     try:
#         result = n/m
#         return result
#     except ZeroDivisionError as e:
#         return e
#
#
# print(my_fun(10,0))


# def decor(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result.upper()
#     return wrapper
#
# @decor
# def my_fun():
#     return "hello"
#
# print(my_fun())

# obj_service = Service('C:\\Users\Vikky\PycharmProjects\Interview_Practice\driver\chromedriver.exe')
# driver = webdriver.Chrome(service=obj_service)
# driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=676742234347&hvpos=&hvnetw=g&hvrand=8976207286231776880&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007786&hvtargid=kwd-10573980&hydadcr=14453_2367553")
# driver.find_element(By.XPATH,"//tagname[@attribute='value']").click()
# driver.find_element(By.CSS_SELECTOR,"tagname[attribute='value']")
# driver.find_element(By.XPATH,"//tag[contains(text(),'value')]
#
# A = driver.window_handles
# driver.switch_to.A[1]


# @pytest.mark.parametrize("A,B,result", [(5, 5, 10)])
# def test_myfun(A, B, result):
#     total = A + B
#     try:
#         assert total == result
#     except AssertionError as e:
#         raise e

