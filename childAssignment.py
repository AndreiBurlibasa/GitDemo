from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])
email = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
driver.close()
driver.switch_to.window(opened_windows[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("123456789")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()


wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)