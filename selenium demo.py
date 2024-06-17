from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Path to your ChromeDriver
chrome_driver_path = '/Users/samuel.yang/Desktop/Code_project/chromedriver-mac-x64/chromedriver'

# Create a new instance of the Chrome driver service
service = Service(chrome_driver_path)

# Initialize the Chrome driver with the service argument
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Navigate to the Google homepage
driver.get('https://www.google.com/')

# Find the search input field by its name attribute and fill in the search query
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('屏東肉圓')

# Get the value of the input field and print it
input_value = search_input.get_attribute('value')
print(input_value)

# Assert that the input value contains the character '.'
assert '屏東肉圓' in input_value, f"Expected '.' in input value but got {input_value}"

# Find and click the search button by its name attribute
search_button = driver.find_element(By.NAME, 'btnK')
time.sleep(5)
search_button.click()

# Wait for the search results to load (you can increase the sleep time if needed)
time.sleep(5)

# Close the browser
driver.quit()



