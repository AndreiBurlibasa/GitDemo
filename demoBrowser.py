from selenium import webdriver

# you have to call a chrome driver(intermediate driver -> invoke the browser)
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# path to chromedriver
service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)


#for firefox
# service_obj = Service("D:\Selenium\geckodriver")
# driver = webdriver.Firefox(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/learning-path")
driver.back()
driver.refresh()
driver.forward()
driver.minimize_window()
driver.close()
