
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from datetime import datetime
import datetime
from time import sleep

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



region = 'US'



sauceParameters = {
    'name': 'Run: ' + str(datetime.datetime.now()),
    'tags':['Case', 'NEW1',],
    'platform': 'windows 10',
    'browserName': 'internet explorer',
    'version': 'latest',
    "prerun": {
        "executable": "sauce-storage:disable-xss.exe",
        "args": [ "/S", "-a", "-q" ],
        "background": False,
        "timeout": 10
        },

}


sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print("You are using the US data center")
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        # command_executor='https://tjtestersauce:4aa9b0f1-44a5-4820-bb4e-35b96ae49a88@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print ("You are using the EU data center")
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)


driver.get('https://saucelabs.com/')

sleep(05)





interact = driver.find_element_by_css_selector("a[href='/support']").click()
interact = driver.find_element_by_css_selector("a[href='https://wiki.saucelabs.com/']").click()


driver.quit()
