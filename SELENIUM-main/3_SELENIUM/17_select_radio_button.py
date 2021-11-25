from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()

# Open a URL
driver.get(r'C:\ON-LINE\3_SELENIUM/Drop_down.html')
time.sleep(3)


# Select radio button
driver.find_element_by_id('age4').click()

time.sleep(10)
driver.close()