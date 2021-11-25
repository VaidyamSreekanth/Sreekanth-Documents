from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.maximize_window()
d.get(r'C:\ON-LINE\3_SELENIUM/alert_2.html')
sleep(5)

d.find_element_by_xpath('/html/body/button').click()

alert = d.switch_to.alert

#  To get alert message
print(' \n\n ' , alert.text)
sleep(5)

## To accept alert
alert.accept()

# alert.accept()  – used to accept the Alert
# alert.dismiss() – used to cancel the Alert
# alert.send_keys(' sriram ') – used to enter a value in the Alert text box.

sleep(10)
d.close()

