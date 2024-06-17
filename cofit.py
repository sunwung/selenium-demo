from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




# Path to your ChromeDriver
chrome_driver_path = '/Users/samuel.yang/Desktop/Code_project/chromedriver-mac-x64/chromedriver'

# Create a new instance of the Chrome driver service
service = Service(chrome_driver_path)

# Initialize the Chrome driver with the executable path argument
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)

# Navigate to the cofit main page
driver.get('https://events.cofit.me/')

# Locate and click the 'select plans' button
select_plans = driver.find_element(By.XPATH, '//*[@id="section-228185"]/header/div/div[2]/div/div/div/div/div[2]/nav/div/div[2]/div/div[4]/div/a')
select_plans.click()

# # Wait for the page to load
# time.sleep(5)

# Locate the element that should contain the title "熱門方案"
popular_plans_title= driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/section/div/div[2]/div/div/div/div/div/div/h2/strong')

# Get the text of the located element
popular_plans_title_text = popular_plans_title.text

# Define the expected title
expected_title = "熱門方案"

# Use assert to check if the title matches the expected title
assert expected_title in popular_plans_title_text, f"Title does not match. Expected '{expected_title}', but got '{popular_plans_title}'"


all_plans_title= driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[4]/section/div/div[2]/div/div/div/div/div/div/h2/strong')
all_plans_title_text = all_plans_title.text
expected_title = "所有方案"
assert expected_title in all_plans_title_text, f"Title does not match. Expected '{expected_title}', but got '{all_plans_title}'"

# Select a popular plan and click it
select_a_popular_plan = driver.find_element(By.XPATH, '//*[@id="section-287706"]/section/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/a/button')
select_a_popular_plan.click()

# Footer about us
about_us = driver.find_element(By.XPATH, '//*[@id="TextBox-Elp2wQuo1RO"]/div[1]/div/p[1]/a/strong/span')
about_us.click()


# Footer privacy
privacy = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[8]/footer/section/div/div[2]/div/div/div/div/div[1]/div/p[2]/a/strong/span')
privacy.click()

# Footer Q&A
QandA = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[8]/footer/section/div/div[2]/div/div/div/div/div[1]/div/p[3]/strong/span/a/strong/span')
QandA.click()


# Footer contact us
contact_us = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[8]/footer/section/div/div[2]/div/div/div/div/div[1]/div/p[4]/span/strong/a')
contact_us.click()

# Footer join us
join_us = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[8]/footer/section/div/div[2]/div/div/div/div/div[1]/div/p[5]/span/a/strong')
join_us.click()


windows = driver.window_handles
driver.switch_to.window(windows[1])

all_plans = driver.find_element(By.XPATH, '//*[@id="section-228185"]/header/div/div[2]/div/div/div/div/div[2]/nav/div/div[2]/div/div[4]/div/a')
all_plans.click()

select_a_popular_plan = driver.find_element(By.XPATH, '//*[@id="section-287706"]/section/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/a/button')
select_a_popular_plan.click()

# Booking analysis 
booking_analysis = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[33]/section/div/div[2]/div/div/div/div/div/div/p/a/strong/span')
booking_analysis.click()



windows = driver.window_handles
driver.switch_to.window(windows[4])
wait = WebDriverWait(driver, 10)

# Select  營養師一對一體態及飲食分析（首次報名）
radio_button_1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[2]/div/div[1]/div/label')
radio_button_1.click()

# Select payment method 信用卡
radio_button_2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[2]/div/div[4]/div/div[1]/label')
radio_button_2.click()

# Input your name
input_name = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[1]/input')
input_name.send_keys('QA test')

# Input number 1
input_phone_number_1 = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[2]/div[2]/input')
input_phone_number_1.send_keys('0926123456')

# Input number 2
input_phone_number_2 = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[2]/div[3]/input')
input_phone_number_2.send_keys('0926123456')

# Input email
input_email = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[3]/input')
input_email.send_keys('sunwung520@gmail.com')

# Select location
selection_location = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[4]/input[1]')
selection_location.click()

# Select available timem
available_time = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[4]/input[10]')
available_time.click()

# Click agreement
agreement = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[5]/div/label/a')
agreement.click()

# Agree ok
agree = driver.find_element(By.XPATH, '//*[@id="dialog"]/button')
agree.click()

# Click next
next = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div[7]/div/button')
next.click()


# # Wait for the page to load
time.sleep(10)
# Close the browser
# driver.quit()
pass