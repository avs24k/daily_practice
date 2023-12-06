# A = "hello world"
# B = A.split()
#
# for i in B:
#     print(i[::-1], end=" ")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# B = {}
#
# for i in A:
#     if i in B:
#         B[i] += 1
#     else:
#         B[i] = 1
#
# C = sorted(B.items(), key= lambda x:x[1])
# print(C)

# A = [i for i in range(10) if i%2==0]
# print(A)

# for log which dependenicies are you used
# if we want only two commit from out of 10 commit
# how to create new branch
# i want verify that three links are open
git
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
#
# def myfun(driver):
#     window = driver.window_handles
#     check = driver.switch_to.window
#     print(len(check))
#     assert check == 3
#
# driver.execute_script("window.open('_blank');")