from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

input('scan and press a key: ')

booty = driver.find_element_by_css_selector('span[title="CHANGE THIS"]')
booty.click()

i=0
n=50

while i<n:
    i+=1
    textarea = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textarea.send_keys('Your Unique Message')
    sendbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span')
    sendbutton.click()
