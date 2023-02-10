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
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")

# travel from parent /div to child div
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

assert len(products) > 0

# add items to cart
for product in products:
    product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

code_message = driver.find_element(By.CLASS_NAME, "promoInfo").text
assert code_message == "Code applied ..!"