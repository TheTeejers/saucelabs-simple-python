####################################################################
# Skeleton for Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
# Not always used for every test
###################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from datetime import datetime, date, time, timezone
import datetime

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
# from reusableFxns import *
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# import KEYS
from selenium.webdriver.common.keys import Keys
import random
import requests
import json
from termcolor import colored

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Select Data Center
# Set region to 'US' or 'EU' or 'localChrome'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################

region = 'US'
# region = 'EU'
# region = 'localChrome'




print(colored('Test is running', 'green'))

# flightType = spaceAvailable
###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs Tests
###################################################################
sauceParameters = {
    # Required platform information
    # 'platformName': 'macOS 10.13',
    # 'browserName': 'safari',
    # 'browserVersion': 'latest',
    # 'name': 'Run: ' + str(datetime.datetime.now()),
    #
    # # Options used by Sauce Labs
    # 'sauce:options':{
    #     'tags':['Case', 'NUM',],
    #     # 'name': 'Run: ' + str(datetime.datetime.now()),
    #     # 'extendedDebugging': 'true',
    #     # 'capturePerformance': 'true',
    #     # "webdriver.remote.quietExceptions": 'true',
    #     # 'tunnelIdentifier':'Phill Tunnel One',
    #     # 'screenResolution':'1920x1080',
    #     # 'seleniumVersion': '3.141.59',
    #     # 'iedriverVersion': '3.4.0',
    #     # 'chromedriverVersion': '2.40',
    #     # 'requireWindowFocus' : True,
    #     # 'maxDuration': 1800,
    #     # 'idleTimeout': 1000,
    #     # 'commandTimeout': 600,
    #     # 'videoUploadOnPass':False,
    #     # 'extendedDebugging':'true',
    # "prerun":"https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat",

    # },
    # 'count': 1,
    'platformName': 'windows 10',
    # 'browserName': 'firefox',
    # 'browserName': 'MicrosoftEdge',
    # 'browserName': 'internet explorer',
    'browserName': 'chrome',
    # 'version': 'latest-1',
    'browserVersion': '85',
    # 'browserVersion': 'latest',
    # 'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    # 'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',

    'sauce:options': {
        'seleniumVersion': '3.141.59',

        'screenResolution': "1600x1200",
        'extendedDebugging':'true',
        # "timeZone": "New_York",
        # 'tunnelIdentifier': 'tj'
    # 'safari.options':{},

        'name': 'Run: ' + str(datetime.datetime.now()) + ' https://1cb20a1.autocad-web-snapshots.com ',
        'build': 'Trying to break it!!!',
        #
        #
        # 'tunnelIdentifier': 'tj',
    },

    # 'sauce:options': {
    #     # 'name': 'UI-Mobile-QA-Regression-tests-Hari',
    #     # 'build': 'Trying to break it',
    #     #
    #     #
    #     # 'tunnelIdentifier': 'tj',
    # },


    # Options used by Chrome
    # 'goog:chromeOptions':{
    #     'w3c': True,    # Required for a W3C Chrome test
    #     # 'mobileEmulation':{'deviceName':'iPhone X'},
    #     # 'prefs': {
    #     #     'profile': {
    #     #         'password_manager_enabled': False
    #     #         },
    #     #         'credentials_enable_service': False,
    #     #     },
    #     # 'args': ['--auto-open-devtools-for-tabs'],
    # },
    # 'moz:firefoxOptions':{
    #     "log": {"level": "trace"},
    #     'geckodriverVersion':'0.27.0',
    # },
}


# This concatenates the tags key above to add the build parameter
# sauceParameters['sauce:options'].update({'build': '-'.join(sauceParameters['sauce:options'].get('tags'))})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU' or region != 'localChrome':
    print(colored("You are using the US data center", 'green', attrs=['blink', 'reverse', 'underline']))
    # driver = webdriver.Chrome(executable_path='/Users/terranceloughry/Downloads/chromedriver',
    driver = webdriver.Remote(
        # command_executor='https://tj.invitationtest3:16e9429a-cc5d-4c36-8caf-087a1e4e899a@ondemand.saucelabs.com:443/wd/hub',

        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print(colored("You are using the EU data center", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Remote(
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-east-1.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'localChrome':
    print(colored("You are using local Chrome browser", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Chrome(executable_path='/Users/terranceloughry/Downloads/chromedriver')

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
#__________________________________________________________________

print (driver.capabilities)



driver.get('https://1cb20a1.autocad-web-snapshots.com/?e2eTests=true&fabricTests=true')



# try:
#     print (colored("looking for id=userID", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "userID")))
#     interact = driver.find_element_by_id("userID")
#
#     print (colored("found element", 'green'))
#     # interact.click()
#     interact.clear()
#     interact.send_keys("67778224")
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find id=userID", 'red'))
#     driver.quit()
#
# try:
#     print (colored("looking for id=password", 'green'))
#     WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "password")))
#     interact = driver.find_element_by_id("password")
#
#     print (colored("found element", 'green'))
#     # interact.click()
#     interact.clear()
#     interact.send_keys("4Password")
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find id=password", 'red'))
#     driver.quit()
#
# try:
#     print (colored("looking for id=login", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login")))
#     interact = driver.find_element_by_id("login")
#
#     print (colored("found element", 'green'))
#     interact.click()
#
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find id=login", 'red'))
#     driver.quit()
#
#
#
#
#
# try:
#     print (colored("looking for searchRoutes.searchParams.type", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[@class='form-control form-group ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")))
#
#     print('found')
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_xpath("//select[@class='form-control form-group ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
#     print(colored(interact, 'red', attrs=['blink', 'underline', 'bold']))
#     # print(len(interact))
#     # if len(interact) == 0:
#     #     print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
#     # else:
#     #     print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
#     #     for x in range (len(interact)):
#     #         print(colored(interact[x].text, 'blue'))
#     #         print(colored(interact[x].value, 'green'))
#     #         print(type(interact[x]))
#
#
#
#     print (colored("found element", 'green'))
#     interact.click()
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, flightType)))
#     # interact = driver.find_element_by_xpath("//option")
#     # print(type(interact))
#     # if len(interact) != 0:
#     #     print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
#     # else:
#     #     print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
#
#
#     interact = driver.find_element_by_xpath(flightType)
#     print(type(interact))
#
#     interact.click()
#     #
#     # if interact != 0:
#     #     print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
#     # # print (colored(interact.get_text, 'blue'))
#     # # for x in range (len(timeElement)):
#     # #     print(colored(timeElement[x].text, 'blue'))
#     # #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find searchRoutes.searchParams.type", 'red'))
#     # driver.quit()
#
# try:
#     print (colored("looking for origin", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "origin")))
#
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_id("origin")
#
#     print (colored("found element", 'green'))
#     interact.click()
#     interact.send_keys('PHX')
#
#
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find origin", 'red'))
#     driver.quit()
#
#
# try:
#     print (colored("looking for destination", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "destination")))
#
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_id("destination")
#
#     print (colored("found element", 'green'))
#     interact.click()
#     interact.send_keys('dfw')
#
#
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find destination", 'red'))
#     driver.quit()
#
#
# try:
#     print (colored("looking for date selection", 'green'))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "md-datepicker-input form-control")))
#
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='md-datepicker-input-container form-group']")))
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_xpath("//div[@class='md-datepicker-input-container form-group']")
#
#     print (colored("found date selection", 'green'))
#     interact.click()
#     print('clicked')
#
#     dates = driver.find_elements_by_xpath("//span[@class='md-calendar-date-selection-indicator']")
#     # print(dates)
#     # RandoNumber = random.randint(1,30)
#     # print(RandoNumber)
#     # print(len(dates))
#     for x in range (len(dates)):
#         # print(x)
#         # print(colored(dates[x].text, 'blue'))
#         # if RandoNumber == x:
#         if dates[x].text == '14':
#             dates[x].click()
#             print(colored('clicked', 'green'))
#
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find date selection", 'red'))
#     # driver.quit()
#
#
#
#
#
#
# try:
#     print (colored("looking for Search", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-sm-4 col-xs-12 col-md-3 submit-bottom selectSpace m-bottom-m-md margin-top-small']")))
#
#     print('found')
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_xpath("//div[@class='col-sm-4 col-xs-12 col-md-3 submit-bottom selectSpace m-bottom-m-md margin-top-small']")
#
#     print (colored("found element", 'green'))
#     interact.click()
#
# except:
#     print (colored("Can not find Search", 'red'))
#     driver.quit()
#
#
#
# try:
#     print (colored("looking for flight", 'green'))
#     WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//card[contains(@structure,'flight')]")))
#
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     Flights = driver.find_elements_by_xpath("//card[contains(@structure,'flight')]")
#     # Flights = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]//div[contains(@ng-init,'segmentIndex = $index')]")
#     print(Flights)
#     print(len(Flights))
#     # print (colored(Flights.get_text, 'blue'))
#     # for x in range (len(Flights)):
#         # print(x)
#         # print(colored(Flights[x].text, 'blue'))
#         # print(type(interact[x]))
#
#     print (colored("found element 1", 'green'))
#     sleep(3)
#     interact = driver.find_elements_by_xpath("//button[@class='select ng-scope']")
#     print(interact)
#     interact = driver.find_element_by_xpath("//button[@class='select ng-scope'][1]")
#     # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
#     print (colored("found element 2", 'green'))
#     print(interact.text)
#     interact.click()
#
#
#     # interact = driver.find_elements_by_xpath("//button[@class='select ng-scope']")
#     # print(interact)
#     # interact = driver.find_element_by_xpath("//button[@class='btn-primary-outline ng-scope'][1]")
#     # # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
#     # print (colored("found element 3", 'green'))
#     # print(interact.text)
#     # interact.click()
#
#
#     # interact.send_keys('DFW')
#
#
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     interact = driver.find_element_by_xpath("//button[@class='btn-primary-outline ng-scope'][1]")
#     # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
#     print (colored("found element 3", 'green'))
#     print(interact.text)
#     interact.click()
#     print(colored("No second option", "red"))
#
#
# try:
#     print (colored("looking for Book Now", 'green'))
#     WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//a[@class='col-xs-6 text-right ng-scope']")))
#
#     print('found')
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_xpath("//a[@class='col-xs-6 text-right ng-scope']")
#
#     print (colored("found element", 'green'))
#     interact.click()
#
# except:
#     print (colored("Can not find Book Now", 'red'))
#     driver.quit()
#
#
#
# try:
#     print (colored("looking for cabin Select", 'green'))
#     WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'cabin-select ng-scope')]")))
#
#     print('found')
#     # # print(interact.get_attribute('class'))
#     # # interact.get_attribute('class')
#     # # print(interact.get_attribute('value'))
#     # # interact.get_attribute('value')
#     # # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     # interact = driver.find_element_by_xpath("//div[contains(@class,'has-error ng-hide')]")
#     #
#     # print (colored("found element interact", 'green'))
#     # print(interact)
#     # # print(interact.get_attribute('class'))
#     # # interact.get_attribute('class')
#     # # print(interact.get_attribute('value'))
#     # # interact.get_attribute('value')
#     # # print(len(interact))
#     #
#     #
#     # interact = driver.find_element_by_xpath("//span[@class,'form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty']")
#     #
#     # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
#     # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
#     # interact = driver.find_elements_by_xpath("//@name='cabin0')")
#     interact = driver.find_elements_by_xpath("//select[contains(@name,'cabin')]")
#     # interact = driver.find_elements_by_xpath("//div[contains(@class,'cabin-select ng-scope')]")
#
#
#     print("gogogogogogo")
#     # print(colored(len(interact), 'red', attrs=['blink', 'underline', 'bold']))
#     print(interact)
#     print(type(interact))
#     type(interact)
#     # interact.click()
#     print(len(interact))
#     len(interact)
#     length = len(interact)
#     print(type(len(interact)))
#     if length == 0:
#         print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
#     else:
#         print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
#         interact = driver.find_elements_by_xpath("//option[contains(@value, 'string:')]")
#         print(colored(type(interact), 'magenta'))
#         for x in range (len(interact)):
#             print("x= ", x)
#             print(colored(interact[x].text, 'green'))
#             print(type(interact[x]))
#         interact[1].click()
#     # interact.get_attribute('val')
#     # print(colored(interact.get_attribute('class'), 'red', attrs=['blink', 'underline', 'bold']))
#     # interact.click()
#
# except:
#     print (colored("Can not find cabin Select", 'red'))
#     # driver.quit()
#
# # interact.click()
# # print(type(interact))
# # print(len(interact))
#
#
# try:
#     print (colored("looking for Traveler Select", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'traveler')]")))
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'pull-left form-control ng-pristine ng-empty ng-invalid ng-invalid-required ng-invalid-aasibling input-box-error ng-touched')]")))
#
#     print('found2')
#
#     #
#     # interact = driver.find_element_by_xpath("//span[@class,'form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty']")
#     #
#     # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
#     # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
#     # interact = driver.find_elements_by_xpath("//@name='cabin0')")
#     interact = driver.find_elements_by_xpath("//select[@name='traveler']")
#     # interact = driver.find_elements_by_xpath("//div[contains(@class,'cabin-select ng-scope')]")
#
#
#     print("traveler found")
#     # print(colored(len(interact), 'red', attrs=['blink', 'underline', 'bold']))
#     print(interact)
#     print(type(interact))
#     # interact.click()
#     print(len(interact))
#     length = len(interact)
#     print(type(len(interact)))
#     if length == 0:
#         print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
#     else:
#         print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
#         # interact = driver.find_elements_by_xpath("//option[contains(@value, 'string:')]")
#         interact = driver.find_elements_by_xpath("//select[contains(@name,'traveler')]//option")
#         print(colored(type(interact), 'magenta'))
#         for x in range (len(interact)):
#             print("x= ", x)
#             print(colored(interact[x].text, 'green'))
#             print(type(interact[x]))
#         interact[1].click()
#     # interact.get_attribute('val')
#     # print(colored(interact.get_attribute('class'), 'red', attrs=['blink', 'underline', 'bold']))
#     # interact.click()
#
# except:
#     print (colored("Can not find Traveler Select----scrolling down to look again", 'red'))
#
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'traveler')]")))
#     interact = driver.find_elements_by_xpath("//select[@name='traveler']//option")
#     # interact = driver.find_elements_by_xpath("//div[contains(@class,'cabin-select ng-scope')]")
#
#
#     print("traveler found")
#     # print(colored(len(interact), 'red', attrs=['blink', 'underline', 'bold']))
#     print(interact)
#     print(type(interact))
#     # interact.click()
#     print(len(interact))
#     length = len(interact)
#     print(type(len(interact)))
#     if length == 0:
#         print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
#     else:
#         print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
#         # interact = driver.find_elements_by_xpath("//option[contains(@value, 'string:')]")
#         interact = driver.find_elements_by_xpath("//select[@name='traveler']//option/")
#         print(colored(type(interact), 'magenta'))
#         for x in range (len(interact)):
#             print("x= ", x)
#             print(colored(interact[x].text, 'green'))
#             print(type(interact[x]))
#         interact[1].click()
#
#
# try:
#     print (colored("looking for Continue ", 'green'))
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'btn btn-primary margin-bottom-medium')]")))
#
#     print('found')
#
#
#     interact = driver.find_element_by_xpath("//button[contains(@class,'btn btn-primary margin-bottom-medium')]")
#
#     print (colored("found element", 'green'))
#     print(interact)
#     print(type(interact))
#
#     interact.click()
#
# except:
#     print (colored("Can not find cabin ", 'red'))
#     driver.quit()


sleep(60)
# Ending the test session
#__________________________________________________________________
driver.quit()
