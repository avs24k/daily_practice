"""
   import pytest
   from selenium import webdriver

   # Define browsers as parameters
   @pytest.mark.parametrize("browser", ["chrome", "firefox"])
   def test_cross_browser(browser):
       # Fixture to set up and tear down WebDriver
       @pytest.fixture
       def driver():
           if browser == "chrome":
               driver = webdriver.Chrome(executable_path='path/to/chromedriver')
           elif browser == "firefox":
               driver = webdriver.Firefox(executable_path='path/to/geckodriver')
           else:
               raise Exception("Unsupported browser")
           yield driver
           driver.quit()

       # Use the driver fixture to run the test
       with driver() as driver:
           driver.get("https://example.com")
           # Perform your tests using 'driver'
   ```

   In this example, we use `@pytest.mark.parametrize` to run the `test_cross_browser` function twice,
   once with "chrome" and once with "firefox" as the `browser` parameter. We also define a fixture `driver`
   to set up and tear down the WebDriver instances.

4. Run your tests using `pytest`:

   ```
   pytest test_cross_browser.py
   ```

   `pytest` will discover and execute the tests, running each test function for each
    specified browser, and generating a report.

This approach allows you to easily expand your test coverage by adding more browsers to the list of parameters,
and it helps keep your test code concise and readable. The fixture ensures that WebDriver instances are properly
set up and cleaned up for each test,
    making it a convenient way to manage WebDriver instances in a parameterized testing scenario."""


"""import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        # Additional Chrome options if needed
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        # Firefox setup
        driver = webdriver.Firefox()
    elif request.param == "edge":
        # Edge setup
        driver = webdriver.Edge()

    yield driver
    driver.quit()

class TestCrossBrowser:
    def test_example(self, driver):
        # Your test code
        driver.get("https://example.com")
        assert "Example" in driver.title
"""