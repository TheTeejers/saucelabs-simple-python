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
# region = 'EU'
# region = 'headless'
# region = 'localSafari'
# region = 'localChrome'


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
    'platformName': 'macos 11.00',
    # 'platformName': 'WIN10',
    # 'browserName': 'firefox',
    # 'browserName': 'MicrosoftEdge',
    # 'browserName': 'internet explorer',
    # 'browserName': 'chrome',
    'browserName': 'safari',
    'version': 'latest',
    # 'browserVersion': 'dev',
    # 'browserVersion': '14',
    # 'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    # 'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',
    # 'public':'private',
    'sauce:options': {
        'name':'Safari 14 test file upload  ' + str(datetime.datetime.now()),
        # 'tags':'13128733',
        # 'extendedDebugging':'true',
        # 'build':'PHAB-D62936_1743005',
        # 'screenResolution':'1600x1200',
        # 'avoidProxy': 'true',
        # 'capturePerformance': 'true',
        'seleniumVersion': '3.141.59',
        # 'public':'private',
        # 'name': 'https://dev.testinghub.autodesk.com/ test of drop down menu',
        # 'extendedDebugging':'true',
        # "timeZone": "New_York",
        # 'tunnelIdentifier': 'safari14test'
        # 'tunnelIdentifier': 'tj'
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
# region = 'US'
# region = 'EU'
# region = 'headless'
# region = 'localSafari'
# region = 'localChrome'

try:
    region
except NameError:
    region = 'US'

if region == 'US':
    print(colored("You are using the US data center", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Remote(
        # command_executor='https://tj.invitationtest3:16e9429a-cc5d-4c36-8caf-087a1e4e899a@ondemand.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print (colored("You are using the EU data center", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'localSafari':
    print(colored("You are using local Safari browser", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Safari(executable_path='/usr/bin/safaridriver');
elif region == 'headless':
    print(colored("You are using local the HEADLESS datacenter", 'green', attrs=['blink', 'reverse', 'underline']))
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-east-1.saucelabs.com:443/wd/hub',
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
#
#
# driver.get('https://www.file.io/')
driver.get('https://filebin.net/')

try:
    print (colored("looking for input type 'file'", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "fileField")))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "react-fine-uploader-file-input")))
    print (colored("found input type 'file'", 'green'))

    interact = driver.find_element_by_css_selector("[type='file']")
    # interact
    # interact.click()
    # JavascriptExecutor driver = (JavascriptExecutor)getDriver();
    # driver.execute_script("arguments[0].click();", interact);
    # driver.execute_script("sauce:job-result={}".format(sauce_result))
    interact.send_keys('/Users/terranceloughry/Desktop/possum.jpg')
    print (colored("uploading image", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find input type 'file'", 'red'))
# #
try:
    print (colored("looking for image link", 'green'))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'link-custom')))
    interact = driver.find_element_by_link_text("possum.jpg")
    interact.click()
    print (colored("found and clicked on image link", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find image link", 'red'))

# try:
#     print (colored("looking for class name img-thumbnail", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'img-thumbnail')))
#     # interact = driver.find_element_by_xpath("//button")
#     # interact.click()
#     sleep(5)
#     print (colored("found image", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find image", 'red'))
#
#
#
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
