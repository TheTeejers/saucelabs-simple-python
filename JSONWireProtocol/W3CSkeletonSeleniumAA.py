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

# region = 'US'
# region = 'EU'
# region = 'localChrome'
region = 'localSafari'


Business = "//option[@label='Business']"
spaceAvailable = "//option[@label='Space available']"

flightType = Business
# flightType = spaceAvailable
# flightType2 = Business
flightType2 = spaceAvailable

multipleFlightsSelected = True
# multipleFlightsSelected = False

print(colored('Test is running ' + flightType, 'green'))

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
    # 'browserVersion': 'dev',
    'browserVersion': 'latest',
    # 'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',

    'sauce:options': {
        'seleniumVersion': '3.141.59',

        'screenResolution': "1600x1200",
        'extendedDebugging':'true',
        # "timeZone": "New_York",
        # 'tunnelIdentifier': 'tj'
    # 'safari.options':{},

        'name': 'Run: ' + str(datetime.datetime.now()) + '  ' + flightType ,
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
elif region == 'localSafari':
    print(colored("You are using local Safari browser", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Safari(executable_path='/usr/bin/safaridriver');

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
#__________________________________________________________________
# driver.get('https://staging-one.newrelic.com')
# # interact = driver.find_element_by_css_selector("[data-selenium='addToCartButton']")
# # interact.click()
# # driver.get('http://www.bhphotovideo.com/find/cart.jsp')
# #
# # sleep(05)
# # interact = driver.find_element_by_css_selector("[data-selenium='qtyInput']").clear()
# # interact = driver.find_element_by_css_selector("[data-selenium='qtyInput']").send_keys('3')
#
#
print (driver.capabilities)
#
#

# driver.key_down(Keys.COMMAND)
# ActionChains(driver).key_down(Keys.COMMAND).key_down(Keys.ALT).send_keys('j').perform()
# driver.key_down(Keys.COMMAND).key_down(Keys.OPTION).send_keys("j").key_up(Keys.COMMAND).key_up(Keys.OPTION).build().perform();
#
# sleep(05)
#
#
# # Setup for finding an element and sending keystrokes
# #__________________________________________________________________
# # interact = driver.find_element_by_name('figure')
# interact = driver.find_element_by_css_selector("input[name='login[email]']")
# interact.click()
# interact.send_keys("infrauiqaautomation1@gmail.com")
# # interact.submit()
#
# interact = driver.find_element_by_css_selector("input[type='password']")
# interact.click()
# interact.send_keys("password123")
# driver.set_location(49, 123, 10)
# print sauceParameters
# driver.get('https://connect-web.staging.dataservices.theice.com')
# driver.get('https://master.dx.traegergrills.com/recipes/smoked-chili-con-carne')
#
# datetime_object = datetime.datetime.now()
# print(datetime_object)

# interact = driver.find_element_by_id("i0116")
# try:
#     print (colored("looking for jsx-1421156901.cookie_notification.row.no-gutters.position-fixed.p-3.w-100", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "jsx-1421156901.cookie_notification.row.no-gutters.position-fixed.p-3.w-100")))
#
#
#     interact = driver.find_element_by_css_selector("btn.btn-outline-primary.mx-auto")
#     # interact.click()
#     print (colored("found button.btn.btn-outline-primary.mx-auto", 'green'))
#     interact.click()
#     print (colored("clicked button.btn.btn-outline-primary.mx-auto", 'green'))
# except:
#     print (colored("Can not find button.btn.btn-outline-primary.mx-auto", 'red'))

# try:
#     print (colored("looking for button.btn.btn-outline-primary.mx-auto", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mx-auto")))
#     interact = driver.find_element_by_css_selector("button.btn.btn-outline-primary.mx-auto")
#     interact.click()
#     print (colored("found button.btn.btn-outline-primary.mx-auto", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find button.btn.btn-outline-primary.mx-auto", 'red'))
#
# try:
#     print (colored("looking for Print", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.jsx-898850507.secondary-button")))
#     print (colored("found Print", 'green'))
#     print(driver.current_window_handle)
#     interact = driver.find_element_by_css_selector("button.jsx-898850507.secondary-button")
#     print (colored("found Print", 'green'))
#     ids = driver.find_element_by_xpath('//*[@id]')
#     # print (ids)
#     # for ii in ids:
#     #print ii.tag_name
#         # print (ii.get_attribute('id'))
#     print(driver.current_window_handle + "   yo")
#
#
#     interact.click()
#
#     print (windowHandles = driver.get_window_handles() + "this")
#     # if windowHandles.is_empty()
#     #     driver.switchTo().window((String) windowHandles.toArray()[windowHandles.size() - 1]);
#     #
#     # # //Now work with the dialog as with an ordinary page:
#     # driver.find_element(By.className("cancel")).click();
#
#
#     print("here")
#
#     # javaScript = "document.getElementsByTagName(\"button\")[2].setAttribute(\"id\", \"printButton\")"
#     # driver.execute_script(javaScript)
#     # window1 = driver.window_handles[1]
#     # driver.switch_to.window(window1)
#     print(driver.current_window_handle)
#     print (colored("clicked button.jsx-898850507.secondary-button", 'green'))
#
#     print (colored("found button.jsx-898850507.secondary-button", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find button.jsx-898850507.secondary-button", 'red'))
#     interact.click()
#
#
# sleep(5)
# driver.window_handles
# print(driver.current_window_handle)
# print(driver.window_handles)
#
# # var el = document.getElementById('printButton'); setTimeout(function() { el.click(); }, 100);
#
# # jsx-898850507 button-container
# # interact = driver.find_element_by_id("i0118")
# # try:
# #     print (colored("looking for i0118", 'green'))
# #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "i0118")))
# #     interact = driver.find_element_by_id("i0118")
# #     interact.click()
# #     print (colored("found i0118", 'green'))
# #     # print (colored(driver.contexts, 'blue'))
# # except:
# #     print (colored("Can not find i0118", 'red'))
# #
# # interact.click()
# #
# # interact.clear()
# #
# # interact.send_keys("q3M97RYtf2R1VzAyb5br24UWZUpss8")
# #
# # interact = driver.find_element_by_id("idSIButton9")
# #
# # interact.click()
# #
# # try:
# #     print (colored("looking for Help", 'green'))
# #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Help")))
# #     interact = driver.find_element_by_css_selector("div:nth-of-type(1) > .menu-dropdown-title > img")
# #     interact.click()
# #     print (colored("found Help", 'green'))
# #     # print (colored(driver.contexts, 'blue'))
# # except:
# #     print (colored("Can not find Help", 'red'))
# #
# # try:
# #     print (colored("looking for Customer journey testing", 'green'))
# #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu-dropdown-trigger')))
# #     interact = driver.find_element_by_class_name("menu-dropdown-trigger")
# #     interact.click()
# #     print (colored("found Customer journey testing", 'green'))
# #     # print (colored(driver.contexts, 'blue'))
# # except:
# #     print (colored("Can not find Customer journey testing", 'red'))
#
#
#
# try:
#     print (colored("looking for Order Fulfillment", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Order Fulfillment")))
#     interact = driver.find_element_by_link_text("Order Fulfillment")
#     interact.click()
#     print (colored("found Order Fulfillment", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find Order Fulfillment", 'red'))
#
# try:
#     print (colored("looking for OWhat is this link", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "What is this?")))
#     interact = driver.find_element_by_link_text("What is this?")
#     interact.click()
#     print (colored("found OWhat is this link", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find OWhat is this link", 'red'))


# interact = driver.find_element_by_xpath('//*[@id=\"pageLogin\"]/div/h1')
# driver.navigate().refresh()

# javaScript = "document.find_element_by_class_name('.apple-icon-button'[0]).click()"
# driver.execute_script(javaScript)
# driver.execute_script("arguments[0].click()", driver.find_element_by_css_selector('.apple-icon-button'));

# interact = driver.find_element_by_css_selector(".privacy")
# interact = driver.find_element_by_css_selector(".apple-icon-button")
# sleep(15)

# interact.click()
# interact.click()
# sleep(15)


driver.get('https://travelplanner.apps.sepaas.aa.com/')
# driver.get('https://google.com')



#
# interact = driver.find_element_by_name('q')
# interact.click()
#
# interact.clear()
# interact.send_keys("local time")
#
# interact.submit()



try:
    print (colored("looking for id=userID", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "userID")))
    interact = driver.find_element_by_id("userID")

    print (colored("found element", 'green'))
    # interact.click()
    interact.clear()
    interact.send_keys("67778224")
    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    print (colored("Can not find id=userID", 'red'))
    driver.quit()

try:
    print (colored("looking for id=password", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "password")))
    interact = driver.find_element_by_id("password")

    print (colored("found element", 'green'))
    # interact.click()
    interact.clear()
    interact.send_keys("4Password")
    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    print (colored("Can not find id=password", 'red'))
    driver.quit()

try:
    print (colored("looking for id=login", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login")))
    interact = driver.find_element_by_id("login")

    print (colored("found element", 'green'))
    interact.click()

    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    print (colored("Can not find id=login", 'red'))
    driver.quit()

# try:
#     print (colored("looking for Type Of Travel", 'green'))
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



try:
    print (colored("looking for searchRoutes.searchParams.type", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[@class='form-control form-group ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")))

    print('found')

    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_xpath("//select[@class='form-control form-group ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
    print(colored(interact, 'red', attrs=['blink', 'underline', 'bold']))
    # print(len(interact))
    # if len(interact) == 0:
    #     print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
    # else:
    #     print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
    #     for x in range (len(interact)):
    #         print(colored(interact[x].text, 'blue'))
    #         print(colored(interact[x].value, 'green'))
    #         print(type(interact[x]))



    print (colored("found element", 'green'))
    print(interact.text)


    interact.click()
    print(interact.text)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, flightType)))
    # interact = driver.find_element_by_xpath("//option")
    # print(type(interact))
    # if len(interact) != 0:
    #     print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
    # else:
    #     print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))


    interact = driver.find_element_by_xpath(flightType)
    print(type(interact))
    # print(interact.type)
    print(interact.text)


    interact.click()
    print(interact.text)
    #
    # if interact != 0:
    #     print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
    # # print (colored(interact.get_text, 'blue'))
    # # for x in range (len(timeElement)):
    # #     print(colored(timeElement[x].text, 'blue'))
    # #     print(type(timeElement[x]))

except:
    print (colored("Can not find searchRoutes.searchParams.type", 'red'))
    # driver.quit()

try:
    print (colored("looking for origin", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "origin")))


    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_id("origin")

    print (colored("found element", 'green'))
    interact.click()
    interact.send_keys('PHX')


    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    print (colored("Can not find origin", 'red'))
    driver.quit()


try:
    print (colored("looking for destination", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "destination")))


    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_id("destination")

    print (colored("found element", 'green'))
    interact.click()
    interact.send_keys('dfw')


    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    print (colored("Can not find destination", 'red'))
    driver.quit()


try:
    print (colored("looking for date selection", 'green'))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "md-datepicker-input form-control")))

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='md-datepicker-input-container form-group']")))

    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_xpath("//div[@class='md-datepicker-input-container form-group']")

    print (colored("found date selection", 'green'))
    interact.click()
    print('clicked')

    dates = driver.find_elements_by_xpath("//span[@class='md-calendar-date-selection-indicator']")
    # print(dates)
    # RandoNumber = random.randint(1,30)
    # print(RandoNumber)
    # print(len(dates))
    for x in range (len(dates)):
        # print(x)
        # print(colored(dates[x].text, 'blue'))
        # if RandoNumber == x:
        if dates[x].text == '14':
            dates[x].click()
            print(colored('clicked', 'green'))

    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    print (colored("Can not find date selection", 'red'))
    # driver.quit()






try:
    print (colored("looking for Search", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-sm-4 col-xs-12 col-md-3 submit-bottom selectSpace m-bottom-m-md margin-top-small']")))

    print('found')

    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_xpath("//div[@class='col-sm-4 col-xs-12 col-md-3 submit-bottom selectSpace m-bottom-m-md margin-top-small']")

    print (colored("found element", 'green'))
    interact.click()

except:
    print (colored("Can not find Search", 'red'))
    driver.quit()



try:
    print (colored("looking for flight", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//card[contains(@structure,'flight')]")))


    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    Flights = driver.find_elements_by_xpath("//card[contains(@structure,'flight')]")
    # Flights = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]//div[contains(@ng-init,'segmentIndex = $index')]")
    print(Flights)
    print(len(Flights))
    # print (colored(Flights.get_text, 'blue'))
    # for x in range (len(Flights)):
        # print(x)
        # print(colored(Flights[x].text, 'blue'))
        # print(type(interact[x]))

    print (colored("found element 1", 'green'))
    sleep(3)
    interact = driver.find_elements_by_xpath("//button[@class='select ng-scope']")
    print(interact)
    interact = driver.find_element_by_xpath("//button[@class='select ng-scope'][1]")
    # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
    print (colored("found element 3", 'green'))
    print(interact.text)
    interact.click()

    print('picked one')

    if multipleFlightsSelected == True:
        interact = driver.find_elements_by_xpath("//li[@class='ng-binding ng-scope tablinks']")
        print(len(interact))

        interact[3].click()
        sleep(3)
        interact = driver.find_elements_by_xpath("//button[@class='select ng-scope']")
        print(interact)
        interact = driver.find_element_by_xpath("//button[@class='select ng-scope'][1]")
        # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
        print (colored("found element 3", 'green'))
        print(interact.text)
        interact.click()
        print (colored("looking for Search", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-sm-4 col-xs-12 col-md-3 submit-bottom selectSpace m-bottom-m-md margin-top-small']")))

        print('found')

        # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
        interact = driver.find_element_by_xpath("//div[@class='col-sm-4 col-xs-12 col-md-3 submit-bottom selectSpace m-bottom-m-md margin-top-small']")

        print (colored("found element", 'green'))
        print(interact.text)

        interact.click()
        print (colored("looking for flight", 'green'))
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//card[contains(@structure,'flight')]")))


        # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
        Flights = driver.find_elements_by_xpath("//card[contains(@structure,'flight')]")
        # Flights = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]//div[contains(@ng-init,'segmentIndex = $index')]")
        print(Flights)
        print(len(Flights))
        # print (colored(Flights.get_text, 'blue'))
        # for x in range (len(Flights)):
            # print(x)
            # print(colored(Flights[x].text, 'blue'))
            # print(type(interact[x]))

        print (colored("found element 1", 'green'))
        sleep(3)
        interact = driver.find_elements_by_xpath("//button[@class='select ng-scope']")
        print(type(interact))

        print(interact[0].text)
        print(interact[1].text)
        interact = driver.find_element_by_xpath("//button[@class='select ng-scope'][1]")
        # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
        print (colored("found element 2", 'green'))
        print(interact.text)
        interact.click()

        print('picked one')

    # interact = driver.find_element_by_xpath("//button[@class='select ng-scope'][2]")
    # # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
    # print (colored("found element 2", 'green'))
    # print(interact.text)
    # interact.click()


    # interact = driver.find_elements_by_xpath("//button[@class='select ng-scope']")
    # print(interact)
    # interact = driver.find_element_by_xpath("//button[@class='btn-primary-outline ng-scope'][1]")
    # # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
    # print (colored("found element 3", 'green'))
    # print(interact.text)
    # interact.click()


    # interact.send_keys('DFW')


    # print (colored(interact.get_text, 'blue'))
    # for x in range (len(timeElement)):
    #     print(colored(timeElement[x].text, 'blue'))
    #     print(type(timeElement[x]))

except:
    interact = driver.find_element_by_xpath("//button[@class='btn-primary-outline ng-scope'][1]")
    # interact = driver.find_element_by_xpath("//card[contains(@structure,'flight')][1]")
    print (colored("found element 3", 'green'))
    print(interact.text)
    interact.click()
    print(colored("No second option", "red"))


try:
    print (colored("looking for Book Now", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//a[@class='col-xs-6 text-right ng-scope']")))

    print('found')

    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_xpath("//a[@class='col-xs-6 text-right ng-scope']")

    print (colored("found element", 'green'))
    interact.click()

except:
    print (colored("Can not find Book Now", 'red'))
    driver.quit()



try:
    print (colored("looking for cabin Select", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'cabin-select ng-scope')]")))

    print('found')
    # # print(interact.get_attribute('class'))
    # # interact.get_attribute('class')
    # # print(interact.get_attribute('value'))
    # # interact.get_attribute('value')
    # # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    # interact = driver.find_element_by_xpath("//div[contains(@class,'has-error ng-hide')]")
    #
    # print (colored("found element interact", 'green'))
    # print(interact)
    # # print(interact.get_attribute('class'))
    # # interact.get_attribute('class')
    # # print(interact.get_attribute('value'))
    # # interact.get_attribute('value')
    # # print(len(interact))
    #
    #
    # interact = driver.find_element_by_xpath("//span[@class,'form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty']")
    #
    # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
    # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
    # interact = driver.find_elements_by_xpath("//@name='cabin0')")
    interact = driver.find_elements_by_xpath("//select[contains(@name,'cabin')]")
    # interact = driver.find_elements_by_xpath("//div[contains(@class,'cabin-select ng-scope')]")


    print("gogogogogogo")
    # print(colored(len(interact), 'red', attrs=['blink', 'underline', 'bold']))
    print(interact)
    print(type(interact))
    type(interact)
    # interact.click()
    print(len(interact))
    len(interact)
    length = len(interact)
    print(type(len(interact)))
    if length == 0:
        print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
    else:
        print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
        interact = driver.find_elements_by_xpath("//option[contains(@value, 'string:')]")
        print(colored(type(interact), 'magenta'))
        for x in range (len(interact)):
            print("x= ", x)
            print(colored(interact[x].text, 'green'))
            print(type(interact[x]))
        interact[1].click()
    # interact.get_attribute('val')
    # print(colored(interact.get_attribute('class'), 'red', attrs=['blink', 'underline', 'bold']))
    # interact.click()

except:
    print (colored("Can not find cabin Select", 'red'))
    # driver.quit()

# interact.click()
# print(type(interact))
# print(len(interact))


try:
    print (colored("looking for Traveler Select", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'traveler')]")))

    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'pull-left form-control ng-pristine ng-empty ng-invalid ng-invalid-required ng-invalid-aasibling input-box-error ng-touched')]")))

    print('found2')

    #
    # interact = driver.find_element_by_xpath("//span[@class,'form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty']")
    #
    # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
    # form-control coachDisable ng-pristine ng-untouched ng-valid ng-not-empty
    # interact = driver.find_elements_by_xpath("//@name='cabin0')")
    interact = driver.find_elements_by_xpath("//select[@name='traveler']")
    # interact = driver.find_elements_by_xpath("//div[contains(@class,'cabin-select ng-scope')]")


    print("traveler found")
    # print(colored(len(interact), 'red', attrs=['blink', 'underline', 'bold']))
    print(interact)
    print(type(interact))
    # interact.click()
    print(len(interact))
    length = len(interact)
    print(type(len(interact)))
    if length == 0:
        print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
    else:
        print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
        # interact = driver.find_elements_by_xpath("//option[contains(@value, 'string:')]")
        interact = driver.find_elements_by_xpath("//select[contains(@name,'traveler')]//option")
        print(colored(type(interact), 'magenta'))
        for x in range (len(interact)):
            print("x= ", x)
            print(colored(interact[x].text, 'green'))
            print(type(interact[x]))
        interact[1].click()
    # interact.get_attribute('val')
    # print(colored(interact.get_attribute('class'), 'red', attrs=['blink', 'underline', 'bold']))
    # interact.click()

except:
    print (colored("Can not find Traveler Select----scrolling down to look again", 'red'))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'traveler')]")))
    interact = driver.find_elements_by_xpath("//select[@name='traveler']//option")
    # interact = driver.find_elements_by_xpath("//div[contains(@class,'cabin-select ng-scope')]")


    print("traveler found")
    # print(colored(len(interact), 'red', attrs=['blink', 'underline', 'bold']))
    print(interact)
    print(type(interact))
    # interact.click()
    print(len(interact))
    length = len(interact)
    print(type(len(interact)))
    if length == 0:
        print(colored("NULL or 0", 'red', attrs=['blink', 'underline', 'bold']))
    else:
        print(colored("NOT NULL", 'red', attrs=['blink', 'underline', 'bold']))
        # interact = driver.find_elements_by_xpath("//option[contains(@value, 'string:')]")
        interact = driver.find_elements_by_xpath("//select[@name='traveler']//option/")
        print(colored(type(interact), 'magenta'))
        for x in range (len(interact)):
            print("x= ", x)
            print(colored(interact[x].text, 'green'))
            print(type(interact[x]))
        interact[1].click()
    # lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # match=False
    #     while(match==False):
    #             lastCount = lenOfPage
    #             time.sleep(3)
    #             lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    #             if lastCount==lenOfPage:
    #                 match=True




    # lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # match=False
    #     while(match==False):
    #             lastCount = lenOfPage
    #             time.sleep(3)
    #             lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    #             if lastCount==lenOfPage:
    #                 match=True


try:
    print (colored("looking for Continue ", 'green'))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'btn btn-primary margin-bottom-medium')]")))

    print('found')

    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
    interact = driver.find_element_by_xpath("//button[contains(@class,'btn btn-primary margin-bottom-medium')]")

    print (colored("found element", 'green'))
    print(interact)
    print(type(interact))

    interact.click()

except:
    print (colored("Can not find cabin ", 'red'))
    driver.quit()
# try:
#     print (colored("looking for searchRoutes.searchParams.type", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[@class='form-control form-group ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")))
#
#     print('found')
#
#     # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model, 'searchRoutes.searchParams.type")))
#     interact = driver.find_element_by_xpath("//select[@class='form-control form-group ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
#
#     print (colored("found element", 'green'))
#     interact.click()
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//option[@label='Business']")))
#     interact = driver.find_element_by_xpath("//option[contains(@label, 'Business")
#     interact.click()
#
#
#     # print (colored(interact.get_text, 'blue'))
#     # for x in range (len(timeElement)):
#     #     print(colored(timeElement[x].text, 'blue'))
#     #     print(type(timeElement[x]))
#
# except:
#     print (colored("Can not find searchRoutes.searchParams.type", 'red'))
#     driver.quit()
#
# driver.implicitly_wait(5000)
# sleep(5)
# driver.switch_to.frame("signInFrame");
# sleep(5)

# javaScript = "driver.find_element_by_id('login-button')[0].click()"
# driver.execute_script(javaScript)
# driver.execute_script("arguments[0].click()", driver.find_element_by_id('login-button'));
# login = driver.find_element_by_id("login-button")
# driver.execute_script("arguments[0].click();", login)
# # interact.click()
#
# element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"signInName")))
#
#

#
# interact.send_keys("email address")


#
# ids = driver.find_element_by_xpath('//*[@id]')
# for ii in ids:
#     print "name: ",  ii.get_attribute('name')
#     print "class: ", ii.get_attribute('class')
#     print "id: ", ii.get_attribute('id')
#
# # interact = driver.find_element_by_css_selector("input[id='login_submit']")
# # interact.submit()
# #
# # sleep(05)
# driver.get('https://www.cbtnuggets.com/login')
# print(driver.session_id)
# # driver.get('https://gauntface.github.io/simple-push-demo/')
# # driver.get('https://www.qa.apartmentguide.com')
# # popup = driver.switch_to_alert
#
# # sleep(90)
# # Setup for finding an element and clicking it
# #__________________________________________________________________
# # interactive tabbed-standard
#
#
# # interact = driver.find_element_by_css_selector("a[href='/support']").click()
# # interact = driver.find_element_by_css_selector("a[href='https://wiki.saucelabs.com/']").click()
#
# sleep(15)
# # iframe = driver.switch_to.frame(find_element_by_class('interactive'))
# # iframe = driver.switch_to.frame(find_element_by_class_name('interactive'))
# # interact = driver.find_element_by_link_text("Documentation").click()
# # interact = driver.find_element_by_id("i_am_a_textbox").send_keys("Sauce")
#
# # interact = driver.find_element_by_name("q")
#
# # try:
# #     element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((driver.find_element_by_id("email"))))
# # finally:
# #     driver.quit()
# # wait = WebDriverWait(driver, 10)
# try:
#     # Wait as long as required, or maximum of 5 sec for element to appear
#     # If successful, retrieves the element
#     interact = WebDriverWait(driver,60).until(
#          EC.presence_of_element_located((By.ID, "email")))
#
#     # Type "selenium"
#     # element.send_keys("selenium")
#
#     #Type Enter
#     # element.send_keys(Keys.ENTER)
#
# # except TimeoutException:
#     print("Failed to load search bar at www.google.com")
# finally:
#     print("Failed to load search bar at www.google.com!!!!!!")
#     print(driver.session_id)
# # element = wait.until(EC.presence_of_element_located((driver.find_element_by_id("email"))))
# # interact = driver.find_element_by_id("email")
# # interact = driver.find_element_by_class_name("mdl-switch__ripple-container ").click()
# interact.click()
# # interact.send_keys('atesting+444bop@cbtnuggets.com')
# interact.send_keys('email@email.email')
# interact = driver.find_element_by_id("password")
# interact.click()
# interact.send_keys('password123')
# # interact.send_keys('XJstgWsu3dwchRyDr')
# interact.submit()

# sleep(15)
# Setup for using random Python commands
#__________________________________________________________________
# driver.save_screenshot('screenshot.png')
# sleep(50)
# print('Message')

# Setup for using Action chains
#__________________________________________________________________
# ActionChains(driver).move_to_element(interact).perform()

# Setup for random script executions
#__________________________________________________________________
# driver.execute_script('sauce: break')
# driver.execute_script('sauce:context=Place words here for notes')

# Ending the test session
#__________________________________________________________________
driver.quit()
