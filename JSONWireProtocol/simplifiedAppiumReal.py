####################################################################
# Minimal script to connect to Sauce Labs RDC
# All this does is connect to your project and start a test
# wait 30 seconds. Then quit test
####################################################################


from appium import webdriver
from time import sleep
import requests
import urllib3
import os
import requests
import random
import json
from termcolor import (colored)
from datetime import datetime
import datetime
from time import sleep
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sauceParameters = {
    # 'appiumVersion': '1.13.0',
# 'deviceName' : 'Samsung_Galaxy_S10_real',
'platformName': 'android',
# 'orientation': 'PORTRAIT',
'browserName': 'chrome',
# 'platformVersion': '8.1.0',
'name': 'Run: ' + str(datetime.datetime.now()),
# 'autoLaunch': False,
# 'cacheId': '17aul506a5f122',
# 'maxInstances': 1,
# 'newCommandTimeout': 120,
# 'language': 'en',
# 'allowTouchIdEnroll': True,
# 'locale': 'en',
# 'name': "testName",
# 'tags':['check', 'out', 'these', 'awesome', 'tags'],

# 'app': 'storage:filename=app-tcpProd-release (1).apk',
    # 'app': 'storage:5c5cbeb4-eb4e-4ec1-b7ce-30537091aa05',

    # 'locale' : "fr_CA",
# 'app': 'storage:ce2b3c44-8543-42d7-bcd7-19bb21e99197',

    # 'testobject_api_key' : 'B2A207D1BF6945108D0FF5EC4EB952BB', # Plug in your project API key here
    # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63', # test on Google website
    # 'tunnelIdentifier':'SC-tunnel-8777291832713194',
}

# sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

driver = webdriver.Remote(
    # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
    # command_executor='https://enriquegh:66af84ca-670f-4647-84c2-54b703833015@ondemand.us-west-1.saucelabs.com:443/wd/hub',
    # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
    command_executor='https://ikanotestmobile:0c13e956560e4327b81a062e935b071b@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
    # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+' @ondemand.eu-central-1.saucelabs.com:443/wd/hub',

    desired_capabilities=sauceParameters)
print (driver.capabilities)
print (colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))
source = driver.page_source
print(colored(source, 'red'))

# driver.get("https://google.com")
#
# print(driver.capabilities['testobject_test_report_url'])
#
# # console.log(driver.capabilities['testobject_test_report_url'])
# print(driver.capabilities['testobject_test_live_view_url'])
#
#
# requests.put(
#     'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
#     headers = { 'Content-Type': 'application/json',},
#     data = '{"passed": false}', # Update this to pass either True or False depending on your requirements
#
# ),
# driver.get('https://sm.engage.comprodls.com/')
# sleep(10)
# print("API CALL- " + 'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/')
#
# print(driver.capabilities)
# print("Session ID -  " + driver.session_id)

driver.quit()
