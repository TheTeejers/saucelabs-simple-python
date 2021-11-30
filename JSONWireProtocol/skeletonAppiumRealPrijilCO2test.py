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
# from reusableFxns import *
import requests
import random
import json
from termcolor import (colored)



androidTest = False
iosTest = False
US_Datacenter=False
EU_Datacenter=False
##################################################################
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
US_Datacenter=True
# EU_Datacenter=True

RandoNumber = random.randint(0,100000)
print(RandoNumber)

###################################################################
# Common parameters (desired capabilities)
# For Test Object tests
###################################################################
projectParameters = {
    # 'tunnelIdentifier': 'tj2',
    # 'locale' : "fr_CA",
    # 'testobject_api_key' : 'BCE49A0E8472461DBBA727592D8DE4D0',
    # On CSTEAM: # The API generated for the Test Object project
    # 'testobject_api_key' : 'B2A207D1BF6945108D0FF5EC4EB952BB', # test on voi-stage
    # 'testobject_api_key' : 'D98E6C58A01C4B3B954087B35E605C63', # test on Google website
    # 'testobject_api_key': '0DAF8BAC7F6C4AA5AB53DE3B959029B0', #prijil app
    # 'testobject_api_key' : '3483B37B52964A839B3A00B3C9C7BB83',
    # 'testobject_api_key' : '62E11503C94443CD9D76483D92D3D3F1', # test on 1Cashify app
    # 'testobject_api_key' : '37696AA9E1274A94B65339806E21A5C4', # test on Varo SIT Debug app
    # 'testobject_api_key' : '7F9F9BD657414E73A556F1AD9941C951', # test on FlashFlood iOS app
    # 'maxInstances': 5,

    'app': 'storage:ec7bacc7-c5f0-4bda-9cad-71778f7ddf0f',
    # 'newCommandTimeout': '5000',
    # 'app': 'storage:filename=BankOfTheWest_20.8.3.ipa',
    # "public": "public",
    # 'sauceLabsImageInjectionEnabled': 'true',








    # 'appiumVersion': '1.16.0',
    # 'testobject_test_live_view_url': True
    # "testobject_session_creation_timeout": "180000",
    # 'name': 'Run: ' + getNumber(),
    # "relaxedSecurityEnabled": "true",
    # "autoAcceptAlerts": True,
    # "cacheId": "test1"
}

androidParameters = { # Define Android parameters here
    # 'platformVersion' : '10',
    # 'automationName': 'uiautomator2',
    # 'deviceName' : 'Google_Pixel_2_XL_Beta_real',
    # 'deviceName' : 'Essential_PH_1_real',

    'browserName' : 'chrome',
    'deviceOrientation' : 'portrait',
    'platformName' : 'Android',
    'platformVersion' : '10',
    # 'app': 'storage:7b50a469-89f2-4d1b-ae8e-8d1997de2f2a'


    # "newCommandTimeout": "600",
    # "testobject_cache_device" :'true',
    # "reportDirectory": "reports",
    # "reportFormat": "xml",
    # "autoGrantPermissions": "true",
    # "testobject_session_creation_timeout": "300000",
    # "commandTimeouts": "180000",
    # "maxDuration": "300",
    # "idleTimeout": "300",
    # "deviceType": "phone",
    # "phoneOnly": 'true',
    # "resetKeyboard": 'true',
    # "unicodeKeyboard": 'true',
    # "ignoreUnimportantViews": 'true',
    # "disableAndroidWatchers": 'true',
    # "automationName": "uiautomator2",
    # 'maxSessions': 5,
}

iosParameters = { # Define iOS Parameters here
    'phoneOnly': 'true',
    # 'deviceName' : 'iPhone_6S_Plus_13_real_us',
    # 'deviceName' : 'iPhone X Simulator',
    # 'deviceName' : 'iPhone_11_13_real_us',
    'deviceOrientation' : 'portrait',
    # 'browserName' : 'Chrome',
    # 'browserName' : 'safari',
    'platformVersion' : '13.6',
    'platformName' : 'iOS',
    # "bundleId" : "com.apple.Preferences",
    # 'name' : "Sauce Labs Test",
    # 'testobject_suite_name': 'BOTW_Mobile_App_Automation_iOS',
    # 'testobject_test_name': "iPhone App: #{scenario.name}",
    # 'testobject_app_id': ['1'],
    'autoAcceptAlerts': 'true',
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

if US_Datacenter==True:
    print (colored('You are testing on the US Datacenter', 'green', attrs=['blink', 'underline']))
    driver = webdriver.Remote(
    # command_executor='https://us1.appium.testobject.com/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com/wd/hub',


        # command_executor='https://us1.appium.testobject.com/wd/hub',
        desired_capabilities=sauceParameters)
elif EU_Datacenter==True:
    print (colored('You are testing on the EU Datacenter', 'green', attrs=['blink', 'underline']))
    driver = webdriver.Remote(
        command_executor='https://eu1.appium.testobject.com/wd/hub',
        desired_capabilities=sauceParameters)
elif US_Datacenter==True and EU_Datacenter==True:
    print (colored('Please select either ', 'red', attrs=[ 'underline']))
    print (colored('US', 'red', attrs=['blink', 'underline', 'bold']))
    print (colored(' or ', 'red', attrs=['underline']))
    print (colored('EU', 'red', attrs=['blink', 'underline', 'bold']))
    print (colored(', not both', 'red', attrs=['underline']))


###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
#__________________________________________________________________
# driver.get_capability("testobject_test_report_url");
# driver.get_capabilities().get_capability("testobject_test_live_view_url");
# driver.desired_capabilities['testobject_test_report_url']
# print driver.capabilities['testobject_test_report_url']
print (driver.capabilities)

# console.log(driver.capabilities['testobject_test_report_url'])
# print(driver.capabilities['testobject_test_live_view_url'])
# print (colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))


# driver.set_location(30.271493, -97.6222673, 14)
# sleep(10)
# driver.launch_app(com.apple.Preferences)
# driver.activate_app("com.apple.Preferences");
#
# driver.get('https://whatismyipaddress.com/')
# interact = driver.find_element_by_name("q")
# interact.click()
# interact.send_keys('google')
# interact.submit()
# sleep(10)
# interact = driver.find_element_by_link_text('Maps')
# interact.click()

# sleep(10)
# interact = driver.find_element_by_css_selector("input[type='email']")

try:
    print (colored("looking for LoginEntryQuickbalanceButton", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "LoginEntryQuickbalanceButton")))
    interact = driver.find_element_by_accessibility_id("LoginEntryQuickbalanceButton")
    interact.click()
    print (colored("found email input", 'green'))
    print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find LoginEntryQuickbalanceButton", 'red'))
    # print (colored(interact.get_attribute('value'), 'blue'))


try:
    print (colored("looking for noThanks_btn", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'noThanks_btn')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("noThanks_btn")
    interact.click()
    print (colored("found No Thanks Button!!!", 'green'))
except:
    print (colored("Can not find noThanks_btn", 'red'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    source = driver.page_source
    interact = driver.find_element_by_class_name("noThanks_btn")
    # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
    interact.click()
    print (colored("found No Thanks Button", 'green'))


    # print(colored(source.split(' '), 'red'))
    # print (colored(interact.get_attribute('value'), 'blue'))


try:
    print (colored("looking for LoginEntryUsernameTextbox", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "LoginEntryUsernameTextbox")))
    interact = driver.find_element_by_accessibility_id("LoginEntryUsernameTextbox")
    interact.click()
    interact.send_keys("testqauser137")
    print (colored("found email input", 'green'))
except:
    print (colored("Can not find LoginEntryUsernameTextbox", 'red'))
    print (colored(interact.get_attribute('value'), 'blue'))


interact = driver.find_element_by_accessibility_id("LoginEntryPasswordTextbox")
interact.click()
interact.send_keys("Nn1234567!")

interact = driver.find_element_by_accessibility_id("LoginEntryLoginButton")
interact.click()


try:
    print (colored("looking for ALLOW NOTIFICATIONS", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'ALLOW NOTIFICATIONS')))
    interact = driver.find_element_by_accessibility_id("ALLOW NOTIFICATIONS")
    # interact.click()
    print (colored("ALLOW NOTIFICATIONS", 'green'))
    interact.click()

except:
    print (colored("Can not find ALLOW NOTIFICATIONS", 'red'))

    interact = driver.find_element_by_class_name("noThanks_btn")
    print (colored(interact.get_attribute('name'), 'blue'))
    # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
    interact.click()
    print (colored('Clicked "no thnaks"', 'blue'))
    # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "TabbarPaymentsButton")))
    interact = driver.find_element_by_accessibility_id("TabbarPaymentsButton")
    interact.click()
    print (colored("found TabbarPaymentsButton", 'green'))

try:
    print (colored("looking for LoginEntryUsernameTextbox", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "TabbarPaymentsButton")))
    interact = driver.find_element_by_accessibility_id("TabbarPaymentsButton")
    interact.click()
    print (colored("found TabbarPaymentsButton", 'green'))
except:
    print (colored("Can not find TabbarPaymentsButton", 'red'))
    source = driver.page_source
    print(colored(source.split(' '), 'red'))
    # interact = driver.find_element_by_class_name("noThanks_btn")
    # print (colored(interact.get_attribute('name'), 'blue'))
    # # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
    # interact.click()
    # print (colored('Clicked "no thnaks"', 'blue'))
    # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "TabbarPaymentsButton")))
try:
    print (colored("looking for noThanks_btn", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Transfer')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("Transfer")
    interact.click()
    print (colored("found Transfer", 'green'))
except:
    print (colored("Can not find Transfer", 'red'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    source = driver.page_source


# interact.click()
# sleep(10)
# source = driver.page_source
# print(colored(source.split(' '), 'red'))


try:
    print (colored("looking for Internal Transfer", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Make an Internal Transfer')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("Make an Internal Transfer")
    interact.click()
    print (colored("found Make an Internal Transfer", 'green'))
except:
    print (colored("Can not find Make an Internal Transfer", 'red'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    source = driver.page_source

try:
    print (colored("looking for Amount", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'Amount')))
    print (colored("found Amount", 'green'))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("Amount")
    interact.click()
    sleep(5)
    interact = driver.find_element_by_name("1")
    interact.click()
    interact = driver.find_element_by_name("0")
    interact.click()
    interact = driver.find_element_by_name("0")
    interact.click()
    interact = driver.find_element_by_name("Done")
    interact.click()
    print (colored("Entered 100", 'green'))
except:
    print (colored("Can not find Amount", 'red'))
    names = driver.find_elements_by_xpath(".//*")
    print (colored(driver.contexts, 'blue'))
    # print(colored(names.get_attribute(), 'green'))
    source = driver.page_source
# interact = driver.find_element_by_css_selector("//*XCUIElementTypeButton[@name='password']")
# interact.click()
# interact.send_keys('test1234')
# interact = driver.find_element_by_css_selector("[id='button__login']")
# interact.click()
try:
    print (colored("looking for CONTINUE", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'CONTINUE')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("CONTINUE")
    sleep(2)
    interact.click()
    print (colored("clicked CONTINUE", 'green'))
    interact = driver.find_element_by_name("Submit")
    sleep(2)
    interact.click()
    print (colored("clicked Submit", 'green'))
    print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find CONTINUE", 'red'))
    print (colored(driver.contexts, 'blue'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    source = driver.page_source

try:
    print (colored("looking for Submit", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Submit')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("Submit")
    sleep(2)
    interact.click()
    print (colored("clicked Submit", 'green'))
    print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find Submit", 'red'))
    print (colored(driver.contexts, 'blue'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    source = driver.page_source


try:
    print (colored("looking for Not Now", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'Not Now')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_id("Not Now")
    sleep(2)
    interact.click()
    print (colored("clicked Not Now", 'green'))
    print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find Not Now", 'red'))
    print (colored(driver.contexts, 'blue'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    # source = driver.page_source

try:
    print (colored("looking for Schheduled", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'Scheduled')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")

    print (colored("Found Scheduled", 'green'))
    print (colored(driver.contexts, 'blue'))
    webview = driver.contexts[1]
    driver.switch_to.context(webview)
    source = driver.page_source

except:
    print (colored("Can not find Scheduled", 'red'))
    print (colored(driver.contexts, 'blue'))
    source = driver.page_source

    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))


try:
    print (colored("looking for transfer-done-button", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'transfer-done-button')))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    interact = driver.find_element_by_name("transfer-done-button")
    sleep(2)
    interact.click()
    print (colored("clicked transfer-done-button", 'green'))
    sleep(2)
    interact.click()
    print (colored("clicked transfer-done-button", 'green'))
    print (colored(driver.contexts, 'blue'))


except:
    print (colored("Can not find transfer-done-button", 'red'))
    print (colored(driver.contexts, 'blue'))
    webview = driver.contexts[1]
    driver.switch_to.context(webview)
    print (colored("looking for transfer-done-button", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'transfer-done-button')))
    interact = driver.find_element_by_name("transfer-done-button")
    sleep(2)
    interact.click()
    print (colored("clicked transfer-done-button", 'green'))
    sleep(2)
    interact.click()
    print (colored("clicked transfer-done-button", 'green'))
    print (colored(driver.contexts, 'blue'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
    # source = driver.page_source


sleep(10)
source = driver.page_source
print(colored(source.split(' '), 'red'))
# print "searching for update button"
# wait.until(ExpectedConditions.alertIsPresent());
# Alert = driver.switch_to_alert();
# interact = driver.find_element_by_class_name('gLFyf')
# interact.click()
# interact.send_keys('Sauce Labs')
# sleep(10)
# driver.hide_keyboard()
# sleep(10)


# interact = driver.find_element_by_id("rvZoneOnboarding")
# interact.click()
# print("clicked 'rvZoneOnboarding'")
#
# interact = driver.find_element_by_id("rvZoneOnboarding")
# interact.click()
# print("clicked 'rvZoneOnboarding'")



#
# names = driver.find_elements_by_xpath(".//*")
# print(colored(names, 'green'))
# source = driver.page_source
#
#
# print(colored(source.split(' '), 'red'))
#
# for i in range(len(source.split(' '))):
#     # if len(source.split(' ')[i]) > 0:
#     # if source.split(' ')[i][0] == 'r' and source.split(' ')[i][1] == 'e':
#     if len(source.split(' ')[i]) > 0 and source.split(' ')[i][0] == 'r' and source.split(' ')[i][1] == 'e':
#         # print('things:    ', len(source.split(' ')[i]))
#         print('ID:    ', source.split(' ')[i])
#     elif len(source.split(' ')[i]) > 0 and source.split(' ')[i][0] == 'c' and source.split(' ')[i][2] == 'a':
#         # print('things:    ', len(source.split(' ')[i]))
#         print('CLASS:    ', source.split(' ')[i])

# resource-id="com.supplyshift.supplyshift_demo:id/versionTextView"
# ids = driver.find_elements_by_xpath('.//*')
# for ii in ids:
    # print (colored("name: ", 'blue',  ii.get_attribute('name')))
    # print (colored("class: ", ii.get_attribute('class'), 'yellow'))
    # print (colored("id: ", ii.get_attribute('id'), 'magenta'))
    # print (colored(ii.get_attribute('class'), 'magenta'))
driver.get_screenshot_as_base64()

# interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='LOG IN']")
# interact.click()
# interact = driver.find_element_by_xpath("//XCUIElementTypeTextField").click()
# interact.send_keys(94597)
#
# interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"new login checkbox\"]").click()
#
# interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()



# interact = driver.find_element_by_accessibility_id('QA').click()
# print "opening login screen"
# # interact = driver.find_element_by_id('com.taxact.express2013.test:id/tv_title')
# driver.execute_script("mobile: scroll", {"direction": "right"})
# sleep(2)
# driver.execute_script("mobile: scroll", {"direction": "right"})
# sleep(2)
# driver.touchAction({ actions: 'tap', x: 188, y: 685 });
#
# # interact = driver.find_element_by_accessibility_id('Email Address').click()
# # print "email selected"
#
# interact = driver.find_element_by_accessibility_id('Email Address').send_keys('karltonrn+20@gmail.com')
# print "email entered"
#
# # interact = driver.find_element_by_accessibility_id('Password').click()
# # print "password selected"
#
# interact = driver.find_element_by_accessibility_id('Password').send_keys('Lemonlime')
# print "password entered"
#
# interact = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='FoodsbyTest']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
# print "log in button tapped"
#
# sleep(15)
# # alert = driver.switch_to_alert().accept()
# interact = driver.find_element_by_link_text('Allow').click()
# print "allow button tapped"
# sleep(15)
#
#
# interact = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='FoodsbyTest']/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeNavigationBar[@name='Consumer.DeliveryView']/XCUIElementTypeStaticText/XCUIElementTypeOther/XCUIElementTypeButton[name='onboarding profile]").click()
# print "profile button tapped"



# print "slept 1"
# TouchAction(driver).press(x=712, y=782).wait(1000).move_to(x=96, y=796).release().perform()
# sleep(20)
# print "slept 2"
# TouchAction(driver).press(x=712, y=782).wait(1000).move_to(x=96, y=796).release().perform()
# sleep(10)
# print "slept 3"
# TouchAction(driver).press(x=712, y=782).wait(1000).move_to(x=96, y=796).release().perform()
# actions = TouchAction(driver)
# actions.press(body.id, x=144, y=2048)
# actions.move_to(x=1296, y=2048)
# actions.release()
# actions.perform()


# Setup for finding an element and clicking it
#__________________________________________________________________
# interact = driver.find_element_by_id('com.taxact.express2013.test:id/tv_title')
# interact.click()

# Setup for finding an element and sending keystrokes
#__________________________________________________________________
# interact = driver.find_element_by_class_name('XCUIElementTypeTextField').click()
# interact.send_keys('tmdeqatest014@wholefoods.com')
# interact.submit()
#
# sleep(15)
#
# interact = driver.find_element_by_class_name('XCUIElementTypeTextField').click()
# interact.send_keys('XZm6Q+RR_1DX')
# interact.submit()
#
# sleep(30)

# Setup for using random Python commands
#__________________________________________________________________
# driver.save_screenshot('screenshot.png')
# sleep(30)
# print('Message')

# Setup for using Action chains
#__________________________________________________________________
# ActionChains(driver).move_to_element(interact).perform()

# Setup for random script executions
#__________________________________________________________________
# driver.execute_script('sauce: break')
# driver.execute_script('sauce:context=Place words here for notes')

# # this is all a test for 'testobject_api_key' : '7F9F9BD657414E73A556F1AD9941C951', # test on FlashFlood iOS app
# email = 'test@test.com'
#
# try:
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "Email")))
#     interact = driver.find_element_by_accessibility_id("Email")
#     print (colored("found email input", 'green'))
# except:
#     print (colored("Can not find email input", 'red'))
#
#     interact.send_keys(email)
#
#     print (colored(interact.get_attribute('value'), 'blue'))
# emailValueUincode = interact.get_attribute('value')
# emailString = emailValueUincode.encode("utf-8")
#
# print (colored(emailString, 'red'),)
# print type(emailString),
# print (colored(email, 'magenta'),)
# print type(email)
# # Updating the test to pass/fail via the API
# #__________________________________________________________________
# if emailValueUincode.encode("utf-8") == email:
#     print "passed"
#     requests.put(
#         'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
#         headers = { 'Content-Type': 'application/json',},
#         data = '{"passed": true}', # Update this to pass either True or False depending on your requirements
#     ),
#
# else:
#     print "failed"
#     requests.put(
#         'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
#         headers = { 'Content-Type': 'application/json',},
#         data = '{"passed": false}' # Update this to pass either True or False depending on your requirements
#     ),

# print('https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/')
# print("testobject_device_session_id=  " + driver.capabilities['testobject_device_session_id'])
# print("session_id=  " + driver.session_id)

# Ending the test session
#__________________________________________________________________
driver.quit()
