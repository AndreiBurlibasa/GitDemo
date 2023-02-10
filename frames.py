from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)

#switch to frame in order to modify/update it
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Automated Frames")
#exit from frame
driver.switch_to.default_content()
text = driver.find_element(By.CSS_SELECTOR, "h3").text
print(text)