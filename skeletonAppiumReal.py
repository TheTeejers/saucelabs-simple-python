####################################################################
# Skeleton for Appium RDC tests on Test Object
####################################################################


###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import sys
from reusableFxns import *
androidTest = False
iosTest = False

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

# androidTest = True
# iosTest = True


###################################################################
# Common parameters (desired capabilities)
# For Test Object tests
###################################################################
projectParameters = {
    'testobject_api_key' : 'APIKEY', # The API generated for the Test Object project
    'appiumVersion': '1.8.1',
    'name': 'Run: ' + getNumber(),
}

androidParameters = { # Define Android parameters here
    'deviceName' : 'Google Pixel',
    'platformVersion' : '9',
    'browserName' : 'Chrome',
    'deviceOrientation' : 'portrait',
    'platformName' : 'Android',
}

iosParameters = { # Define iOS Parameters here
    'deviceName' : 'iPhone X',
    'deviceOrientation' : 'portrait',
    'browserName' : 'safari',
    'platformVersion' : '12',
    'platformName' : 'iOS',
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
elif iosTest:
    sauceParameters.update(iosParameters)

###################################################################
# Connect to Test Object (RDC Cloud)
###################################################################
driver = webdriver.Remote(
    command_executor='https://us1.appium.testobject.com/wd/hub',
    #command_executor='https://eu1.appium.testobject.com/wd/hub',
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


