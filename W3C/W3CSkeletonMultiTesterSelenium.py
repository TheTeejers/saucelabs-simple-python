####################################################################
# Skeleton for Multi Testing Selenium tests on Sauce Labs
####################################################################


###################################################################
# Imports that are good to use
###################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
from datetime import datetime
from time import sleep
import multiprocessing
from termcolor import colored
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # av
from selenium.webdriver.common.by import By
import requests
import json


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
# This makes the functions below execute 'run' amount of times
###################################################################

run = 300
run = 3

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################

region = 'US'

###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Sauce Labs Tests
    ###################################################################
    sauceParameters = {
        # Required platform information
        'platformName': 'macos 10.15',
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'pageLoadStrategy': 'none',


        # Options used by Sauce Labs
        'sauce:options':{
            'tags':['Case', 'NUM',],
            'name': 'testing load of http://dev.newyorklife.com/resources/financial-calculators/retirement-savings-calculator',
            'build': 'page load test NYL',
            # 'extendedDebugging': 'true',
            # 'capturePerformance': 'true'
            # 'tunnelIdentifier':'Phill Tunnel One',
            # 'screenResolution':'1920x1080',
            # 'seleniumVersion': '3.141.59',
            # 'iedriverVersion': '3.4.0',
            # 'chromedriverVersion': '2.40',
            # 'requireWindowFocus' : True,
            # 'maxDuration': 1800,
            'idleTimeout': 1000,
            'commandTimeout': 600,
            # 'videoUploadOnPass':False,
            # 'extendedDebugging':'true',
            # 'prerun':{
            #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
            #     'args': ['--silent'],
            #     'timeout': 500,
            #     'background': 'false',
            # },
        },

        # # Options used by Chrome
        # 'goog:chromeOptions':{
        #     'w3c': True,    # Required for a W3C Chrome test
        #     # 'mobileEmulation':{'deviceName':'iPhone X'},
        #     # 'prefs': {
        #     #     'profile': {
        #     #         'password_manager_enabled': False
        #     #         },
        #     #         'credentials_enable_service': False,
        #     #     },
        #     # 'args': ['test-type', 'disable-infobars'],
        # },
        # 'moz:firefoxOptions':{
        #     "log": {"level": "trace"},
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
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    elif region == 'EU':
        print ("You are using the EU data center")
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    ###################################################################
    # Test logic goes here
    ###################################################################
    # Navigating to a website
    #__________________________________________________________________


    # driver.get('https://stg.newyorklife.com')
    # print(colored (str(driver.title), "red"))


    # driver.get('http://stg.newyorklife.com/resources/financial-calculators/retirement-savings-calculator')
    driver.get('https://stg.newyorklife.com/learn-and-plan/retirement-savings-calculator')

    # https://stg.newyorklife.com/resources/financial-calculators/retirement-savings-calculator
    print(colored ("hello world!", "blue"))
    print(colored (str(driver.title), "red"))

    driver.get('https://stg.newyorklife.com')
    print(colored (str(driver.title), "red"))


    driver.get('http://stg.newyorklife.com/resources/financial-calculators/retirement-savings-calculator')
    print(colored ("hello world!", "blue"))
    print(colored (str(driver.title), "red"))

    # Setup for finding an element and clicking it
    #__________________________________________________________________
    # interact = driver.find_element_by_id('menu-item-112')
    # interact.click()
    try:
        print (colored("looking for Page", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "main-frame-error")))
        # interact = driver.find_element_by_accessibility_id("I already have an account")
        # interact.click()
        print (colored("site failed to load", 'red'))

        # sauce_result = "failed"
        # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"

        # driver.execute_script('site failed to load')

        # driver.execute_script("sauce:job-result={}".format(failed))


        # print (colored(driver.contexts, 'blue'))
    except:
        print (colored("site loaded", 'green'))

    sauce_result = "passed" if str(driver.title) != 'dev.newyorklife.com' else "failed"

    # driver.execute_script('site failed to load')

    driver.execute_script("sauce:job-result={}".format(sauce_result))


        # print (colored(interact.get_attribute('value'), 'blue'))
    # Setup for finding an element and sending keystrokes
    #__________________________________________________________________
    # interact = driver.find_element_by_class_name('figure')
    # interact.send_keys('Dryzz')
    # interact.submit()

    # Setup for using random Python commands
    #__________________________________________________________________
    # driver.save_screenshot('screenshot.png')
    # sleep(10)
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




###################################################################
# This is the command to use multiprocessing to run the desired
# amount of times
###################################################################

if __name__ == '__main__':
    jobs = [] # Array for the jobs
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() # Start the functions.
        # print('this is the run for: '+ str(i))
