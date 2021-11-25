from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\ON-LINE\3_SELENIUM/Drop_down.html')
time.sleep(5)


# Select Check box
obj = driver.find_element_by_id('vehicle1')
obj.click()
time.sleep(5)

driver.close()
