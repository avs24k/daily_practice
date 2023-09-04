import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""Cookies"""

driver = webdriver.Chrome()
#driver.implicitly_wait(10)
#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.get("about:blank")

# delt = driver.delete_cookie("bypass_utm")
# cooki = driver.get_cookies()
# driver.add_cookie({'name':'bypass_utm'})


"""Frames"""

# driver.switch_to.frame(driver.find_elements())
# driver.switch_to.default_content()

"""driver navigation"""
# driver.back()
# driver.forward()
# driver.refresh()

"""Scroll Page"""
# time.sleep(3)
# driver.execute_script("window.scrollTo(0,500)")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# X = driver.find_element(By.XPATH,"//legend[normalize-space()='Mouse Hover Example']")
# driver.execute_script("arguments[0].scrollIntoView();",X)

"""java script executor"""

# driver.execute_script("window.open('https://rahulshettyacademy.com/AutomationPractice/','_self')" )
# time.sleep(5)
# driver.execute_script("window.scrollTo(0,500)")
# #driver.execute_script("document.getElementById('show-textbox').click()")
# A = driver.find_element(By.ID,"show-textbox")
# driver.execute_script("arguments[0].click()",A)
# time.sleep(3)

