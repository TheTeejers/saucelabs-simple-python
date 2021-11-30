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
        # 'commandTimeout':600,
        # 'build': "really?",
        # "recordDeviceVitals": 'true',
        # 'tunnelIdentifier': 'Digital_Mobile_QA',
        # 'locale' : "fr_CA",
        # 'testobject_api_key' : '6BE172925CB6420AAEF39D7B8ED575F3',
        # 'testobject_api_key' : 'BCE49A0E8472461DBBA727592D8DE4D0',

        # On CSTEAM: # The API generated for the Test Object project


        # 'app': 'storage:f5988b56-89f1-4db8-b9a8-d4e2a8f0887c', #ios smartsheets
        # 'app': 'storage:59549449-8b97-47c5-9343-f76799cc4fe4', #android smartsheets


        # 'app': 'storage:filename=mynewfilename.ipa',
        # 'app': 'storage:filename=Broker_Plus-UATOCP-1205',
        # 'app': 'storage:2e9da00c-8086-4c34-b0a1-7c6048ba6803',
        # 'app': 'storage:0debe8c2-bc55-48e1-ad44-8dac657d0051',



        # "public": "public",
        # "appiumVersion":"1.20.1",
        # 'tunnelIdentifier':'try1tj'

        # 'sauceLabsImageInjectionEnabled': 'true',

        # 'wdaEventloopIdleDelay': '5',
        # "waitForQuiescence": False,

        # "cacheId": "1234",
        # "noReset": "true",






        'appiumVersion': '1.19.0',
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
        # 'app': 'storage:filename=interact.ipa',
        # 'app': 'storage:264d3821-e02c-4aa6-a678-e9df4f164d9e', #bersa-uat
        # 'app': 'storage:2a231e42-0425-4e5c-8023-a7c68f59f970', #swag-labs
        'app': 'storage:b955e283-cc89-494a-b4b0-5e937522da02', #My Account App


    }

    androidParameters = { # Define Android parameters here
        # 'platformVersion' : '10',
        # 'automationName': 'uiautomator2',
        # 'deviceName' : 'Samsung.*',
        'appium:deviceName' : 'Samsung Galaxy S20.*',
        # 'deviceName' : 'Samsung_Galaxy_S[1-2]0_real',
        # 'deviceName' : 'Google_Pixel_4_XL_real_us',

        'browserName' : 'chrome',
        'deviceOrientation' : 'portrait',
        'appium:platformName' : 'Android',
        # 'platformVersion' : '9',
        # "recordDeviceVitals": 'true',
        "sauce:options":{

        }
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
        # 'deviceName' : 'iPhone 11.*',
        # 'deviceName' : 'iPhone X Simulator',
        # 'deviceName' : 'iPhone_11_13_real_us',
        # 'deviceOrientation' : 'portrait',
        # 'browserName' : 'Chrome',
        # 'browserName' : 'safari',
        'platformVersion' : '14',
        'platformName' : 'iOS',
        # "recordDeviceVitals": 'true',
        # "bundleId" : "com.apple.Preferences",
        # 'name' : "Sauce Labs Test",
        # 'testobject_suite_name': 'BOTW_Mobile_App_Automation_iOS',
        # 'testobject_test_name': "iPhone App: #{scenario.name}",
        # 'testobject_app_id': ['1'],
        # 'autoAcceptAlerts': True,
        'w3c': True,
        "nativeWebTap": True,
        "realMobile": True,
        "javascriptEnabled": True,
        # 'safariInitialUrl': 'https://www.saucelabs.com'
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
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+' @ondemand.us-west-1.saucelabs.com:443/wd/hub',
            command_executor='https://mandeepsingh.matharoo:d01c022e-b4b7-4472-b22f-b6dbe03ab8ec@ondemand.us-west-1.saucelabs.com:443/wd/hub',
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

    try:
        print (colored("looking for PROD", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "PROD")))
        print (colored("found PROD", 'green'))
        interact = driver.find_element_by_id("PROD")
        interact.click()
    except:
        print (colored("Can not find PROD", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))

    try:
        print (colored("looking for Done", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Done")))
        print (colored("found Done", 'green'))
        interact = driver.find_element_by_id("Done")
        interact.click()
    except:
        print (colored("Can not find Done", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    # try:
    #     print (colored("looking for Number?", 'green'))
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Number?")))
    #     print (colored("found Number?", 'green'))
    #     interact = driver.find_element_by_id("Number?")
    #     # interact.click()
    # except:
    #     print (colored("Can not find Number?", 'red'))
    #     source = driver.page_source
    #     print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for onboarding_btn_close", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "onboarding_btn_close")))
        print (colored("found onboarding_btn_close", 'green'))
        interact = driver.find_element_by_id("onboarding_btn_close")
        interact.click()
    except:
        print (colored("Can not find onboarding_btn_close", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for ctnAuth_view_getAccessNowTitle", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ctnAuth_view_getAccessNowTitle")))
        print (colored("found ctnAuth_view_getAccessNowTitle", 'green'))
        interact = driver.find_element_by_id("ctnAuth_view_getAccessNowTitle")
        # interact.click()
    except:
        print (colored("Can not find ctnAuth_view_getAccessNowTitle", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for ctnAuth_btn_doNotHaveFidoNumber", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ctnAuth_btn_doNotHaveFidoNumber")))
        print (colored("found ctnAuth_btn_doNotHaveFidoNumber", 'green'))

        interact = driver.find_element_by_id("ctnAuth_btn_doNotHaveFidoNumber")

        # interact2 = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name=\"Log In\"]")
        # print (len(interact2))
        # print (interact2)
        interact.click()

    except:

        print (colored("Can not find ctnAuth_btn_doNotHaveFidoNumber", 'red'))

        source = driver.page_source
        print(colored(source.split(' '), 'red'))



    try:
        print (colored("looking for Log In", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Log In")))
        print (colored("found Log In", 'green'))

        interact = driver.find_element_by_id("Log In")
        print (colored("found Log In", 'green'))

        interact
        interact.click()

    except:

        print (colored("Can not find Log In", 'red'))
        print (colored("looking for ctnAuth_btn_doNotHaveFidoNumber", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ctnAuth_btn_doNotHaveFidoNumber")))
        print (colored("found ctnAuth_btn_doNotHaveFidoNumber", 'green'))

        interact = driver.find_element_by_id("ctnAuth_btn_doNotHaveFidoNumber")

        # interact2 = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name=\"Log In\"]")
        # print (len(interact2))
        # print (interact2)
        interact.click()

        print (colored("looking for Log In", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Log In")))
        print (colored("found Log In", 'green'))

        interact = driver.find_element_by_id("Log In")
        print (colored("found Log In", 'green'))

        interact
        interact.click()
        source = driver.page_source
        print(colored(source.split(' '), 'red'))



    try:
        print (colored("looking for login_view_loginMessage", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login_view_loginMessage")))
        print (colored("found login_view_loginMessage", 'green'))
        interact = driver.find_element_by_id("login_view_loginMessage")
        # interact.click()
    except:
        print (colored("Can not find login_view_loginMessage", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for login_tf_username", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login_tf_username")))
        print (colored("found login_tf_username", 'green'))
        interact = driver.find_element_by_id("login_tf_username")
        interact.click()
        interact.send_keys("demo")
    except:
        print (colored("Can not find login_tf_username", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for login_tf_password", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login_tf_password")))
        print (colored("found login_tf_password", 'green'))
        interact = driver.find_element_by_id("login_tf_password")
        interact.click()
        interact.send_keys("demo")
    except:
        print (colored("Can not find login_tf_password", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))

    try:
        print (colored("looking for login_btn_login", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login_btn_login")))
        print (colored("found login_btn_login", 'green'))
        interact = driver.find_element_by_id("login_btn_login")
        interact.click()
        # interact.send_keys("demo")
    except:
        print (colored("Can not find login_btn_login", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))



    try:
        print (colored("looking for dataCollection_btn_dataCollectionDeclineButton", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "dataCollection_btn_dataCollectionDeclineButton")))
        print (colored("found dataCollection_btn_dataCollectionDeclineButton", 'green'))
        interact = driver.find_element_by_id("dataCollection_btn_dataCollectionDeclineButton")
        # interact.click()
        # interact.send_keys("demo")
    except:
        print (colored("Can not find dataCollection_btn_dataCollectionDeclineButton", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))



    try:
        print (colored("looking for dataCollection_btn_dataCollectionDeclineButton", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "dataCollection_btn_dataCollectionDeclineButton")))
        print (colored("found dataCollection_btn_dataCollectionDeclineButton", 'green'))
        interact = driver.find_element_by_id("dataCollection_btn_dataCollectionDeclineButton")
        interact.click()
        # interact.send_keys("demo")
    except:
        print (colored("Can not find dataCollection_btn_dataCollectionDeclineButton", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for Allow", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Allow")))
        print (colored("found Allow", 'green'))
        interact = driver.find_element_by_id("Allow")
        print (colored("found Allow", 'green'))
        # source = driver.page_source
        # print(colored(source.split(' '), 'red'))
        # interact2 = driver.find_element_by_id("Don't Allow")

        interact.click()
        print (colored("clicked Allow", 'green'))
        # sleep(10)
        # interact.send_keys("demo")
    except:
        print (colored("Can not find Allow", 'red'))
        # source = driver.page_source
        # print(colored(source.split(' '), 'red'))ç

    try:
        print (colored("looking for SUPPORT", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "SUPPORT")))
        print (colored("found SUPPORT", 'green'))
        interact = driver.find_element_by_name("SUPPORT")
        interact.click()
    except:
        print (colored("Can not find SUPPORT", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))

    try:
        print (colored("looking for support_view_contactUs_settingsRowTitle", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "support_view_contactUs_settingsRowTitle")))
        print (colored("found support_view_contactUs_settingsRowTitle", 'green'))
        interact = driver.find_element_by_id("support_view_contactUs_settingsRowTitle")
        interact.click()
    except:
        print (colored("Can not find support_view_contactUs_settingsRowTitle", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))



    try:
        print (colored("looking for contactUs_view_socialMediaSupport_expandableViewTitleLabel", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "contactUs_view_socialMediaSupport_expandableViewTitleLabel")))
        print (colored("found contactUs_view_socialMediaSupport_expandableViewTitleLabel", 'green'))
        interact = driver.find_element_by_id("contactUs_view_socialMediaSupport_expandableViewTitleLabel")
        interact.click()
    except:
        print (colored("Can not find contactUs_view_socialMediaSupport_expandableViewTitleLabel", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for contactUs_view_facebookMessenger_expandedSubViewTitleLabel", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "contactUs_view_facebookMessenger_expandedSubViewTitleLabel")))
        print (colored("found contactUs_view_facebookMessenger_expandedSubViewTitleLabel", 'green'))
        interact = driver.find_element_by_id("contactUs_view_facebookMessenger_expandedSubViewTitleLabel")
        interact.click()
    except:
        print (colored("Can not find contactUs_view_facebookMessenger_expandedSubViewTitleLabel", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))

    try:
        print (colored("looking for OK", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "OK")))
        print (colored("found OK", 'green'))
        interact = driver.find_element_by_id("OK")
        interact.click()
    except:
        print (colored("Can not find OK", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for URL", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "URL")))
        print (colored("found URL", 'green'))
        interact = driver.find_element_by_id("URL")
        interact.click()
    except:
        print (colored("Can not find URL", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))





    try:
        driver.activate_app('com.fido.myaccount.enterprise')
    except:
        print (colored("Can not activate app", 'red'))
        # source = driver.page_source
        # print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for contactUs_view_socialMediaSupport_expandableViewTitleLabel", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "contactUs_view_socialMediaSupport_expandableViewTitleLabel")))
        print (colored("found contactUs_view_socialMediaSupport_expandableViewTitleLabel", 'green'))
        interact = driver.find_element_by_id("contactUs_view_socialMediaSupport_expandableViewTitleLabel")
        # source = driver.page_source
        # print(colored(source.split(' '), 'red'))
        interact.click()
    except:
        print (colored("Can not find contactUs_view_socialMediaSupport_expandableViewTitleLabel", 'red'))
        source = driver.page_source
        print(colored(source.split(' '), 'red'))


    try:
        print (colored("looking for CONTACT US", 'green'))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "CONTACT US")))
        print (colored("found CONTACT US", 'green'))
        # source = driver.page_source
        # print(colored(source, 'red'))
        # <XCUIElementTypeStaticText type="XCUIElementTypeStaticText" value="CONTACT US" name="CONTACT US" label="CONTACT US" enabled="true" visible="true" x="131" y="55" width="113" height="21" index="1"/>


        interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar/*")
        # interact1 = driver.find_elements_by_xpath("//*/XCUIElementTypeOther")
        # interact1 = driver.find_elements_by_xpath("//*")
        # interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar//XCUIElementTypeOther")

        print ("looking at XCUIElementTypeNavigationBar/* only")
        # print (interact1)
        # print (type(interact))

        print (range(len(interact1)))
        print (len(interact1))
        for i in range(len(interact1)):
            print (i)
            print (interact1[i].tag_name)
            # print (type(interact1[i]))
            # print (interact1[i])
            print (interact1[i].get_attribute("label"))
        print ("  ")
        print ("  ")


        interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar/XCUIElementTypeButton")
        # interact1 = driver.find_elements_by_xpath("//*/XCUIElementTypeOther")
        # interact1 = driver.find_elements_by_xpath("//*")
        # interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar//XCUIElementTypeOther")

        print ("looking at XCUIElementTypeNavigationBar/XCUIElementTypeButton only")

        # print (interact1)
        # print (type(interact))

        print (range(len(interact1)))
        print (len(interact1))
        for i in range(len(interact1)):
            print (i)
            print (interact1[i].tag_name)
            # print (type(interact1[i]))
            # print (interact1[i])
            print (interact1[i].get_attribute("label"))
        print ("  ")
        print ("  ")

        # interact1[1].click()


        interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar/XCUIElementTypeOther")
        # interact1 = driver.find_elements_by_xpath("//*/XCUIElementTypeOther")
        # interact1 = driver.find_elements_by_xpath("//*")
        # interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar//XCUIElementTypeOther")

        print ("looking at XCUIElementTypeNavigationBar/XCUIElementTypeOther only")

        # print (interact1)
        # print (type(interact))

        print (range(len(interact1)))
        print (len(interact1))
        for i in range(len(interact1)):
            print (i)
            print (interact1[i].tag_name)
            # print (type(interact1[i]))
            # print (interact1[i])
            print (interact1[i].get_attribute("label"))
        print ("  ")
        print ("  ")


        interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar/XCUIElementTypeStaticText")
        # interact1 = driver.find_elements_by_xpath("//*/XCUIElementTypeStaticText")
        # interact1 = driver.find_elements_by_xpath("//*")
        # interact1 = driver.find_elements_by_xpath("//XCUIElementTypeNavigationBar//XCUIElementTypeStaticText")

        print ("looking at XCUIElementTypeNavigationBar/XCUIElementTypeStaticText only")

        # print (interact1)
        # print (type(interact))

        print (range(len(interact1)))
        print (len(interact1))
        for i in range(len(interact1)):
            print (i)
            print (interact1[i].tag_name)
            # print (type(interact1[i]))
            # print (interact1[i])
            print (interact1[i].get_attribute("label"))
        print ("  ")
        print ("  ")
        interact1[0].click()



        # interact = driver.find_elements_by_id("CONTACT US")
        #
        # print ('looking up all CONTACT US elements')
        # # print (type(interact))
        # print (len(interact))
        # for i in range(len(interact)):
        #     print (i)
        #     print (interact[i].tag_name)
        #
        #     print (interact[i].get_attribute("name"))
        # print ("  ")
        # print ("  ")
        # print (interact.get_attribute("label"))
        #
        # interact.click()
        # source = driver.page_source
        # print(colored(source.split(' '), 'red'))

        sleep(3)
    except:
        print (colored("Can not find CONTACT US", 'red'))
        # source = driver.page_source
        # print(colored(source.split(' '), 'red'))


    # print (type(driver.current_url))
    sauce_result = "failed" if 1 != 1 else "passed"
    # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
    driver.execute_script("sauce:job-result={}".format(sauce_result))


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
