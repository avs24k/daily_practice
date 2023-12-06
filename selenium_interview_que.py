"""What is the use of Thread count? """
# if we want to run multiple test cases in paralarly then we use Thread Count in selenium

import concurrent.futures
import re
import time

from selenium import webdriver

# def run_test(test_case):
#     driver = webdriver.Chrome()
#     driver.get('https://example.com')
#     driver.quit()

# List of test cases to be executed concurrently
# test_cases = ['test_case_1', 'test_case_2', 'test_case_3']

# Set the desired thread count (number of concurrent executions)
# thread_count = 3

# Run tests concurrently using ThreadPoolExecutor
# with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
#     executor.map(run_test, test_cases)


"""How will you Download the popup?"""
# Locate and click the link or button that triggers the download
# download_button = driver.find_element(By.ID, 'downloadButton')
# download_button.click()

# Use keyboard shortcuts to handle the download popup (Ctrl + j in this case for Chrome)
# You might need to adjust this based on the browser
# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'j')

"""Which selenium version is your working"""
# The latest version of Selenium is 4.15.0.


"""What is a regular expression?"""

# In Selenium with Python, a regular expression (regex or regexp) is a powerful tool for pattern matching
# and text manipulation. It allows you to define a search pattern, which can be used to match, search, or replace
# strings based on that pattern.

# The `re` module in Python provides support for regular expressions.
# Here's a brief overview of using regular expressions in Selenium with Python:

# 1. **Import the `re` module:**
#    ```python
#    import re
#    ```
#
# 2. **Using Basic Patterns:**
#    - You can use basic patterns to find matches in strings.
#    ```python
#    pattern = r'abc'  # This pattern will match 'abc' in a string
#    result = re.search(pattern, 'abcdef')
#    if result:
#        print('Pattern found:', result.group())
#    ```
#
# 3. **Meta-characters and Special Sequences:**
#    - Regular expressions can include meta-characters and special sequences for more complex patterns.
#    ```python
#    pattern = r'\d+'  # This pattern will match one or more digits
#    result = re.search(pattern, 'The price is $100')
#    if result:
#        print('Pattern found:', result.group())
#    ```
#
# 4. **Using Regular Expressions with WebDriver:**
#    - Regular expressions are often used when locating elements on a web page using WebDriver.
#    ```python
#    from selenium import webdriver
#
#    driver = webdriver.Chrome()
#    driver.get('https://example.com')
#
#    element = driver.find_element_by_xpath("//input[@id='username']")
#    ```
#
#    - You can use regular expressions in locators:
#    ```python
#    import re
#
#    pattern = r'user'  # This pattern will match 'user' in the element ID
#    element = driver.find_element_by_xpath("//input[@id and re:match(@id, '{}')]".format(pattern))

'''Selenium function used for retrieving the attribute or value? or
How do you get the href of a link / get the source of an image?
'''

# In Selenium, you can use the get_attribute() method to retrieve the value of an attribute for a web element.
# This method is available on the WebElement object and allows you to access the value of any HTML attribute of
# the element

# Find an element by its XPath (replace with your own locator)
# element = driver.find_element_by_xpath("//input[@id='username']")

# Get the value of the 'placeholder' attribute
# placeholder_value = element.get_attribute("placeholder")

# Print the retrieved value
# print(f"The 'placeholder' attribute value is: {placeholder_value}")


"""How do you verify if the checkbox/radio is checked or not"""

#  In Selenium, you can use the is_selected() method to verify whether a checkbox
#  or radio button is checked or not. This method returns True if the element is selected (checked) and
#  False if it is not selected.

# Find the checkbox by its ID (replace with your own locator)
# checkbox = driver.find_element_by_id("checkbox_id")

# Check if the checkbox is selected
# if checkbox.is_selected():
#     print("The checkbox is checked.")
# else:
#     print("The checkbox is not checked.")


"""Count the number of links on a page"""

# To count the number of links on a page using Selenium in Python,
# you can use the find_elements_by_tag_name method to find all a (anchor) elements and then determine the length
# of the list.

# Find all anchor elements on the page
# links = driver.find_elements_by_tag_name("<a")

# Get the count of links
# num_links = len(links)

# Print the number of links
# print(f"The number of links on the page is: {num_links}")
"--------------------------------------------------------------------------------------------------------------"
# element = driver.find_elements(By.TAG_NAME,"a")
# count_link = len(element)
# print(count_link)

"""How do you upload a file? """
# file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
# Provide the full path to the file you want to upload
# file_path = "/path/to/your/file.txt"
# file_input.send_keys(file_path)
# driver.find_element(By.ID, "file-submit").click()

"""How do you get the current page URL?"""
# current_url = driver.current_url
# print(current_url)

"""How do you handle untrusted certificates?
ans------
Handling untrusted certificates in Selenium with Python typically involves dealing with SSL/TLS certificate
errors that may occur when accessing a website with an invalid or self-signed SSL certificate. In a production 
environment, it's crucial to ensure the security of the connection and use valid certificates. However, for testing 
purposes or when dealing with internal services, you might encounter scenarios where you need to 
handle untrusted certificates."""

# option = webdriver.ChromeOptions
# option.add_argument('--ignore-certificate-errors')

"""How to get the number of frames on a page?
ans---

In Selenium, you can use the driver.find_elements method with the By.TAG_NAME locator strategy to find all the
frames on a page. 
The HTML <frame> and <iframe> elements are used to define frames on a web page.
"""
# Find all frames on the page
# frames = driver.find_elements_by_tag_name("frame") + driver.find_elements_by_tag_name("iframe")

# Print the number of frames
# print("Number of frames on the page:", len(frames))

"""How do you check that the pagination on the google search page is working fine or not?
ans-
1)Perform a search on the Google homepage.
2)Extract the search results or any visible information about the search results.
3)Click on the next page link to navigate to the next page of search results.
4)Extract the new set of search results or information.
5)Repeat steps 3 and 4 for multiple pages.
6)Compare the information from different pages to ensure the pagination is working as expected.
"""

"""How to check if an element is visible on the web page?
"""

# element = driver.find_element_by_css_selector("your_element_selector")

# Check if the element is visible
# if element.is_displayed():
#     print("The element is visible on the web page.")
# else:
#     print("The element is NOT visible on the web page."

"""How to check if a button is enabled on the page?
"""

# Locate the button element you want to check (replace with your own locator)
# button = driver.find_element_by_css_selector("your_button_selector")

# Check if the button is enabled
# if button.is_enabled():
#     print("The button is enabled on the web page.")
# else:
#     print("The button is disabled on the web page.")

"""How do you handle the secured connection error in HTTPS?
"""
# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--ignore-certificate-errors')
#
# driver = webdriver.Chrome(chrome_options=chrome_options)

"""How to run the tests without a browser or with an HTML unit driver in selenium webdriver?
"""
# Set Chrome options for headless mode
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Run in headless mode

"""How to check if the checkbox or radio button is selected?
"""
# Locate the checkbox element
# checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
#
# # Check if the checkbox is selected
# if checkbox.is_selected():
#     print("Checkbox is selected.")
# else:
#     print("Checkbox is not selected.")


"""How do you get the attribute of the web element?
"""

# Locate an element by its XPath (replace with the actual XPath)
# element = driver.find_element_by_xpath("//input[@id='someId']")

# Get the value of the 'value' attribute
# value_attribute = element.get_attribute("value")

# Get the value of the 'href' attribute
# href_attribute = element.get_attribute("href")

# Get the value of the 'src' attribute
# src_attribute = element.get_attribute("src")

# Get the value of the 'class' attribute
# class_attribute = element.get_attribute("class")

"""How to get the CSS attribute of a web element using the web driver?
"""

# Locate an element by its XPath (replace with the actual XPath)
# element = driver.find_element_by_xpath("//div[@id='yourElementId']")

# Get the value of a specific CSS attribute (replace 'background-color' with the desired attribute)
# css_value = element.value_of_css_property("background-color")

# Print the CSS value
# print(f"The value of the 'background-color' attribute is: {css_value}")

"""How to press Shift+Tab?
"""

# element = driver.find_element("xpath", "//input[@id='yourElementId']")

# Create an ActionChains object
# actions = ActionChains(driver)

# Press Shift+Tab using key_down() method
# actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)

"""This corrected code uses key_down() to press the Shift key, send_keys(Keys.TAB) to simulate pressing the 
Tab key, and key_up(Keys.SHIFT) to release the Shift key. 
The perform() method executes the series of actions. Adjust the code according to your specific needs."""

# Perform the action on the element
# actions.perform()

"""How to enter :(colon using web driver)?
"""

# Locate an input field on the page (replace with your actual locator strategy)
# input_field = driver.find_element("xpath", "//input[@id='yourElementId']")

# Enter a colon in the input field
# input_field.send_keys(Keys.SHIFT, ';')

"""
What is the use of getPageSource()?
Ans-----
The getPageSource() method in Selenium is used to retrieve the entire HTML source code of the current page. 
This method returns a string containing the HTML source of the page as it exists in the DOM (Document Object Model)
 at the time the method is called."""

# Get the page source
# page_source = driver.page_source

# Print or use the page source as needed
# print(page_source)