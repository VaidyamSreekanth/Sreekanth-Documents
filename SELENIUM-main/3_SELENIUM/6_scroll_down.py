from selenium import webdriver
import time

# Open a Chrome Browser
d = webdriver.Chrome();
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(10)

# To Scroll down page
d.execute_script("window.scrollTo(0, 200)")
time.sleep(6)
d.execute_script("window.scrollTo(200, 400)")
time.sleep(6)

# To Scroll up page
d.execute_script("window.scrollTo(500, 0)")
time.sleep(5)
d.close()

