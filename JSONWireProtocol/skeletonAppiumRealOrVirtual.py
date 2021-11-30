####################################################################
# Skeleton for Appium tests on Sauce Labs RDC
####################################################################


###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import os
import sys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import multiprocessing
# from reusableFxns import *
import requests
import random
import json
from termcolor import (colored)
from datetime import datetime
import datetime
from selenium.webdriver.common.action_chains import ActionChains


##################################################################
# Selenium/Appium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


##################################################################
#setting all variables to false
###################################################################
androidTest = False
iosTest = False
US_Datacenter=False
EU_Datacenter=False
US_Datacenter_TO=False
EU_Datacenter_TO=False

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################
# androidTest = True
iosTest = True

###################################################################
# Choose Data Center and platform
# (Unified Platform or Test Object/Legacy RDC)
# you want to test on
# Uncomment one of these lines
###################################################################
US_Datacenter=True
# EU_Datacenter=True

# US_Datacenter_TO=True
# EU_Datacenter_TO=True

###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################
run = 1


###################################################################
# Declare as a function in order to do multiple runs
###################################################################
def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    ###################################################################
    projectParameters = {
        'name': 'Run: ' + str(datetime.datetime.now()),
        'deviceOrientation' : 'portrait',
        # 'appiumVersion': '1.20.1',
        # 'commandTimeout':600,
        # "recordDeviceVitals": 'true',
        # 'tunnelIdentifier': '<the_name_of_your_tunnel>',
        # "public": "public",
        # "deviceType": "phone",
        # "phoneOnly": 'true',
        # 'wdaEventloopIdleDelay': '5',
        # "waitForQuiescence": False,
        # "cacheId": "1234",
        # "noReset": "true",
    }

    ###################################################################
    # TO/Legacy On CSTEAM: # The API generated for the Test Object project
    # Google website project https://app.testobject.com/#/csteam/google/dashboard
    # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63'
    ###################################################################
    testObjectAppStorage = {
        # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63',
    }

    ###################################################################
    # On Unified Platform
    #AppID and filename found in app setting found on
    #https://app.saucelabs.com/live/app-testing
    ###################################################################
    unifiedPlatformAppStorage = {
        # 'app': 'storage:filename=interact.ipa',
        # 'app': 'storage:2a231e42-0425-4e5c-8023-a7c68f59f970',
    }

    androidParameters = { # Define Android parameters here
        'platformVersion' : '10',
        # 'automationName': 'uiautomator2',
        # 'deviceName' : 'Android GoogleAPI Emulator', #virtual example
        # 'deviceName' : 'Google_Pixel_4_XL_real_us', #RDC example
        'platformName' : 'Android',
    }

    iosParameters = { # Define iOS Parameters here
        # 'deviceName' : 'iPhone_11_14_real_us', #RDC example
        'deviceName' : 'iPhone X Simulator', #virtual example
        'platformVersion' : '14.3',
        'platformName' : 'iOS',
        # 'autoAcceptAlerts': 'true',
        # 'nativeWebTap': True, # iOS only capability.
    }

    ###################################################################
    # Merge parameters into a single capability dictionary
    ###################################################################

    sauceParameters = {}
    sauceParameters.update(projectParameters)
    if androidTest != True and iosTest != True:
        print('You need to specify a platform to test on!')
        sys.exit()
    elif androidTest == True and iosTest == True:
        print('Don\'t be greedy! Only choose one platform!')
        sys.exit()
    elif androidTest:
        sauceParameters.update(androidParameters)
        if len(unifiedPlatformAppStorage) == 0 and len(testObjectAppStorage) == 0:
            sauceParameters.update({'browserName': 'Chrome'}) # Otherwise use Chrome
    elif iosTest:
        sauceParameters.update(iosParameters)
        if len(unifiedPlatformAppStorage) == 0 and len(testObjectAppStorage) == 0:
            sauceParameters.update({'browserName': 'safari'})

    ###################################################################
    # Connect to Test Object (RDC Cloud)
    ###################################################################

    if US_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You have selected the Sauce Labs US Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    elif EU_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You have selected the Sauce Labs EU Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+' @ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    if US_Datacenter_TO==True:
        sauceParameters.update(testObjectAppStorage)
        print (colored('You have selected the Test Object/Legacy RDC US Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://us1.appium.testobject.com/wd/hub',
            desired_capabilities=sauceParameters)

    elif EU_Datacenter_TO==True:
        sauceParameters.update(testObjectAppStorage)
        print (colored('You have selected the Test Object/Legacy RDC EU Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://eu1.appium.testobject.com/wd/hub',
            desired_capabilities=sauceParameters)

    ###################################################################
    # Print all capabilites  passed to test in console
    ###################################################################
    print (driver.capabilities)
    print (len(unifiedPlatformAppStorage))

    try:
        driver.capabilities['testobject_test_name']
        print ('Test Name == ', colored(driver.capabilities['testobject_test_name'], 'green', attrs=['reverse', 'blink']))
        print ('Device Name == ', colored(driver.capabilities['testobject_device_name'], 'green', attrs=['reverse', 'blink']))
        print ('Device descriptor == ', colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))
        print ('Platform Version == ', colored(driver.capabilities['platformVersion'], 'green', attrs=['reverse', 'blink']))
    except:
        print ('Device Name == ', colored(driver.capabilities['deviceName'], 'green', attrs=['reverse', 'blink']))
        print ('Platform Version == ', colored(driver.capabilities['platformVersion'], 'green', attrs=['reverse', 'blink']))

    # ###################################################################
    # # Test logic goes here
    # ###################################################################
    # # Navigating to a website
    # ###################################################################
    driver.get("https://saucelabs.com")

    # source = driver.page_source
    # print(colored(source, 'red'))
    driver.execute_script('sauce:context=Open google.com') #only works on VDC


    try:
        print (colored("looking for Pricing link", 'green'))
        WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.LINK_TEXT, "Pricing")))
        print (colored("found Pricing link!!!", 'green'))
        interact = driver.find_element_by_link_text("Pricing")
        interact.click()
    except:
        print (colored("Can not find Pricing link", 'red'))

    try:
        print (colored("looking for supertitle", 'green'))
        WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CLASS_NAME, "supertitle")))
        print (colored("found supertitle !!!", 'green'))
        interact = driver.find_element_by_class_name("supertitle")
    except:
        print (colored("Can not find supertitle", 'red'))






    # print('https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/')
    # print("testobject_device_session_id=  " + driver.capabilities['testobject_device_session_id'])
    # print("session_id=  " + driver.session_id)

    # Ending the test session
    #__________________________________________________________________
    sauce_result = "failed" if driver.title != 'Pricing | Sauce Labs' else "passed"
    # # sauce_result = "failed" if 1 != 1 else "passed"
    driver.execute_script("sauce:job-result={}".format(sauce_result))

    # driver.execute_script('sauce:context=Change name of test')
    # driver.execute_script('sauce:job-name=Name Changed via JavascriptExecutor')
    # driver.execute_script('sauce:job-name=Name Changed via JavascriptExecutor ' + sauceParameters["name"])

    # print (type(driver.current_url))

    driver.quit()

if __name__ == '__main__':
    jobs = [] #Array for the jobs
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) #Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() #Start the functions.
        num = i+1
        # print(type(i))
        # print(num)
        print('this is the run for: '+ str(num))
