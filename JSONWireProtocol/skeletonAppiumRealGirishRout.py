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


androidTest = False
iosTest = False
US_Datacenter=False
EU_Datacenter=False
US_Datacenter_TO=False
EU_Datacenter_TO=False

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

###################################################################
# Choose The Platform and Data Center you want to test on
# Uncomment one of those lines
###################################################################
US_Datacenter=True
# EU_Datacenter=True

# US_Datacenter_TO=True
# EU_Datacenter_TO=True


RandoNumber = random.randint(0,100000)
# print(RandoNumber)

###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################
run = 1


###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################
# androidTest = True
# iosTest = True

###################################################################
# Declare as a function in order to do multiple runs
###################################################################
def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Test Object tests
    ###################################################################
    projectParameters = {
        'name': 'Run: ' + str(datetime.datetime.now()),
        'commandTimeout':600,
        # "recordDeviceVitals": 'true',
        # 'tunnelIdentifier': 'tj1',
        # 'locale' : "fr_CA",


        # On CSTEAM: # The API generated for the Test Object project

        # 'sauce:options': {
        #   'appiumVersion': '1.20.1',
        #   'name': 'Run: ' + str(datetime.datetime.now()),
        #
        # },


        # "public": "public",
        # "appiumVersion":"1.17.1",
        # 'tunnelIdentifier':'try1tj'

        # 'sauceLabsImageInjectionEnabled': 'true',

        'wdaEventloopIdleDelay': '5',
        "waitForQuiescence": False,

        # "cacheId": "1234",
        # "noReset": "true",






        # 'appiumVersion': '1.16.0',
        # 'testobject_test_live_view_url': True
        # "testobject_session_creation_timeout": "180000",
        # 'name': 'Run: ' + getNumber(),
        # "relaxedSecurityEnabled": "true",
        # "autoAcceptAlerts": True,
        # "cacheId": "test1"
    }

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

    androidParameters = { # Define Android parameters here
        'platformVersion' : '10',
        # 'automationName': 'uiautomator2',
        # 'deviceName' : 'Samsung.*',
        # 'deviceName' : 'Samsung Galaxy S[1-2]0.*',
        # 'deviceName' : 'Samsung_Galaxy_S[1-2]0_real',
        # 'deviceName' : 'Google_Pixel_4_XL_real_us',

        'browserName' : 'chrome',
        'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
        # 'platformVersion' : '9',
        # "recordDeviceVitals": 'true',
        # 'app': 'storage:7b50a469-89f2-4d1b-ae8e-8d1997de2f2a'
        # 'testobject_app_id': '9',
        # 'appID': '10',

        # "newCommandTimeout": "7000",
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
        # 'deviceName' : 'iPhone_11_14_real_us',
        # 'deviceName' : 'iPhone X Simulator',
        # 'deviceName' : 'iPhone_11_13_real_us',
        'deviceOrientation' : 'portrait',
        # 'browserName' : 'Chrome',
        # 'browserName' : 'safari',
        # 'platformVersion' : '13',
        # 'platformVersion' : '14',
        'appium:platformVersion': '14',
        'platformName' : 'iOS',
        # "recordDeviceVitals": 'true',
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

    elif US_Datacenter==True and EU_Datacenter==True:
        print (colored('Please select either ', 'red', attrs=[ 'underline']))
        print (colored('US', 'red', attrs=['blink', 'underline', 'bold']))
        print (colored(' or ', 'red', attrs=['underline']))
        print (colored('EU', 'red', attrs=['blink', 'underline', 'bold']))
        print (colored(', not both', 'red', attrs=['underline']))


    print (driver.capabilities)


    print ('Test Name == ', colored(driver.capabilities['testobject_test_name'], 'green', attrs=['reverse', 'blink']))
    print ('Device Name == ', colored(driver.capabilities['testobject_device_name'], 'green', attrs=['reverse', 'blink']))
    print ('Device descriptor == ', colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))
    print ('Platform Version == ', colored(driver.capabilities['platformVersion'], 'green', attrs=['reverse', 'blink']))
    # ###################################################################
    # # Test logic goes here
    # ###################################################################
    # # Navigating to a website
    # #__________________________________________________________________
    # # driver.get_capability("testobject_test_report_url");
    # # driver.get_capabilities().get_capability("testobject_test_live_view_url");
    # # driver.desired_capabilities['testobject_test_report_url']
    # # print driver.capabilities['testobject_test_report_url']
    #
    # # console.log(driver.capabilities['testobject_test_report_url'])
    # # print(driver.capabilities['testobject_test_live_view_url'])
    # sleep(10)
    # source = driver.page_source
    # print(colored(source.split(' '), 'red'))
    # driver.execute_script('sauce:context=Open google.com')

    # driver.get("https://se2sbl-qa-uatx.unqork.io/?style=se2sblterm#/display/6008fa52e78d1d025ae63209?firstName=John&lastName=Smith&email=john@testemail.com")
    # driver.execute_script('sauce:context=names ' + str(driver.capabilities['platformVersion']) + ' yup')
    driver.get("https://app.qa.everlylife.io/app/termlifewf#/")

    # try:
    #     print (colored("looking for btnGetStarted", 'green'))
    #     WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"btnGetStarted\"]/span")))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_xpath("//*[@id=\"btnGetStarted\"]/span")
    #     interact.click()
    #     print (colored("found btnGetStarted!!!", 'green'))
    #
    # except:
    #     print (colored("Can not find btnGetStarted", 'red'))

    try:
        print (colored("looking for username and password", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'username')))
        show = EC.presence_of_element_located((By.ID, 'username'))
        print (show)
        interact = driver.find_element_by_id("username")
        interact.click()
        print (colored("found username!!!", 'green'))
        interact.send_keys("Srinatha.gangadharaiah+Automation@unqork.com")
        print (colored("looking for password", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
        interact = driver.find_element_by_id("password")
        interact.click()
        print (colored("found password!!!", 'green'))
        interact.send_keys("Automation123")
        interact.submit()
    except:
        print (colored("Can not find username and password", 'red'))

    # try:
    #     print (colored("looking for password", 'green'))
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    #     interact = driver.find_element_by_id("password")
    #     interact.click()
    #     print (colored("found password!!!", 'green'))
    #     interact.send_keys("Automation123")
    #     interact.submit()
    # except:
    #     print (colored("Can not find password", 'red'))


    try:
        print (colored("looking for remove", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Remove ']")))
        print (colored("found remove!!!", 'green'))
        interact = driver.find_element_by_xpath("//button[text()=' Remove ']")
        interact.click()
        print (colored("clicked remove!!!", 'green'))

    except:
        print (colored("Can not find remove", 'red'))



    try:
        print (colored("looking for insuredFirstName", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredFirstName\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        if EC.presence_of_element_located((By.XPATH, "//button[text()=' Remove ']")) == True:
            interact = find_element_by_xpath("//button[text()=' Remove ']")
            interact.click()
            print ("remove removed")

        else:
            print ("remove not here")
        interact = driver.find_element_by_xpath("//*[@id=\"insuredFirstName\"]")
        interact.click()
        interact.clear()
        print (colored("found insuredFirstName!!!", 'green'))
        interact.send_keys("Nineteen AL")


    except:
        print (colored("Can not find insuredFirstName", 'red'))

    try:
        print (colored("looking for insuredLastName", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredLastName\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[@id=\"insuredLastName\"]")
        interact.click()
        interact.clear()
        print (colored("found insuredLastName!!!", 'green'))
        interact.send_keys("Moore")


    except:
        print (colored("Can not find insuredLastName", 'red'))

    try:
        print (colored("looking for insuredDOB", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredDOB\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[@id=\"insuredDOB\"]")
        interact.click()
        interact.clear()
        print (colored("found insuredDOB!!!", 'green'))
        interact.send_keys("11162001")


    except:
        print (colored("Can not find insuredDOB", 'red'))

    try:
        print (colored("looking for Male", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),\"Male\")]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[contains(text(),\"Male\")]")
        interact.click()
        # interact.clear()
        print (colored("found Male!!!", 'green'))
        # interact.send_keys("11162001")


    except:
        print (colored("Can not find Male", 'red'))

    # try:
    #     print (colored("looking for Search...", 'green'))
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Search...']")))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_xpath("//div[text()='Search...']")
    #     interact.click()
    #     # interact.clear()
    #     print (colored("found Search...!!!", 'green'))
    #     # interact.send_keys("11162001")
    #
    #
    # except:
    #     print (colored("Can not find Search...", 'red'))

    # try:
    #     print (colored("looking for react-select-2-input", 'green'))
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-select-2-input\"]")))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_xpath("//*[@id=\"react-select-2-input\"]")
    #     interact.click()
    #     interact.clear()
    #     print (colored("found react-select-2-input!!!", 'green'))
    #     interact.send_keys("2201 University Blvd, Tuscaloosa, AL 35401")
    #
    #
    # except:
    #     print (colored("Can not find react-select-2-input", 'red'))

    try:
        print (colored("looking for hiddenAddressLine1", 'green'))
        # print (colored("looking for react-select-2-input", 'green'))
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-select-2-input\"]")))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"hiddenAddressLine1\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        print (colored("looking for hiddenAddressLine1", 'green'))
        interact = driver.find_element_by_xpath("//*[@id=\"hiddenAddressLine1\"]")
        print (colored("found hiddenAddressLine1", 'green'))

        interact.click()
        interact.send_keys("7000 N Mopac")
        print (colored("looking for insuredCity", 'green'))
        interact = driver.find_element_by_xpath("//*[@id=\"insuredCity\"]")
        interact.click()
        interact.send_keys("Austin")
        print (colored("looking for insuredState", 'green'))
        interact = driver.find_element_by_xpath("//*[@id=\"insuredState\"]")
        interact.click()
        interact.send_keys("Texas")
        print (colored("looking for insuredPostalCode", 'green'))
        interact = driver.find_element_by_xpath("//*[@id=\"insuredPostalCode\"]")
        interact.click()
        interact.send_keys("78754")
        # print (colored("found react-select-2-input!!!", 'green'))
        # interact = driver.find_element_by_xpath("//*[@id=\"react-select-2-input\"]")
        # print (colored("found react-select-2-input!!!", 'green'))
        #
        # # interact.click()
        # # print (colored("clicked react-select-2-input!!!", 'green'))
        #
        # # interact.clear()
        # print (colored("cleared react-select-2-input!!!", 'green'))
        # interact.send_keys("2201 University Blvd, Tuscaloosa, AL 35401")
        # interact.submit()


    except:
        # print (colored("Can not find react-select-2-input", 'red'))
        print (colored("looking for hiddenAddressLine1", 'green'))
        # interact = driver.find_element_by_xpath("//*[@id=\"hiddenAddressLine1\"]")
        # interact.click()
        # interact.send_keys("7000 N Mopac")
        # print (colored("looking for insuredCity", 'green'))
        # interact = driver.find_element_by_xpath("//*[@id=\"insuredCity\"]")
        # interact.click()
        # interact.send_keys("Austin")
        # print (colored("looking for insuredState", 'green'))
        # interact = driver.find_element_by_xpath("//*[@id=\"insuredState\"]")
        # interact.click()
        # interact.send_keys("Texas")
        # print (colored("looking for insuredPostalCode", 'green'))
        # interact = driver.find_element_by_xpath("//*[@id=\"insuredPostalCode\"]")
        # interact.click()
        # interact.send_keys("78754")

    try:
        print (colored("looking for insuredMobilePhone", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredMobilePhone\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[@id=\"insuredMobilePhone\"]")
        print ('before click mobile phone number Value is ' + interact.get_attribute("value"))

        interact.click()
        print ('after click mobile phone number Value is ' + interact.get_attribute("value"))

        interact.clear()
        print ('after clear mobile phone number Value is ' + interact.get_attribute("value"))
        # print (interact.get_attribute("value"))
        interact.click()
        print ('after click mobile phone number Value is ' + interact.get_attribute("value"))

        print (colored("found insuredMobilePhone!!!", 'green'))
        interact.send_keys("6466717203")
        print ('after send keys all mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("4")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("4")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("6")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("6")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("1")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("7")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("1")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("2")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("0")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("3")
        # # sleep(5)
        # print (interact.attribute(value))
        print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))

    except:
        print (colored("Can not find insuredMobilePhone", 'red'))

    try:
        print (colored("looking for insuredSSN", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredSSN\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[@id=\"insuredSSN\"]")
        print ('before click SSN Value is ' + interact.get_attribute("value"))

        interact.click()
        print ('after click SSN Value is ' + interact.get_attribute("value"))

        interact.clear()
        print ('after clear SSN Value is ' + interact.get_attribute("value"))

        print (colored("found insuredSSN!!!", 'green'))
        interact.send_keys("646671720")
        print ('after send keys all mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("6")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("4")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("6")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("6")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("1")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("7")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("1")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("2")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))
        # interact.send_keys("0")
        # print ('after send keys 1 mobile phone number Value is ' + interact.get_attribute("value"))

        print ('after send keys SSN Value is ' + interact.get_attribute("value"))


    except:
        print (colored("Can not find insuredSSN", 'red'))

    try:
        print (colored("looking for insuredEmail", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredEmail\"]")))
        interact = driver.find_element_by_xpath("//*[@id=\"insuredEmail\"]")
        print (colored("found insuredEmail!!!", 'green'))
        interact.send_keys("test@test.com")

    except:
        print (colored("Can not find insuredEmail", 'red'))

    try:
        print (colored("looking for insuredIDType", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
        interact = driver.find_element_by_xpath("//*[@id=\"insuredIDType\"]")
        print (colored("found insuredIDType!!!", 'green'))
        driver.execute_script("arguments[0].scrollIntoView(true);", interact)
        action = ActionChains(driver)
        action.move_to_element(interact).perform()
    except:
        print (colored("Can not find insuredIDType", 'red'))

    try:
        print (colored("looking for insuredIDType", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
        interact.get_attribute("name")
        print (colored("found insuredIDType!!!", 'green'))

    except:
        print (colored("Can not find insuredIDType", 'red'))

    try:
        print (colored("looking for option", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
        print ('made it here')
        interact = driver.find_elements_by_xpath("//*[@id=\"insuredIDType\"]/option")

        for i in range(len(interact)):
            if interact[i].get_attribute("label") == "State ID Number":
                interact[i].click()
                print("clicked")

        print (colored("found option!!!", 'green'))

    except:
        print (colored("Can not find option", 'red'))

    try:
        print (colored("looking for insuredStateIDNumber", 'green'))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"insuredStateIDNumber\"]")))
        interact = driver.find_element_by_xpath("//*[@id='insuredStateIDNumber']")
        interact.click()
        print (colored("found insuredStateIDNumber!!!", 'green'))
        interact.send_keys("H12345678901234")


    except:
        print (colored("Can not find insuredStateIDNumber", 'red'))

    try:
        print (colored("looking for option", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDState\"]")))

        interact = driver.find_elements_by_xpath("//*[@id=\"insuredIDState\"]/option")

        interact
        print (len(interact))

        for i in range(len(interact)):

            # print (interact[i].tag_name)
            # print (type(interact[i]))
            # print (interact[i].get_attribute("label"))
            # print (interact[i].element)

            if interact[i].get_attribute("label") == "Alabama":
                interact[i].click()

        print (colored("found Alabama!!!", 'green'))
        # print (interact.value)
        # interact.send_keys("021891234")


    except:
        print (colored("Can not find Alabama", 'red'))

    try:
        print (colored("looking for insuredIDType", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"btnContinue\"]")))
        interact = driver.find_element_by_xpath("//*[@id=\"btnContinue\"]")

        print (colored("found btnContinue!!!", 'green'))
        interact.click()


    except:
        print (colored("Can not find btnContinue", 'red'))



    try:
        print (colored("looking for Well this is unexpected...", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Well this is unexpected...']")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//h2[text()='Well this is unexpected...']")
        # interact.click()
        # interact.clear()
        print (colored("found Well this is unexpected...!!!", 'green'))
        # interact.send_keys("11162001")
        driver.execute_script("sauce:job-result={}".format("passed"))


    except:
        print (colored("Can not find Well this is unexpected...", 'red'))
        driver.execute_script("sauce:job-result={}".format("failed"))


    # print (type(driver.current_url))
    # sauce_result = "failed" if str(driver.current_url) == 'https://saucelabs.com/' else "passed"
    # driver.execute_script("sauce:job-result={}".format(sauce_result))


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
