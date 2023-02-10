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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//ul//li[2]/a").click()

driver.execute_script("window.scrollBy(0,500);")

# name = driver.find_element(By.XPATH, "//app-card/div/div/h4/a[text()='Samsung Note 8']").text

phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for phone in phones:
    product_name = phone.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        phone.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//app-shop/nav/div/div/ul/li/a").click()

driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

driver.find_element(By.ID, "country").send_keys("rom")
#explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Romania")))

driver.find_element(By.LINK_TEXT, "Romania").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in message
driver.close()