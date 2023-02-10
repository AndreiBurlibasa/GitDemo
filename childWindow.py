from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#make web page stay open even after opening it
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("D:\Selenium\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Click Here").click()
# get the name of all opened windows in chrome
windows_opened = driver.window_handles
#use the name of the opend windows to switch to the new one
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
#close current window
driver.close()
#switch back to parent window
driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text