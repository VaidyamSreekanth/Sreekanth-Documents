from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\ON-LINE\3_SELENIUM/Drop_down.html')
time.sleep(5)

select_element = driver.find_element_by_id('MONTHS')

months = Select(select_element)
time.sleep(5)
## To select a value based on visable text
#months.select_by_visible_text('May')
#time.sleep(5)

## To select a value based on value
#months.select_by_value('Apr')
#time.sleep(5)

## To select a value based on index
months.select_by_index(1)

time.sleep(10)
driver.close()





