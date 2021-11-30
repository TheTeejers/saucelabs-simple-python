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
    # 'browserName': 'firefox',
    # 'browserName': 'MicrosoftEdge',
    # 'browserName': 'internet explorer',
    'browserName': 'chrome',
    # 'browserName': 'safari',
    # 'version': 'latest-1',
    # 'browserVersion': '11.1',
    'browserVersion': 'latest',
    # 'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    # 'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',
    'public':'private',
    'sauce:options': {
        'name':'https://search.myway.com intercept test with no body',
        # 'tags':'13128733',
        'extendedDebugging':'true',
        'build':'Customer repro',
        'screenResolution':'1600x1200',
        # 'avoidProxy': 'true',
        # 'capturePerformance': 'true',
        # 'seleniumVersion': '3.141.59',
        # 'public':'private',
        # 'name': 'https://dev.testinghub.autodesk.com/ test of drop down menu',
        # 'extendedDebugging':'true',
        # "timeZone": "New_York",
        # 'tunnelIdentifier': '5672e05b4b7f4b8bb9f032a511b4d3fb'
        # 'tunnelIdentifier': 'tj111::sauce::468f60825c404ca889c5b420c790c80b'
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
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
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
driver.execute_script("sauce:intercept", {
    "url": "https://search.myway.com/search/*",
        "response": {
            "headers": {
                "Authorization": "Basic YWRtaW46aFY2YzJxPmU=",
                "Connection": "Keep-Alive",
                "Content-Encoding": "gzip",
                "Accept-Language": "en-US",
                "Content-Type": "text/html; charset=UTF-8",
                "Cookie": "anx=fv=1604909571251&g=-&nv=1&lv=1604909571251&sn=41121f676035",
                "Proxy-Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Host": "10.53.125.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            },
            # "body": [{
            #     # "title": "Hello",
            #     # "order": 1,
            # }]
        }
    })
#
# driver.execute_script('sauce:intercept', {
#     "url": "https://www.google.com",
#     "redirect": "https://saucelabs.com"
# })
# driver.get('https://www.ancestry.com/account/signin?returnUrl=https%3A%2F%2Fwww.ancestry.com')
driver.get('https://search.myway.com/search/GGmain.jhtml?n=783996E5&p2=%5Ezs%5Eyyyyyy%5ETTAB02%5Eus&searchfor=flowers&st=hp&tpr=sbt')

# driver.execute_script('sauce:intercept', {
#     "url": "https://google.com",
#     "redirect": "https://saucelabs.com"
# })




# driver.execute_script('sauce:intercept', {
#     "url": "https://google.com/*",
#     # "error": "Failed"
#     "response": {
#         "status": 500,
#             "body": [{
#                 "title": "Hello, the page has a 500 error",
#             }],
#     }
# })

#__________________________________________________________________
driver.quit()
