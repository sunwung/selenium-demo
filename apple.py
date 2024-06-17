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
driver.get('https://www.apple.com/tw/')


mac_page = driver.find_element(By.CLASS_NAME, 'globalnav-link globalnav-submenu-trigger-link globalnav-link-mac')
mac_page.click()


# Wait for the search results to load (you can increase the sleep time if needed)
time.sleep(5)

# Close the browser
driver.quit()
