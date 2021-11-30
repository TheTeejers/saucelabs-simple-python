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
# from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from datetime import datetime
import datetime
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import requests
import json
from selenium.webdriver.common.by import By


from termcolor import colored
# from reusableFxns import *

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
    'tags':['New', 'Build',],
    'name': 'Run: ' + str(datetime.datetime.now()),
    # 'name': 'Run without search between clicks',

    'platform': 'macos 10.15',
    # 'platform': 'windows 10',

    'browserName': 'chrome',
    # 'browserName': 'internet explorer',
    # 'browserName': 'firefox',

    'version': 'latest',
    # 'extendedDebugging': 'true',
    # 'tunnelIdentifier': 'TJTestTunnel1'

    }


# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print (colored("You are using the US data center", 'green'))
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        # command_executor='https://z_h.-1:de2e705d-2f7f-4690-9d1c-9676dbb583e3@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print( colored("You are using the EU data center", 'green'))
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)


print (driver.capabilities)


driver.get('https://google.com')

interact = driver.find_element_by_name('q')
interact.click()

interact.clear()
interact.send_keys("local time")

interact.submit()



try:
    print (colored("looking for Timezone info", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "Uo8X3b")))
    timeElement = driver.find_elements_by_class_name('KfQeJ')

    print (colored("found element", 'green'))
    # print (colored(interact.get_text, 'blue'))
    for x in range (len(timeElement)):
        print(colored(timeElement[x].text, 'blue'))
        print(type(timeElement[x]))
except:
    print (colored("Can not find find_element_by_name('KfQej')", 'red'))
    # print (colored(interact.get_attribute('value'), 'blue'))


print(timeElement[1])
print(type(timeElement[1]))

# if emailValueUincode.encode("utf-8") == email:
if element[1] == '(PDT)':
    print(colored("PASSED", 'green', attrs=['blink', 'underline', 'bold', 'reverse']))
    requests.put(
        # 'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
        'https://saucelabs.com/rest/v1/' + os.environ['SAUCE_USERNAME'] +'/jobs/' + driver.session_id,
        headers = { 'Content-Type': 'application/json',},
        data = '{"passed": true}', # Update this to pass either True or False depending on your requirements
    ),

else:
    print(colored("FAILED", 'red', attrs=['blink', 'underline', 'bold', 'reverse']))
    requests.put(
        # 'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
        'https://saucelabs.com/rest/v1/' + os.environ['SAUCE_USERNAME'] +'/jobs/' + driver.session_id,

        headers = { 'Content-Type': 'application/json',},
        data = '{"passed": false}' # Update this to pass either True or False depending on your requirements
    ),

driver.quit()
# sauce.downloadHAR("job_id", "/var/tmp/");
