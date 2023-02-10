from selenium import webdriver
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


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")

# travel from parent /div to child div
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

assert len(products) > 0

# add items to cart
for product in products:
    product.find_element(By.XPATH, "div/button").click()

name_list = []
names = driver.find_elements(By.CSS_SELECTOR, ".product-name")
for name in names:
    if name.text != "":
        # separate the entire name that would be Cucumber - 1 Kg into parts separated by comma
        name_to_be_added = name.text.split(" ")
        name_list.append(name_to_be_added[0])
print(name_list)
assert ['Cucumber', 'Raspberry', 'Strawberry'] == name_list
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# SUM validation, se merge din tr in td[5] si apoi in p
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)
total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == total_amount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

# first we srt up a time out of 10 seconds
wait = WebDriverWait(webdriver, 10)

# secondly we define what should be searched for
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

discouned_amount = int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert total_amount > discouned_amount
# code_message = driver.find_element(By.CLASS_NAME, "promoInfo").text
# assert code_message == "Code applied ..!"
