####################################################################
# Skeleton for Appium tests on Sauce Labs RDC
####################################################################


###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import multiprocessing
import sys
import os
from datetime import datetime
import datetime
# from reusableFxns import *
import requests
# from pathlib import Path
from termcolor import (colored)
androidTest = False
iosTest = False
androidTest = False
iosTest = False
US_Datacenter=False
EU_Datacenter=False
US_Datacenter_TO=False
EU_Datacenter_TO=False

US_Datacenter=True
# EU_Datacenter=True

# US_Datacenter_TO=True
# EU_Datacenter_TO=True

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################

run = 2

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

androidTest = True
# iosTest = True


###################################################################
# Declare as a function in order to do multiple runs
###################################################################


def run_sauce_test():
    testObjectAppStorage = {
        # 'testobject_api_key' : 'B2A207D1BF6945108D0FF5EC4EB952BB', # test on voi-stage
        # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63', # test on Google website
        # 'testobject_api_key': '0DAF8BAC7F6C4AA5AB53DE3B959029B0', #prijil app
        # 'testobject_api_key' : '47061F3DBA644FB5A2DE1C950D94EA92', #bersa-uat
        # 'testobject_api_key' : '62E11503C94443CD9D76483D92D3D3F1', # test on 1Cashify app
        # 'testobject_api_key' : '37696AA9E1274A94B65339806E21A5C4', # test on Varo SIT Debug app
        # 'testobject_api_key' : '7F9F9BD657414E73A556F1AD9941C951', # test on FlashFlood iOS app
        # 'maxInstances': 5,
    }

    unifiedPlatformAppStorage = {
        # 'app': 'storage:filename=BankOfTheWest.ipa',
        # 'app': 'storage:264d3821-e02c-4aa6-a678-e9df4f164d9e', #bersa-uat
    }
    ###################################################################
    # Common parameters (desired capabilities)
    # For Test Object tests
    ###################################################################
    projectParameters = {
        # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63', # The API generated for the Test Object project
        # 'appiumVersion': '1.8.1',
        # 'nativeWebTap': True,
        # 'name': 'Run: ' + getNumber(),
        'maxInstances': 10,

    }

    androidParameters = { # Define Android parameters here
        'deviceName' : 'Google Pixel',
        'platformVersion' : '9',
        # 'browserName' : 'Chrome',
        # 'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
        # 'maxSessions': 1,

    }

    androidParameters1 = { # Define Android parameters here
        'deviceName' : 'Samsung.*',
        'platformVersion' : '10',
        # 'browserName' : 'Chrome',
        # 'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
        # 'maxSessions': 1,

    }

    iosParameters1 = { # Define iOS Parameters here
        'deviceName' : 'iPhone 8 Simulator',
        'deviceOrientation' : 'portrait',
        # 'browserName' : 'safari',
        'platformVersion' : '12.2',
        'platformName' : 'iOS',
        'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'

    }

    iosParameters2 = { # Define iOS Parameters here
        'deviceName' : 'iPhone 8 Simulator',
        'deviceOrientation' : 'portrait',
        # 'browserName' : 'safari',
        'platformVersion' : '14.0',
        'platformName' : 'iOS',
        'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
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
        sauceParameters.update(androidParameters),
        sauceParameters.update(androidParameters1),
        print(run)
    elif iosTest:
        sauceParameters.update(iosParameters1)
        sauceParameters.update(iosParameters2)

    ###################################################################
    # Connect to Test Object (RDC Cloud)
    ###################################################################
    if US_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You are testing on the Sauce Labs US Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://tj.invitationtest1:24168dc8-0900-4994-9ef9-f3442fb9683a@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
            # command_executor='https://<user>.<access_key>.us-west-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    elif EU_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You are testing on the Sauce Labs EU Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    if US_Datacenter_TO==True:
        sauceParameters.update(testObjectAppStorage)
        print (colored('You are testing on the Test Object/Legacy RDC US Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://us1.appium.testobject.com/wd/hub',
            desired_capabilities=sauceParameters)

    elif EU_Datacenter_TO==True:
        sauceParameters.update(testObjectAppStorage)
        print (colored('You are testing on the Test Object/Legacy RDC EU Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://eu1.appium.testobject.com/wd/hub',
            desired_capabilities=sauceParameters)

    ###################################################################
    # Test logic goes here
    ###################################################################
    # Navigating to a website
    #__________________________________________________________________
    print (colored(str(datetime.datetime.now()), 'green', attrs=['blink', 'underline']))
    source = driver.page_source
    print(colored(source, 'red'))
    try:
        print (colored("looking for Sign In", 'green'))
        print (colored(str(datetime.datetime.now()), 'green', attrs=['blink', 'underline']))

        WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "*//XCUIElementTypeButton")))
        # WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, "Sign in")))
        # WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.CLASS_NAME, "Sign in")))
        print (colored(str(datetime.datetime.now()), 'green', attrs=['blink', 'underline']))

        # interact = driver.find_element_by_accessibility_id("I already have an account")
        interact = driver.find_element_by_class_name("Sign in")
        # interact.click()
        print (colored("found sign in", 'green'))
        interact.click()
        print (colored("clicked sign in", 'green'))
        sleep(10)
        # print (colored(driver.contexts, 'blue'))
    except:
        print (colored("Did not find Sign in", 'red'))


    #__________________________________________________________________
    driver.quit()






###################################################################
# This is the command to use multiprocessing to run the desired
# amount of times
###################################################################

if __name__ == '__main__':
    jobs = [] #Array for the jobs
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) #Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() #Start the functions.
        print('this is the run for: '+ str(i))
