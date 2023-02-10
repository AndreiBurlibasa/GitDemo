from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://www.autovit.ro/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
driver.find_element(By.XPATH, "//div/div/input[@placeholder='Marca']").send_keys("Ford")
driver.find_element(By.LINK_TEXT, "Ford").click()
driver.find_element(By.XPATH, "//div/div/div/input[@placeholder='Model']").send_keys("Focus")

