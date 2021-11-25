from selenium import webdriver
import selenium
import time

# To Know selenium VERSION
print(' \n SELENIUM VERSION IS :: ', selenium.__version__)


# Open a Browser 
driver = webdriver.Chrome()
time.sleep(3)

## If Chrome driver in different path
# driver = webdriver.Chrome(r'C:\\Users\\TEST\chromedriver.exe')

## To Maximize window
driver.maximize_window()
time.sleep(3)

## Open a URL
driver.get('https://accounts.lambdatest.com/login')
time.sleep(3)

## To enter username in text box based on ID Locator
uname = driver.find_element_by_name('email')
uname.send_keys('sriram.python111@gmail.com')
time.sleep(5)

## To enter password in text box based on name Locator
password = driver.find_element_by_id('userpassword')
password.send_keys('sriram.python111')
time.sleep(5)

## To click on login button
login_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[3]/button')
login_button.click()

## Close a browser
driver.close()

