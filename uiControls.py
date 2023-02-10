from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#
# for option in checkboxes:
#     if option.get_attribute('value') == "option2":
#         option.click()
#         assert option.is_selected()
#         break

# find by class
# radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
#
# for button in radiobutton:
#     if button.get_attribute('value') == "radio3":
#         button.click()
#         assert button.is_selected()
#         break

display_box = driver.find_element(By.ID, "displayed-text")
hide_button = driver.find_element(By.ID, "hide-textbox")
assert display_box.is_displayed()
print(display_box.is_displayed())

time.sleep(3)

hide_button.click()

assert display_box.is_displayed()
print(display_box.is_displayed())