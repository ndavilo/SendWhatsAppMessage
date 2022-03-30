from selenium import webdriver
import time


driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get('https://web.whatsapp.com/')
msg_box_class = 'p3_M1' # this might change in future to get a new class name inspect the whatsapp web 
button_class = '_4sWnG' # this might change in future 

name = input('Enter the name of user or group: ')
count = int(input('Enter the count: '))
msg = input('Enter your message: ')

input('Enter anything after scanning OR code')

def SendWhatsappMessage(driver, name, count, msg, msg_box_class, button_class):

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name(msg_box_class)

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name(button_class)
        button.click()
        time.sleep(1)

SendWhatsappMessage(driver, name, count, msg, msg_box_class, button_class)
