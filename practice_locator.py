from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "forgot-password-link").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
driver.find_element(By.ID, "confirmPassword").send_keys("123456789")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#on the main page

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("123456789")