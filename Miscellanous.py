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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#To take a screenshot of the page
#driver.get_screenshot_as_file("screen.png")

#Headless mode -> no browser will be opened
# chrome_option_2 = webdriver.ChromeOptions()
# chrome_option_2.add_argument("headless")