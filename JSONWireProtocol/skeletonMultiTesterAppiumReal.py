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

run = 10
multiCaps =[
{ # Define iOS Parameters here
    # 'deviceName' : 'iPhone 8 Simulator',
    # 'deviceOrientation' : 'portrait',
    'browserName' : 'safari',
    'platformVersion' : '12',
    'platformName' : 'iOS',
    # 'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
    'browserName' : 'safari',


},
{ # Define iOS Parameters here
    # 'deviceName' : 'iPhone 12 Pro Max Simulator',
    # 'deviceOrientation' : 'portrait',
    'browserName' : 'safari',
    'platformVersion' : '14',
    'platformName' : 'iOS',
    # 'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
    'browserName' : 'safari',

}
]
print (len(multiCaps))

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

# androidTest = True
iosTest = True


###################################################################
# Declare as a function in order to do multiple runs
###################################################################
projectParameters = {
    # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63', # The API generated for the Test Object project
    # 'appiumVersion': '1.8.1',
    # 'nativeWebTap': True,
    # 'name': 'Run: ' + getNumber(),
    # 'maxInstances': 10,
    # 'privateDevicesOnly': 'false'

}
sauceParameters = {}
iosParameters1 = { # Define iOS Parameters here
    # 'deviceName' : 'iPhone 8 Simulator',
    # 'deviceOrientation' : 'portrait',
    'browserName' : 'safari',
    'platformVersion' : '12',
    'platformName' : 'iOS',
    # 'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
    'browserName' : 'safari',


}

iosParameters2 = { # Define iOS Parameters here
    # 'deviceName' : 'iPhone 12 Pro Max Simulator',
    # 'deviceOrientation' : 'portrait',
    'browserName' : 'safari',
    'platformVersion' : '14',
    'platformName' : 'iOS',
    # 'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
    'browserName' : 'safari',

}
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
    print('iOS')
    sauceParameters.update()
    # sauceParameters.update(iosParameters2)
def run_sauce_test():
    testObjectAppStorage = {

    }

    unifiedPlatformAppStorage = {
        # 'app': 'storage:filename=BankOfTheWest.ipa',
        # 'app': 'storage:264d3821-e02c-4aa6-a678-e9df4f164d9e', #bersa-uat
    }
    ###################################################################
    # Common parameters (desired capabilities)
    # For Test Object tests
    ###################################################################
    # projectParameters = {
    #     # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63', # The API generated for the Test Object project
    #     # 'appiumVersion': '1.8.1',
    #     # 'nativeWebTap': True,
    #     # 'name': 'Run: ' + getNumber(),
    #     # 'maxInstances': 10,
    #     # 'privateDevicesOnly': 'false'
    #
    # }

    androidParameters = { # Define Android parameters here
        'deviceName' : 'Google Pixel',
        # 'platformVersion' : '9',
        # 'browserName' : 'Chrome',
        # 'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
        # 'maxSessions': 1,

    }

    androidParameters1 = { # Define Android parameters here
        'deviceName' : 'Samsung.*',
        # 'platformVersion' : '9',
        # 'browserName' : 'Chrome',
        # 'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
        # 'maxSessions': 1,

    }

    # iosParameters1 = { # Define iOS Parameters here
    #     # 'deviceName' : 'iPhone 8 Simulator',
    #     # 'deviceOrientation' : 'portrait',
    #     'browserName' : 'safari',
    #     'platformVersion' : '12.2',
    #     'platformName' : 'iOS',
    #     # 'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
    #     'browserName' : 'safari',
    #
    #
    # }

    # iosParameters2 = { # Define iOS Parameters here
    #     # 'deviceName' : 'iPhone 12 Pro Max Simulator',
    #     # 'deviceOrientation' : 'portrait',
    #     'browserName' : 'safari',
    #     'platformVersion' : '14',
    #     'platformName' : 'iOS',
    #     # 'app':'storage:filename=Simulator_Indeed_Jobs_QA2.zip'
    #     'browserName' : 'safari',
    #
    # }

    ###################################################################
    # Merge parameters into a single capability dictionary
    ###################################################################

    # sauceParameters = {}
    # sauceParameters.update(projectParameters)
    # if androidTest != True and iosTest != True:
    #     print('You need to specify a platform to test on!')
    #     sys.exit()
    # elif androidTest == True and iosTest == True:
    #     print('Don\'t be greedy! Only choose one platform!')
    #     sys.exit()
    # elif androidTest:
    #     sauceParameters.update(androidParameters),
    #     sauceParameters.update(androidParameters1),
    #     print(run)
    # elif iosTest:
    #     print('iOS')
    #     sauceParameters.update()
    #     # sauceParameters.update(iosParameters2)

    ###################################################################
    # Connect to Test Object (RDC Cloud)
    ###################################################################
    if US_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You are testing on the Sauce Labs US Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+' @ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://tj.invitationtest1:24168dc8-0900-4994-9ef9-f3442fb9683a@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
            # command_executor='https://<user>.<access_key>.us-west-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    elif EU_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You are testing on the Sauce Labs EU Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+' @ondemand.eu-central-1.saucelabs.com:443/wd/hub',
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
    # driver.get('https://www.dryzz.com')
    driver.get('https://www.childrensplace.com/ca/home')
    # # interact = driver.find_element_by_name("q")
    # # interact.click()
    # # interact.send_keys('google')
    # # interact.submit()
    # # sleep(10)
    # # interact = driver.find_element_by_link_text('Maps')
    # # interact.click()
    #
    # sleep(100)
    try:
        print (colored("looking for Page", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "storelocatorlink__img")))
        # interact = driver.find_element_by_accessibility_id("I already have an account")
        # interact.click()
        print (colored("found page storelocatorlink__img", 'green'))
        # print (colored(driver.contexts, 'blue'))
    except:
        print (colored("Not loaded storelocatorlink__img", 'red'))

    # Setup for finding an element and clicking it
    #__________________________________________________________________
    # interact = driver.find_element_by_id('menu-item-112')
    # interact.click()

    # Setup for finding an element and sending keystrokes
    #__________________________________________________________________
    # interact = driver.find_element_by_class_name('figure')
    # interact.send_keys('Dryzz')
    # interact.submit()

    # Setup for using random Python commands
    #__________________________________________________________________
    # driver.save_screenshot('screenshot.png')
    # sleep(20)
    # print('Message')

    # Setup for using Action chains
    #__________________________________________________________________
    # ActionChains(driver).move_to_element(interact).perform()

    # Setup for random script executions
    #__________________________________________________________________
    # driver.execute_script('sauce: break')
    # driver.execute_script('sauce:context=Place words here for notes')

    # Updating the test to pass/fail via the API
    #__________________________________________________________________
    # requests.put(
    #     'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
    #     headers = { 'Content-Type': 'application/json',},
    #     data = '{"passed": true}' # Update this to pass either True or False depending on your requirements
    # )


    print (driver.current_url)
    sauce_result = "failed" if str(driver.current_url) == 'https://www.gymboree.com/ca/home' else "passed"
    driver.execute_script("sauce:job-result={}".format(sauce_result))
    # Ending the test session
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
        if i == 4:
            sauceParameters.update(iosParameters1)
        else:
            sauceParameters.update(iosParameters2)
        jobRun.start() #Start the functions.
        print('this is the run for: '+ str(i))
