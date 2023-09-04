# # #
# # # """Que.1 Swap a string"""
# # # def swap_string(s):
# # #     swap_str = s.swapcase()
# # #     return swap_str
# # #
# # # input_string = "AvinasH is Real Og"
# # # op_string = swap_string(input_string)
# # # print(op_string)
# # #
# # # """Que.2 You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen."""
# # # def split_and_join(line):
# # #     a = line.split(" ")
# # #     b = "-".join(a)
# # #     return b
# # # def inpt():
# # #     c= input("Enter the value:")
# # #     result = split_and_join(c)
# # #     print(result)
# # # #inpt()
# # #
# # # """Q.3 You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# # #
# # # Hello firstname lastname! You just delved into python."""
# # #
# # #
# # # def print_full_name(a,b):
# # #     first = first_name
# # #     last= last_name
# # #     print(f"Hello {first} {last}! You just delved into python.")
# # #
# # #
# # # if __name__ == '__main__':
# # #     first_name = input("Enter a name:")
# # #     last_name = input("enter l name:")
# # #     print_full_name(first_name, last_name)
# # #
# # # """Que.4 change the charechter of string..insert new char and print """
# # #
# # #
# # # def mutate_string(string, position, character):
# # #     string = string[:position] + character + string[position + 1:]
# # #     #return string
# # #
# # #
# # # if __name__ == '__main__':
# # #     s = input()
# # #     i, c = input().split()
# # #     s_new = mutate_string(s, int(i), c)
# # #     #print(s_new)
# #
# # """Que.5 """
# #
# #
# # def count_substring(string, sub_string):
# #     count1 = string.count(sub_string)
# #     return count1+1
# #
# #
# # if __name__ == '__main__':
# #     string = input().strip()
# #     sub_string = input().strip()
# #
# #     count = count_substring(string, sub_string)
# #     print(count)
#
#
#
#
# import requests
#
# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
#
# # Create a WebDriver instance
# driver = webdriver.Chrome()
#
# # Navigate to the web page with the links
# driver.get("https://www.interviewbit.com/automation-testing-interview-questions/")
#
# # Find all anchor tags on the page
# strig = driver.find_elements(By.TAG_NAME,"a")
#
# for A in strig:
#     B = A.get_attribute("href")
#     C = requests.head(B)
#     D = C.status_code
#     if D < 200 or D >= 300:
#         print("broken link:",B,"status Code:",D)

import requests
from selenium import webdriver

# Create a WebDriver instance
driver = webdriver.Chrome()

# Navigate to the web page with the links
driver.get("https://www.interviewbit.com/automation-testing-interview-questions")

# Find all anchor tags on the page
links = driver.find_elements(By.TAG_NAME,"a")

# Iterate through each link and check for broken links
for link in links:
    url = link.get_attribute("href")
    response = requests.head(url)
    status_code = response.status_code
    if  status_code >= 400:
        print("Broken link found:", url, "Status Code:", status_code)

# Close the browser and terminate the WebDriver session
driver.quit()
driver.switch_to.frame()
driver.switch_to.default_content()
driver.delete_cookie()