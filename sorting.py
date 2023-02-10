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

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

browserSortedVeggies = []

#click on colum header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#colect all veggie names in list -> BrowserSortedVeggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#Sort veggie list => newSortedList
browserSortedVeggies.sort()
# BrowserSortedVeggieList == newSortedList
assert originalBrowserSortedList == browserSortedVeggies
