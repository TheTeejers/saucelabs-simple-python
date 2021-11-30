from appium import webdriver

# from time import sleep

import os

import sys

from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

import multiprocessing

import requests

import json

from termcolor import (colored)

from datetime import datetime

import datetime

import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



projectParameters = {

   'name': 'Run: ' + str(datetime.datetime.now()),

   'commandTimeout':600,

   'testobject_api_key' : '47061F3DBA644FB5A2DE1C950D94EA92',

   'phoneOnly': 'true',

   'deviceOrientation' : 'portrait',

   'platformVersion' : '14',

   'platformName' : 'iOS',

   'autoAcceptAlerts': 'true',
   'wdaEventloopIdleDelay': '5',
   'waitForQuiescence': False,

}



driver = webdriver.Remote(command_executor='https://us1.appium.testobject.com/wd/hub', desired_capabilities=projectParameters)



print (driver.capabilities)

print ('Test Name == ', colored(driver.capabilities['testobject_test_name'], 'green', attrs=['reverse', 'blink']))

print ('Device Name == ', colored(driver.capabilities['testobject_device_name'], 'green', attrs=['reverse', 'blink']))

print ('Device descriptor == ', colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))

print ('Platform Version == ', colored(driver.capabilities['platformVersion'], 'green', attrs=['reverse', 'blink']))



try:

    print (colored("looking for bersa-uat", 'green'))

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'bersa-uat')))

    interact = driver.find_element_by_name("bersa-uat")

    print (colored("found bersa-uat!!!", 'green'))

    sauce_result = "passed"

    driver.execute_script("sauce:job-result={}".format(sauce_result))



except:

    print (colored("Can not find bersa-uat", 'red'))

    sauce_result = "failed"

    driver.execute_script("sauce:job-result={}".format(sauce_result))



driver.quit()
