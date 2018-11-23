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
from reusableFxns import *


###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################

run = 2

###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Sauce Labs Tests
    ###################################################################    
    sauceParameters = {
        'tags':['Case', 'NUM',],
        'platform': 'Windows 10',
        'browserName': 'chrome',
        'version': 'latest',
        'screenResolution':'1920x1080',
        'name': 'Run: ' + getNumber(),
        # 'seleniumVersion': '3.8.1',
        # 'iedriverVersion': '3.4.0',
        # 'maxDuration': 1800,
        # 'idleTimeout': 1000,
        # 'commandTimeout': 600,
        # 'videoUploadOnPass':False,
        # 'extendedDebugging':'true',
        # 'prerun':{ 
        #     'executable': 'https://gist.githubusercontent.com/phillram/92a0f22db47892e4b27d04066084ce92/raw/aaeee222780e4ad8647667b267d81684d6059b5c/set_agent.sh',
        #     'args': '',
        #     'background': 'true',
        # },
        # 'chromeOptions':{
        #     mobileEmulation':{'deviceName':'iPhone X'},
        #     'prefs': {
        #         'profile': {
        #             'password_manager_enabled': False
        #             },
        #             'credentials_enable_service': False,
        #         },
        #         'args': ['test-type', 'disable-infobars'],
        # },
    }

    # This concatenates the tags key above to add the build parameter
    sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})
    
    ###################################################################
    # Connect to Sauce Labs
    ###################################################################
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
    
    ###################################################################
    # Test logic goes here
    ###################################################################
    # Navigating to a website
    #__________________________________________________________________
    driver.get('https://www.dryzz.com')

    # Setup for finding an element and clicking it
    #__________________________________________________________________
    interact = driver.find_element_by_id('menu-item-112')
    interact.click()

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

