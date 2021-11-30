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
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################

region = 'US'

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
    'browserName': 'chrome',
    # 'version': 'latest-1',
    'browserVersion': 'latest',
    'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    # 'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',

    'sauce:options': {
        'name': 'https://dev.testinghub.autodesk.com/ test of drop down menu',
        # 'extendedDebugging':'true',
        # "timeZone": "New_York",
        'tunnelIdentifier': 'tj'
    # 'safari.options':{},

        # 'name': 'UI-Mobile-QA-Regression-tests-Hari',
        # 'build': 'Trying to break it',
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

if region != 'EU':
    print("You are using the US data center")
    driver = webdriver.Remote(
        # command_executor='https://tj.invitationtest3:16e9429a-cc5d-4c36-8caf-087a1e4e899a@ondemand.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print ("You are using the EU data center")
    driver = webdriver.Remote(
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-east-1.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

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
driver.get('https://dev.testinghub.autodesk.com/')

datetime_object = datetime.datetime.now()
print(datetime_object)

# interact = driver.find_element_by_id("i0116")
try:
    print (colored("looking for i0116", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "i0116")))
    interact = driver.find_element_by_id("i0116")
    interact.click()
    print (colored("found i0116", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find i0116", 'red'))

interact.click()

interact.clear()

interact.send_keys("svc_s_thuser@autodesk.com")

interact = driver.find_element_by_id("idSIButton9")

interact.click()

# interact = driver.find_element_by_id("i0118")
try:
    print (colored("looking for i0118", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "i0118")))
    interact = driver.find_element_by_id("i0118")
    interact.click()
    print (colored("found i0118", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find i0118", 'red'))

interact.click()

interact.clear()

interact.send_keys("q3M97RYtf2R1VzAyb5br24UWZUpss8")

interact = driver.find_element_by_id("idSIButton9")

interact.click()

try:
    print (colored("looking for Help", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.LINK_TEXT, "Help")))
    interact = driver.find_element_by_css_selector("div:nth-of-type(1) > .menu-dropdown-title > img")
    interact.click()
    print (colored("found Help", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find Help", 'red'))

try:
    print (colored("looking for Customer journey testing", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu-dropdown-trigger')))
    interact = driver.find_element_by_class_name("menu-dropdown-trigger")
    interact.click()
    print (colored("found Customer journey testing", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find Customer journey testing", 'red'))



try:
    print (colored("looking for Order Fulfillment", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.LINK_TEXT, "Order Fulfillment")))
    interact = driver.find_element_by_link_text("Order Fulfillment")
    interact.click()
    print (colored("found Order Fulfillment", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find Order Fulfillment", 'red'))

try:
    print (colored("looking for OWhat is this link", 'green'))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.LINK_TEXT, "What is this?")))
    interact = driver.find_element_by_link_text("What is this?")
    interact.click()
    print (colored("found OWhat is this link", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find OWhat is this link", 'red'))


# interact = driver.find_elements_by_xpath('//*[@id=\"pageLogin\"]/div/h1')
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

# driver.get('https://www.ancestry.com/account/signin?returnUrl=https%3A%2F%2Fwww.ancestry.com')
# wait = WebDriverWait(driver, 20)
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
# element = WebDriverWait(driver, 30000).until(EC.presence_of_element_located((By.ID,"signInName")))
#
#

#
# interact.send_keys("email address")


#
# ids = driver.find_elements_by_xpath('//*[@id]')
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
