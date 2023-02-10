from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

#locators for elements on the page ID, Xpath, CSSSelector, Classname, name, linktext

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#CSSSelector tagname[attribut='value']  #id,  .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Andrei")

driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
#sau
#driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()

#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
#OR
# dropdown.deselect_by_visible_text("Female")

#For XPATH //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#locator
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

#driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")