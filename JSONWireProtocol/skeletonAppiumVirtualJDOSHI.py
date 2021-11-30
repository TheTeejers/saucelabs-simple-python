###################################################################
# Skeleton for Appium Virtual Tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
import sys
import os
import datetime
from termcolor import colored
androidTest = False
import multiprocessing

# from reusableFxns import *
iosTest = False
useApp = False

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

# androidTest = True
iosTest = True


###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################

region = 'US'
# region = 'EU'

###################################################################
# Uncomment if this is an app test
# Add in the location to the stored app too
###################################################################

useApp = True
# appLocation = 'https://github.com/truongsinh/android_flutter_host/releases/download/0.0.1/app-free-debug.apk'
# appLocation = 'maps'
# appLocation = 'https://mobile-app-archive-prod-us-east-1.s3.amazonaws.com/Android/release/Tasty_QA_11858/1480002_1.48.0-QA/Tasty-1.48.0-QA-RC.apk'
appLocation = 'storage:filename=Simulator_Indeed_Jobs_QA1.zip'

# appLocation = 'storage:25e76be0-bc67-49d1-a785-a22bfd0e1d90'
# appLocation = 'storage:f9232cab-fb1c-4340-b3f9-e3d8f2398abb'
# appLocation = 'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'
# 'app': 'storage:f5988b56-89f1-4db8-b9a8-d4e2a8f0887c', #ios smartsheets
# 'app': 'storage:59549449-8b97-47c5-9343-f76799cc4fe4', #android smartsheets
# 'app':'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'




###################################################################
# Common parameters (desired capabilities)
# For Test Object tests
###################################################################

run = 1

###################################################################
# Declare as a function in order to do multiple runs
###################################################################


projectParameters = {
    'tags':['https://www.gymboree.com/ca/home'],
    # 'appiumVersion': '1.18.1',
    'name': 'Testing URL at Run Time: ' + str(datetime.datetime.now()),
    'commandTimeout': 200,
    "idleTimeout": 200,
    # 'name': 'Testing App ' + appLocation +' at Run Time: ' + str(datetime.datetime.now()),
    # "timeZone": "Alaska",
    # 'sauce:throttleNetwork': 'offline',
    # 'tunnelIdentifier': 'tj1',
    # 'appWaitActivity': "*, .*",
    # 'isHeadless': True,
# 'sauce:options':{

    # 'extendedDebugging':'true',

    # },
# },
    # 'autoAcceptAlerts':'true',
    # 'locationServicesEnabled': True,
    # 'locationServicesAuthorized': True,
    # 'extendedDebugging': 'true',
    # 'capturePerformance': 'true',
    # # 'pageLoadStrategy': 'eager',
    # 'nativeEvents': 'true',
    # 'sendKeyStrategy': 'setValue',
    # 'appiumVersion': '1.9.1',
    # 'resetKeyboard': 'true',
    # 'useJSONSource': 'true',
    # 'clearSystemFiles':'true',

}

androidParameters = { # Define Android parameters here
    'deviceOrientation' : 'portrait',
    # 'relaxedSecurityEnabled': True,
    # 'autoGrantPermissions': True,
    # 'ignoreUnimportantViews': True,
    'automationName': 'UiAutomator2',
    # 'gpsEnabled': True,
    # 'maxDuration': 10800,
    # 'recordScreenshots': False
    # 'browserName': '',
    # 'platformVersion': 'latest',
    'apppackage':'com.buzzfeed.tasty',
    "appActivity":".LauncherActivity",
    'deviceName': 'Android GoogleAPI Emulator',
    'platformVersion': '11',
    'platformName': 'Android',
    # 'gpsEnabled': False


}

iosParameters = { # Define iOS Parameters here

    # 'deviceName' : 'iPhone X Simulator',
	"automationName": "XCuiTest",
	"newCommandTimeout": 60,
	"deviceOrientation": "portrait",
	"deviceName": "iPhone 8 Simulator",
	"nativeWebScreenshot": True,
	# "platformVersion": "14.0",
	"platformVersion": "12.2",
    'platformName' : 'iOS',
    # 'avoidProxy': True,
    # 'platformName' : 'iOS',
    # 'autoWebview': 'true',
    # 'bundleId': 'com.apple.Maps',
    # 'browserName': 'safari',
    # 'nativeWebTap': True, # iOS only capability.
    # 'autoAcceptAlerts': True,
    # 'locationServicesEnabled': True,
    # 'locationServicesAuthorized': True

}

###################################################################
# Merge parameters into a single capability dictionary
###################################################################

sauceParameters = {}
sauceParameters.update(projectParameters)
# This concatenates the tags key above to add the build parameter
# print ('name : Run: ' + str(datetime.datetime.now()))

if androidTest != True and iosTest != True:
    print('You need to specify a platform to test on!')
    sys.exit()
elif androidTest == True and iosTest == True:
    print('Don\'t be greedy! Only choose one platform!')
    sys.exit()
elif androidTest:
    sauceParameters.update(androidParameters)

    if useApp:
        sauceParameters['app'] = appLocation
        sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['platformVersion'] + ' device: ' + sauceParameters['deviceName']})  # Use app if it's specified
    else:
        sauceParameters['browserName'] = 'Chrome' # Otherwise use Chrome
        #Note! Replace 'Chrome' with 'Browser' for older versions of Android to use the stock browser
        sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['platformVersion'] + ' device: ' + sauceParameters['deviceName']})

elif iosTest:
    sauceParameters.update(iosParameters)

    if useApp:
        sauceParameters['app'] = appLocation
        sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['platformVersion'] + ' device: ' + sauceParameters['deviceName']})
    else:
        sauceParameters['browserName'] = 'safari'
        # sauceParameters['browserName'] = 'safari'
        sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['platformVersion'] + ' device: ' + sauceParameters['deviceName']})

# print colored("Testing on " + str(sauceParameters['platformName']) + ' ' + str(sauceParameters['deviceName']), 'green')


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
        # command_executor='https://jaxon.lee:f7958d00-80d2-413b-8bb2-2c86fa1bd419@ondemand.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://sso-buzzfeed-gabriela.conde-moreau:a784696d-665e-4173-a597-cedb42cc8b2a@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',

        desired_capabilities=sauceParameters)
elif region == 'EU':
    # print (colored("You are using the EU data center", 'green'))
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

# ###################################################################
# # Test logic goes here
# ###################################################################

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


driver.quit()


# if __name__ == '__main__' and region == 'US':
#     jobs = [] # Array for the jobs
#     print(colored(str(run) +" Tests running in the US data center.", 'green'))
#     for i in range(run): # Run the amount of times set above
#         jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
#         jobs.append(jobRun) # Add to the array.
#         jobRun.start() # Start the functions.
#         # print('this is the run for: '+ str(i))
#         # sauceParameters.update({'name': 'Run ' + str(i) +': ' + str(datetime.datetime.now())})
#         # print("You are using the US data center on run " + str(i))
# elif __name__ == '__main__' and region != 'US':
#     jobs = [] # Array for the jobs
#     print(colored(str(run) +" Tests running in the EU data center.", 'green'))
#     for i in range(run): # Run the amount of times set above
#         jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
#         jobs.append(jobRun) # Add to the array.
#         jobRun.start()
