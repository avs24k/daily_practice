import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)

# driver.get("http://blank.page")
"""Handling Download"""

# option = webdriver.ChromeOptions()
# prefs = {"download.default_directory":"download path"}
# option.add_experimental_option("prefs",prefs)

"""Waits"""
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//form[@id='nav-search-bar-form']")))
#
# select = Select()
# select.select_by_value()
# select.select_by_index()
# select.select_by_visible_text()

# alert = driver.switch_to.alert
# alert.accept()
# alert.dismiss()


# action = ActionChains(driver)
# action.context_click()
# action.double_click()
# action.drag_and_drop_by_offset()
# action.drag_and_drop().perform()

"""Multiple Window Handling"""

# handler = driver.window_handles
# window = driver.switch_to.window(handler[0])

# driver.switch_to.frame()
# driver.switch_to.default_content()

# driver.execute_script("window.scrollTo(0,2000)")
# driver.execute_script("wind")

# driver.get_screenshot_as_png()

# with open('path', 'r') as readble:
#     a = readble.readlines()

# try:
#     A = 10/0
#     print(A)
# except Exception as e:
#     print(e)




# def fun(n,m):
#     yield n+m
#     yield n*m
#
# obj = fun(5,6)
# print(next(obj))
# print(next(obj))

# class A:
#     def my_fun(self):
#         print("class A")
#
# class B(A):
#     def my_fun0(self):
#         print("Class B")
#
# class C(B):
#     def my_fun02(self):
#         super().my_fun()
#         super().my_fun0()
#         print("Class C")
#
# obj = C()
# obj.my_fun02()


# def decor(func):
#     def wraper(*args):
#         result = func(*args)
#         return result.upper()
#     return wraper
#
# @decor
# def fun():
#     return 'hello'
#
# obj = fun()
# print(obj)











