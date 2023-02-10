from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# #action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

action.move_to_element(driver.find_element(By.ID, "checkBoxOption1")).click().perform()
action.move_to_element(driver.find_element(By.ID, "checkBoxOption2")).click().perform()
action.move_to_element(driver.find_element(By.ID, "checkBoxOption3")).click().perform()
