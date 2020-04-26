""" Implemented by Sidhant Goyal 
 """

import webbrowser
import selenium
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import string
import time
import pytesseract
from pytesseract import image_to_string 
from PIL import Image 

print("--------------Start-----------------")

def get_captcha_demo(location, size):
    im = Image.open('captcha.png') # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('captcha.png')
    captcha_text = image_to_string(Image.open('captcha.png'))
    print(captcha_text)
    return captcha_text

def getimage(browser):
    captcha_img = browser.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/img')
    location = captcha_img.location
    size = captcha_img.size 
    print(size)
    print(location)
    browser.save_screenshot('captcha.png')
    get_captcha_demo(location , size)

def scrapper():
    url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
    browser = webdriver.Chrome('./chromedriver') 
    browser.get(url)
    browser.maximize_window()
    

    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_dlNO"]').send_keys('DL-0420110149646')
    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_dob_input"]').send_keys('09-02-1976')
    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_dob_input"]').click()


    ## Please insert Your function to get captcha 
    ## getcaptcha()
    #browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt34:CaptchaID"]').send_keys(text)

    time.sleep(20)
    browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt46"]').click()
    time.sleep(10)
    name = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[2]/td[2]').text
    print(name)
    doi = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[3]/td[2]').text
    print(doi)
    doe = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[2]/tbody/tr[1]/td[3]').text
    print(doe)
    classof  = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[2]').text
    print(classof)
    browser.close()


scrapper()


print("------------The End--------------")
