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
import time
import datetime
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
# This makes the functions below execute 'run' amount of times
###################################################################

run = 100

###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Sauce Labs Tests
    ###################################################################
    sauceParameters = {
        'tags':['try and recreate '],

        'name': 'CURRENT_URL Run: ' + str(datetime.datetime.now()),

        'platform': 'Windows 10',
        'browserName': 'chrome',
        'version': 'latest',
        'screenResolution':'1920x1080',
        # 'maxInstances': 2,
        # 'extendedDebugging': 'true',
        # 'capturePerformance': 'true'
        # 'name': 'Run: ' + getNumber(),
        # 'seleniumVersion': '3.8.1',
        # 'iedriverVersion': '3.4.0',
        # 'maxDuration': 1800,
        # 'idleTimeout': 1000,
        # 'commandTimeout': 600,
        # 'videoUploadOnPass':False,
        # 'extendedDebugging':'true',
        # 'prerun':{
        #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
        #     'args': ['--silent'],
        #     'timeout': 500,
        #     'background': 'false',
        # },
        # 'chromeOptions':{
        #     mobileEmulation':{'deviceName':'iPhone X'},
        #     'prefs': {
        #         'profile': {
        #             'password_manager_enabled': False
        #             },
        #             'credentials_enable_service': False,
        #         },
        #     'args': ['test-type', 'disable-infobars'],
        # },
        # 'moz:firefoxOptions':{
        #     "log": {"level": "trace"},
        # },
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
        # print("You are using the US data center on run " + str(run))
        driver = webdriver.Remote(
            # command_executor='https://theteejers817:f0d1527b-840c-46c0-b0d4-69eb97f2d772@ondemand.saucelabs.com:443/wd/hub',
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
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
    # driver.get('https://www.worldtimeserver.com/')
    # # driver.get('https://www.dryzz.com')
    #
    # # Setup for finding an element and clicking it
    # #__________________________________________________________________
    # interact = driver.find_element_by_id('theTime')
    # # interact.click()
    # # print('this is the run for: '+ str(i))
    # print(interact.text)
    # driver.get('https://www.where-am-i.net/')
    #
    # sleep(5)
    # interact = driver.find_element_by_id('location')
    # print(interact.body)

    driver.get("https://www.gymboree.com/ca/home")
    # print(driver.get_cookies())


    # print(driver.get_cookie('name'))
    # driver.get_cookie('name')
    # cookies_list = driver.get_cookies()
    # cookies_dict = {}
    # for cookie in cookies_list:
    #     cookies_dict[cookie['name']] = cookie['value']
    #
    # print(cookies_dict)
    # driver.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[1])
    #
    # driver.get("https://login.microsoftonline.com/897c5146-ab0e-40e5-92cd-154908142efc/oauth2/authorize?client_id=00000003-0000-0ff1-ce00-000000000000&response_mode=form_post&protectedtoken=true&response_type=code%20id_token&resource=00000003-0000-0ff1-ce00-000000000000&scope=openid&nonce=B1E493C5C5C3FA5498BCFA295C57359AEE7709CAAF1FA191-16F09504A8E710E2FDA08B6AE27168087742D41C59676ADC610F15D605C72F76&redirect_uri=https%3A%2F%2Fconstel1.sharepoint.com%2F_forms%2Fdefault.aspx&claims=%7B%22id_token%22%3A%7B%22xms_cc%22%3A%7B%22values%22%3A%5B%22CP1%22%5D%7D%7D%7D&wsucxt=1&cobrandid=11bd8083-87e0-41b5-bb78-0bc43c8a8e8a&client-request-id=3a13a99f-f0ae-b000-c40b-5b281c45f5f9&sso_reload=true")
    sleep(10)

    # driver.current_url
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

    sauce_result = "failed" if str(driver.current_url) != 'https://www.gymboree.com/ca/home' else "passed"
    driver.execute_script("sauce:job-result={}".format(sauce_result))
    # Ending the test session
    #__________________________________________________________________
    driver.quit()




###################################################################
# This is the command to use multiprocessing to run the desired
# amount of times
###################################################################

if __name__ == '__main__' and region == 'US':
    jobs = [] # Array for the jobs
    print(str(run) +" Tests running in the US data center.")
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() # Start the functions.
        # print('this is the run for: '+ str(i))
        # sauceParameters.update({'name': 'Run ' + str(i) +': ' + str(datetime.datetime.now())})
        # print("You are using the US data center on run " + str(i))
elif __name__ == '__main__' and region != 'US':
    jobs = [] # Array for the jobs
    print(str(run) +" Tests running in the EU data center.")
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() # Start the functions.
        # print('this is the run for: '+ str(i))
        # sauceParameters.update({'name': 'Run ' + str(i) +': ' + str(datetime.datetime.now())})
        # print("You are using the US data center on run " + str(i))
