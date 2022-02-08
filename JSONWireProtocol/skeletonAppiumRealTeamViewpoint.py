###################################################################
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
        'recordDeviceVitals': True,
        # 'name': 'AEM home page options validation -256390 home page displayed',
        # "timeZone": "Honolulu",
        # 'commandTimeout':600,
        # 'build': "really?",
        # "recordDeviceVitals": 'true',
        # 'tunnelIdentifier': 'tjnew1',
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
        # 'tunnelIdentifier':'one',
        # 'parentTunnel':'TJLoughry'

        # 'sauceLabsImageInjectionEnabled': 'true',
        # "eventLoopIdleDelaySec": 4,
        # 'wdaEventloopIdleDelay': '5',
        # "waitForQuiescence": False,
        # "waitForQuietness": False,


        # "cacheId": "1234",
        # "noReset": "true",






        # 'appiumVersion': '1.18.1',
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
        # 'testobject_api_key' : '9DB6106BD03943729266E0E77EBF26E2', # test on FlashFlood iOS app

        # 'maxInstances': 5,
    }

    unifiedPlatformAppStorage = {
        # 'app': 'storage:filename=interact.ipa',
        # 'app': 'storage:264d3821-e02c-4aa6-a678-e9df4f164d9e', #bersa-uat
        # 'app': 'storage:521f9d7b-2106-49b8-80c5-4b9b8c617a5d', #childplace app android
        # 'app': 'storage:bc8ce2eb-4c15-4463-9521-4af2639ba664', #swag-labs iOS US SIM
        # 'app': 'storage:640aa9b0-a50a-46a6-bae7-0e47fa70f211', #swag-labs android EU
        # 'app': 'storage:1f77b56e-e9aa-4c4d-951c-31c1b97a18b9', #SelfHelp ios Real
        # 'app': 'storage:co.uk.simplyhealth.simplyplan.staging',
        # 'app': 'storage:ad8710ff-d8b4-4448-a017-0686f4d8c1bb', #swag-labs Android US
        'app': 'storage:e9e8a918-a1e4-4064-b244-47cffcf9789f', #Team Viewpoint application iOS
    }

    androidParameters = { # Define Android parameters here
        # 'platformVersion' : '10',
        # 'automationName': 'uiautomator2',
        'deviceName' : 'Google.*',
        # 'deviceName' : 'Samsung.*Galaxy.*',
        # 'appium:deviceName' : 'Samsung Galaxy S20.*',
        # 'deviceName' : '.*Pixel.*',
        # 'deviceName' : '	Google_Pixel_5a_real_us',

        'browserName' : 'chrome',
        # 'deviceOrientation' : 'PORTRAIT',
        # 'appium:platformName' : 'Android',
        'platformName' : 'Android',
        'platformVersion' : '11',
        'recordVideo':False,
        # "orientation": "portrait",
        "orientation": "PORTRAIT",
        # "recordDeviceVitals": 'true',
        # "sauce:options":{

        # }
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
        # 'chromeDriverVersion': '91.0.4472.19'
        # 'chromeDriverVersion': '83.0.4103.39'

    }

    iosParameters = { # Define iOS Parameters here
        'phoneOnly': 'true',
        # 'tabletOnly': 'true',
        # 'includeSafariInWebviews': True,
        # 'deviceName' : 'iPhone 11',
        'deviceName' : 'iPhone_12_Pro_real_us',
        # 'deviceName' : 'iPhone_11_15_real_us',
        # 'deviceOrientation' : 'portrait',
        # 'browserName' : 'Chrome',
        # 'browserName' : 'safari',
        # 'platformVersion' : '15',
        'platformName' : 'iOS',
        # "recordDeviceVitals": 'true',
        # "bundleId" : "com.apple.Preferences",
        # 'name' : "Sauce Labs Test",
        # 'testobject_suite_name': 'BOTW_Mobile_App_Automation_iOS',
        # 'testobject_test_name': "iPhone App: #{scenario.name}",
        # 'testobject_app_id': ['1'],
        'autoAcceptAlerts': 'true',
        # 'w3c': True,
        # "nativeWebTap": True,
        # "realMobile": True,
        # "javascriptEnabled": True,
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
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://enriquegh:66af84ca-670f-4647-84c2-54b703833015@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://TJLoughry:69e79050-5358-440b-b38e-453e30f71d6f@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
            # command_executor='https://<user>.<access_key>.us-west-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    elif EU_Datacenter==True:
        sauceParameters.update(unifiedPlatformAppStorage)
        print (colored('You are testing on the Sauce Labs EU Datacenter', 'green', attrs=['blink', 'underline']))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+' @ondemand.eu-central-1.saucelabs.com:443/wd/hub/session',
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


    # driver.execute_script("mobile: shell", {"args":["--allow-insecure=adb_shell"]});
    # driver.execute_script('mobile: shell', {"command": "su root service call alarm 3 s16 Europe/Volgograd"})
    # print (driver.execute_script('mobile: shell', {"command": "wm size"}))
# adb shell wm size
    # driver.get('https://www.google.com/search?q=current+time&oq=current+time&aqs=chrome..69i57j0i402l2j0i131i433i512j69i64l3j69i61.2821j0j4&sourceid=chrome&ie=UTF-8')

    # sleep(10)
    size = driver.get_window_size()
    size
    print(size)
    print (driver.capabilities)
    # print (driver.capabilities['testobject_test_report_url'])





    # print (colored(str(datetime.datetime.now()), 'green', attrs=['blink', 'underline']))
    # source = driver.page_source
    # print(colored(source, 'red'))
    # try:
    #     print (colored("looking for Allow Once", 'green'))
    #     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'bersa-uat')))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Allow Once')))
    #     # print (colored("found login_overview_btn_sign_in", 'green'))
    #
    #
    #
    #     interact = driver.find_element_by_name("Allow Once")
    #     interact.click()
    #     sleep(5)
    #     # print (colored("clicked type == 'login_overview_btn_sign_in", 'green'))
    #     # interact.click()
    #
    #     print (colored("clicked Allow Once", 'green'))
    #     sleep(10)
    #     source = driver.page_source
    #     print(colored(source, 'red'))
    # except:
    #     print (colored("Can not find Allow Once", 'red'))

    # sleep(10)
    # media = driver.media_devices.get_user_media({audio: true, video: true})
    # print (media)

    # (async () => {
    #     await navigator.mediaDevices.getUserMedia({audio: true, video: true});
    #     let devices = await navigator.mediaDevices.enumerateDevices();
    #     console.log(devices);
    # })();

    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.mobileslideshow'})
# /private/var/mobile/Media/DCIM/
    # driver.push_file("@com.apple.DocumentsApp:sampletext.txt", "/Users/terranceloughry/Desktop/sampletext.txt")
    # driver.push_file("@com.apple.DocumentsApp:is_it.gif", "/Users/terranceloughry/Desktop/Thor_Reaction_Gifs/is_it.gif")
    # driver.push_file("/Users/terranceloughry/Desktop/test.jpeg", "@com.apple.mobileslideshow:test.jpeg")
    # driver.push_file("@com.apple.mobileslideshow:test.jpeg", "/Users/terranceloughry/Desktop/test.jpeg")
    # driver.push_file("/Users/terranceloughry/Desktop/paterntest.jpeg", "@com.apple.mobileslideshow:paterntest.jpeg")

    # driver.push_file("@com.apple.Keynote/Patern_test.jpeg", "")

    # print('file pushed')

    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.DocumentsApp'})
    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.mobileslideshow'})
    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.Safari'})


    # driver.get("https://www.portal.ehealth.gov.hk/app/index.html")
    # sleep(5)
    # webview = driver.contexts[0]
    # print(webview)
    # driver.switch_to.context(webview)
    # source = driver.page_source
    # print(colored(source, 'red'))
    #
    # sleep(5)
    # driver.refresh()
    # webview = driver.contexts[1]
    # print(webview)
    # driver.switch_to.context(webview)
    # version = driver.execute_script("return navigator.userAgent.match('Chrome/[^ ]+')[0]")
    # print(version)
    # source = driver.page_source
    # print(colored(source, 'blue'))


    #
    # print ('Test Name == ', colored(driver.capabilities['testobject_test_name'], 'green', attrs=['reverse', 'blink']))
    # print ('Device Name == ', colored(driver.capabilities['testobject_device_name'], 'green', attrs=['reverse', 'blink']))
    # print ('Device descriptor == ', colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))
    # print ('Platform Version == ', colored(driver.capabilities['platformVersion'], 'green', attrs=['reverse', 'blink']))
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
    # driver.close_app()
    # sleep(10)

    # source = driver.page_source
    # print(colored(source.split(' '), 'red'))
    # driver.execute_script('sauce:context=Open google.com')
    # pref = 'com.apple.Preferences'
    # driver.launch_app(pref)
    # sleep(1)
    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.Maps'})
    # sleep(10)
    # driver.close_app()
    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.mobilesafari'})
    #
    # sleep(5)
    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.saucelabs.SafariLauncher'})
    # sleep(5)
    # # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.mobilesafari'})
    # # sleep(5)
    # # driver.get("https://www.google.com")
    # # print(driver.get_cookies())
    # # sleep(10)
    # print (driver.contexts)
    # driver.contexts
    #
    # webview = driver.contexts[0]
    # print (webview)
    # print (len(webview))
    # print (driver.contexts)
    # webview = driver.contexts
    # driver.current_context
    #
    # print (driver.current_context)
    # print (webview)
    # print (webview[1])
    # print (len(webview))
    # print (len(driver.contexts))
    # driver.switch_to.context(webview[1])
    # # driver.get("https://www.google.com")
    # print (driver.contexts)
    # print (driver.current_context)
    # driver.get("https://www.google.com")
    #
    # interact = driver.device_time
    # print (interact)


    # print(driver.get_cookie('name'))
    # driver.get_cookie('name')
    # cookies_list = driver.get_cookies()
    # cookies_dict = {}
    # for cookie in cookies_list:
    #     cookies_dict[cookie['name']] = cookie['value']
    #
    # print(cookies_dict)
    # driver.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    # driver.execute_script('sauce:context=Open new tab')
    #
    # driver.execute_script("window.open('');")
    # driver.execute_script('sauce:context=Switch to new tab')
    #
    # driver.switch_to.window(driver.window_handles[1])

    # driver.execute_script('sauce:context=Open saucelabs.com')
    # driver.get("https://saucelabs.com")

    # driver.execute_script('sauce:context=Get URL')
    # try:
    #     print (colored("looking for class check mark", 'green'))
    #     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'bersa-uat')))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-ion-label-ios-h sc-ion-label-ios-s ios hydrated')))
    #     interact = driver.find_element_by_class("sc-ion-label-ios-h sc-ion-label-ios-s ios hydrated")
    #     # interact = driver.find_element_by_name("bersa-uat")
    #     interact.click()
    #     print (colored("found class check mark!!!", 'green'))
    #     sleep(10)
    # except:
    #     print (colored("Can not find class check mark", 'red'))
    #
    #
    # try:
    #     print (colored("looking for xpath agree", 'green'))
    #     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'bersa-uat')))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="Agree"]')))
    #     interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Agree']")
    #     # interact = driver.find_element_by_name("bersa-uat")
    #     interact.click()
    #     print (colored("found agree!!!", 'green'))
    #     sleep(10)
    # except:
    #     print (colored("Can not find xpath agree", 'red'))
    #
    # try:
    #     print (colored("looking for Soy", 'green'))
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'Soy')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("Soy")
    #     # interact.click()
    #     print (colored("found Soy!!!", 'green'))
    # except:
    #     print (colored("Can not find Soy", 'red'))
        # names = driver.find_elements_by_xpath(".//*")
        # print(colored(names.get_attribute(), 'green'))
        # source = driver.page_source
        # interact = driver.find_element_by_class_name("noThanks_btn")
        # # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
        # interact.click()
        # print (colored("found No Thanks Button", 'green'))
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/')
    # try:
    #     WebDriverWait(driver, 15).until(EC.alert_is_present())
    #
    #     alert = browser.switch_to.alert
    #     alert.dismiss()
    #     print("alert accepted")
    # except:
    #     print("no alert")
    #
    # try:
    #     WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'q')))
    #     print('found1')
    #     interact = driver.find_element_by_name("q")
    #     interact.click()
    #     print('clicked')
    #     interact.send_keys('click google search button')
    #     print('sent keys')
    #
    #     interact = driver.find_element_by_name("btnK")
    #     print('found search button')
    #     interact.click()
    #
    #     print('clicked')
    #
    #     sleep(5)
    # except:
    #     print("did not work")
    #
    # try:
    #     WebDriverWait(driver, 15).until(EC.alert_is_present())
    #
    #     alert = browser.switch_to.alert
    #     alert.dismiss()
    #     print("alert accepted")
    # except:
    #     print("no alert")
    #
    # driver.get('https://google.com/')
    # try:
    #     WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'q')))
    #     print('found2')
    #
    #     interact = driver.find_element_by_name("q")
    #     interact.click()
    #     print('clicked')
    #     interact.send_keys('submitting after send keys')
    #     print('sent keys')
    #
    #     interact.submit()
    #     sleep(5)
    # except:
    #     print("did not work")

    # driver.get('https://google.com/')
    # try:
    #     WebDriverWait(driver, 30).until(EC.EC.presence_of_element_located((By.CLASS_NAME, 'q')))
    #     interact = driver.find_element_by_name("q")
    #     interact.click()
    #     interact.send_keys('submitting after send keys')
    #     interact.submit()
    #
    # except:
    #     print("did not work")

    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)
    #
    # driver.get('https://google.com/maps')
    # print (str(datetime.datetime.now()))
    # sleep(55)


    # driver.set_location(49, 123, 10)
    # driver.toggle_location_services()


    # # sleep(10)
    # # driver.launch_app(com.apple.Preferences)
    # driver.activate_app("com.apple.mobilesafari");
    # # #
    # sleep(10)
    # source = driver.page_source
    # print(colored(source, 'red'))
    # print (colored(driver.contexts, 'blue'))
    # driver.activate_app("com.apple.mobilesafari");
    # print (colored(driver.contexts, 'blue'))
    # try:
    #     WebDriverWait(driver, 15).until(EC.alert_is_present())
    #
    #     alert = browser.switch_to.alert
    #     alert.dismiss()
    #     print("alert accepted")
    #     driver.get('https://whatismyipaddress.com/')
    # except:
    #     print("no alert")
    #     print (colored(driver.contexts, 'blue'))


    # try:
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//XCUIElementTypeButton[@name='URL']")))
    #     # driver.switch_to.context('WEBVIEW_442.1')
    #     # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Google']").click()
    #     # interact.send_keys("google.com")
    #     # sleep(5)
    #     # alert = browser.switch_to.alert
    #     # alert.dismiss()
    #     # print("alert accepted")
    #     print (colored(driver.contexts, 'blue'))
    #     webview = driver.contexts[1]
    #     driver.switch_to.context(webview)
    #     driver.get('https://whatismyipaddress.com/')
    #             # alert = browser.switch_to.alert
    #             # alert.dismiss()
    #             # print("alert accepted")
    # except:
    #     print("no alert")
    #     print (colored(driver.contexts, 'blue'))
        # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
        # <XCUIElementTypeButton type="XCUIElementTypeButton" value="Search or enter website name" name="URL" label="Address" enabled="true" visible="true" accessible="false" x="234" y="24" width="644" height="36" index="1">
        #             <XCUIElementTypeOther type="XCUIElementTypeOther" value="Search or enter website name" name="Address" label="Address" enabled="true" visible="true" accessible="true" x="452" y="32" width="228" height="21" index="0"/>




        # driver.get('https://whatismyipaddress.com/')
        # alert = browser.switch_to.alert
        # alert.dismiss()
        # print("alert accepted")

    # driver.get('https://google.com/maps')
    # driver.get('https://gps-coordinates.org/my-location.php')
    # sleep(5)
    # print (str(datetime.datetime.now()))
    # str(datetime.datetime.now())
    # driver.toggle_location_services()
    # sleep(55)
    # driver.get('https://gps-coordinates.org/my-location.php')
    # driver.get('https://google.com/maps')


    # sleep(10)
    #
    # # "com.android.packageinstaller:id/dialog_container"
    # # driver.switch_to_alert
    # # source = driver.page_source
    # # print(source)
    # try:
    #     WebDriverWait(driver, 30).until(EC.alert_is_present())
    #
    #     alert = browser.switch_to.alert
    #     alert.accept()
    #     print("alert accepted")
    # except:
    #     print("no alert")
    #
    # print (colored(driver.contexts, 'blue'))
    # # interact.click()
    # print ("allow button tapped")
    # sleep(10)
    # interact = driver.find_element_by_id("latitude")
    # interact.get_attribute("value")
    # print(interact.get_attribute("value"))

    # driver.switch_to_alert().accept()
    # alert = driver.switch_to_alert().accept()
    # interact = driver.find_element_by_link_text('Allow').click()
    # print ("allow button tapped")
    # driver.get('https://google.com')



    # interact = driver.find_element_by_name("q")
    # interact.click()
    # interact.send_keys('google')
    # interact.submit()
    # sleep(10)
    # interact = driver.find_element_by_link_text('Maps')
    # interact.click()
    #
    # # sleep(10)
    # # interact = driver.find_element_by_css_selector("input[type='email']")
    #
    # try:
    #     print (colored("looking for I already have an account", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "I already have an account")))
    #     interact = driver.find_element_by_accessibility_id("I already have an account")
    #     interact.click()
    #     print (colored("found email input", 'green'))
    #     print (colored(driver.contexts, 'blue'))
    # except:
    #     print (colored("Can not find I already have an account", 'red'))
    #     # print (colored(interact.get_attribute('value'), 'blue'))
    # #
    #
    # driver.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
    # print (colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))


    # driver.execute_script("sauce:intercept", {
    #    "url": "http://sampleapp.appspot.com/api/todos",
    #       "response": {
    #           "headers": {
    #               "Authorization": "Basic YWRtaW46aFY2YzJxPmU="
    #           },
    #           "body": [{
    #              "url": "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert"
    #           }]
    #       }
    #  })
    # print('snap 1')
    # driver.get_screenshot_as_base64()
    # sleep(65)
    # print('snap 2')
    # driver.get_screenshot_as_base64()
    # print (colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))

                            # driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
                            # # driver.get('http://the-internet.herokuapp.com/windows')
                            #
                            #
                            #
                            #
                            # #
                            # #
                            # # #
                            # try:
                            #     print (colored("looking for tryhome", 'green'))
                            #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'tryhome')))
                            #     print (colored("found tryhome", 'green'))
                            #
                            #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Try it']")))
                            #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
                            #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='menu_share_form']")
                            #     # interact = driver.find_element_by_link_text("Click Here")
                            #     # interact = driver.find_element_by_class_name("VDXfz")
                            #     interact = driver.find_element_by_xpath("//iframe[@id='iframeResult']")
                            #     print(interact)
                            #     iframe = driver.find_elements_by_tag_name('iframe')
                            #     print(colored(iframe, 'blue'))
                            #
                            #     # driver.switch_to().frame("5001");
                            #     sleep(5)
                            #     interact = driver.find_elements_by_xpath("//*[contains(text(), 'Try it']")
                            #     print(interact)
                            #     # print(interact.get_attribute)
                            #     # source = driver.page_source
                            #
                            #     # interact.click()
                            #     # print (colored("found and Try It", 'green'))
                            #     # names = driver.find_elements_by_xpath(".//*")
                            #     # print(colored(names.get_attribute(), 'green'))
                            # except:
                            #     print (colored("Can not find Click Here", 'red'))
                            #     # interact = driver.find_element_by_xpath("//button[text()='Try it']")
                            #     # interact.click()
                            #
                            #
                            # print (driver.title),
        # names = driver.find_elements_by_xpath(".//*")
        # print(colored(names, 'green'))
        # source = driver.page_source
        # print(source, 'red')
        # interact = driver.find_element_by_class_name("menu_share_form")
        # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
        # interact.click()
        # print (colored("found No Thanks Button", 'green'))

    # sleep(5)
    # obj = driver.switch_to.alert
    #
    # #Retrieve the message on the Alert window
    # msg=obj.text
    # print ("Alert shows following message: "+ msg )
    # sleep(10)
    #
    #
    #
    # # dest_path = '/User/Desktop/signature.png'
    # # data = bytes('/storage/emulated/0/Download/jpg.jpg', 'utf-8')
    # # driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))
    #
    # driver.push_file("storage/emulated/0/Download/mypng.png'","@/User/Desktop/signature.png")
        # print(colored(source.split(' '), 'red'))
        # print (colored(interact.get_attribute('value'), 'blue'))
    #
    #
    # try:
    #     print (colored("looking for LoginEntryUsernameTextbox", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "LoginEntryUsernameTextbox")))
    #     interact = driver.find_element_by_accessibility_id("LoginEntryUsernameTextbox")
    #     interact.click()
    #     interact.send_keys("testqauser137")
    #     print (colored("found email input", 'green'))
    # except:
    #     print (colored("Can not find LoginEntryUsernameTextbox", 'red'))
    #     print (colored(interact.get_attribute('value'), 'blue'))
    #
    #
    # interact = driver.find_element_by_accessibility_id("LoginEntryPasswordTextbox")
    # interact.click()
    # interact.send_keys("Nn1234567!")
    #
    # interact = driver.find_element_by_accessibility_id("LoginEntryLoginButton")
    # interact.click()
    #
    #
    # try:
    #     print (colored("looking for ALLOW NOTIFICATIONS", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'ALLOW NOTIFICATIONS')))
    #     interact = driver.find_element_by_accessibility_id("ALLOW NOTIFICATIONS")
    #     # interact.click()
    #     print (colored("ALLOW NOTIFICATIONS", 'green'))
    #     interact.click()
    #
    # except:
    #     print (colored("Can not find ALLOW NOTIFICATIONS", 'red'))
    #
    #     interact = driver.find_element_by_class_name("menu_share_form")
    #     print (colored(interact.get_attribute('name'), 'blue'))
    #     # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
    #     interact.click()
    #     print (colored('Clicked "no thnaks"', 'blue'))
    #     # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "TabbarPaymentsButton")))
    #     interact = driver.find_element_by_accessibility_id("TabbarPaymentsButton")
    #     interact.click()
    #     print (colored("found TabbarPaymentsButton", 'green'))
    #
    # try:
    #     print (colored("looking for LoginEntryUsernameTextbox", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "TabbarPaymentsButton")))
    #     interact = driver.find_element_by_accessibility_id("TabbarPaymentsButton")
    #     interact.click()
    #     print (colored("found TabbarPaymentsButton", 'green'))
    # except:
    #     print (colored("Can not find TabbarPaymentsButton", 'red'))
    #     source = driver.page_source
    #     print(colored(source.split(' '), 'red'))
    #     # interact = driver.find_element_by_class_name("noThanks_btn")
    #     # print (colored(interact.get_attribute('name'), 'blue'))
    #     # # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
    #     # interact.click()
    #     # print (colored('Clicked "no thnaks"', 'blue'))
    #     # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "TabbarPaymentsButton")))
    # try:
    #     print (colored("looking for noThanks_btn", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Transfer')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("Transfer")
    #     interact.click()
    #     print (colored("found Transfer", 'green'))
    # except:
    #     print (colored("Can not find Transfer", 'red'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     source = driver.page_source
    #
    #
    # # interact.click()
    # # sleep(10)
    # # source = driver.page_source
    # # print(colored(source.split(' '), 'red'))
    #
    #
    # try:
    #     print (colored("looking for Internal Transfer", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Make an Internal Transfer')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("Make an Internal Transfer")
    #     interact.click()
    #     print (colored("found Make an Internal Transfer", 'green'))
    # except:
    #     print (colored("Can not find Make an Internal Transfer", 'red'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     source = driver.page_source
    #
    # try:
    #     print (colored("looking for Amount", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'Amount')))
    #     print (colored("found Amount", 'green'))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("Amount")
    #     interact.click()
    #     sleep(5)
    #     interact = driver.find_element_by_name("1")
    #     interact.click()
    #     interact = driver.find_element_by_name("0")
    #     interact.click()
    #     interact = driver.find_element_by_name("0")
    #     interact.click()
    #     interact = driver.find_element_by_name("Done")
    #     interact.click()
    #     print (colored("Entered 100", 'green'))
    # except:
    #     print (colored("Can not find Amount", 'red'))
    #     names = driver.find_elements_by_xpath(".//*")
    #     print (colored(driver.contexts, 'blue'))
    #     # print(colored(names.get_attribute(), 'green'))
    #     source = driver.page_source
    # # interact = driver.find_element_by_css_selector("//*XCUIElementTypeButton[@name='password']")
    # # interact.click()
    # # interact.send_keys('test1234')
    # # interact = driver.find_element_by_css_selector("[id='button__login']")
    # # interact.click()
    # try:
    #     print (colored("looking for CONTINUE", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'CONTINUE')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("CONTINUE")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked CONTINUE", 'green'))
    #     interact = driver.find_element_by_name("Submit")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked Submit", 'green'))
    #     print (colored(driver.contexts, 'blue'))
    # except:
    #     print (colored("Can not find CONTINUE", 'red'))
    #     print (colored(driver.contexts, 'blue'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     source = driver.page_source
    #
    # try:
    #     print (colored("looking for Submit", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Submit')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("Submit")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked Submit", 'green'))
    #     print (colored(driver.contexts, 'blue'))
    # except:
    #     print (colored("Can not find Submit", 'red'))
    #     print (colored(driver.contexts, 'blue'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     source = driver.page_source
    #
    #
    # try:
    #     print (colored("looking for Not Now", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'Not Now')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_id("Not Now")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked Not Now", 'green'))
    #     print (colored(driver.contexts, 'blue'))
    # except:
    #     print (colored("Can not find Not Now", 'red'))
    #     print (colored(driver.contexts, 'blue'))
    #     interact = driver.find_element_by_name("Submit")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked Submit", 'green'))
    #     print (colored("looking for Not Now", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'Not Now')))
    #     interact = driver.find_element_by_id("Not Now")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked Not Now", 'green'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     # source = driver.page_source
    #
    # try:
    #     print (colored("looking for Scheduled", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'Scheduled')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #
    #     print (colored("Found Scheduled", 'green'))
    #     print (colored(driver.contexts, 'blue'))
    #     webview = driver.contexts[1]
    #     # driver.switch_to.context(webview)
    #     source = driver.page_source
    #
    # except:
    #     print (colored("Can not find Scheduled", 'red'))
    #     print (colored(driver.contexts, 'blue'))
    #     source = driver.page_source
    #
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #
    #
    # try:
    #     print (colored("looking for transfer-done-button", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'transfer-done-button')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
    #     interact = driver.find_element_by_name("transfer-done-button")
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked transfer-done-button", 'green'))
    #     sleep(2)
    #     interact.click()
    #     print (colored("clicked transfer-done-button", 'green'))
    #     print (colored(driver.contexts, 'blue'))
    #
    #
    # except:
    #     print (colored("Can not find transfer-done-button", 'red'))
    #     print (colored(driver.contexts, 'blue'))
    #     webview = driver.contexts[1]
    #     driver.switch_to.context(webview)
    #     # print (colored("looking for transfer-done-button", 'green'))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'transfer-done-button')))
    #     # interact = driver.find_element_by_name("transfer-done-button")
    #     # sleep(2)
    #     # interact.click()
    #     # print (colored("clicked transfer-done-button", 'green'))
    #     # sleep(2)
    #     # interact.click()
    #     # print (colored("clicked transfer-done-button", 'green'))
    #     # print (colored(driver.contexts, 'blue'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     # source = driver.page_source
    #
    #
    # sleep(10)
    # source = driver.page_source
    # print(colored(source.split(' '), 'red'))
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
    # driver.get_screenshot_as_base64()

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
    # # #__________________________________________________________________
    # emailValueUincode = "fun times"
    # email = "not so miuch fun times"
    #
    # if emailValueUincode.encode("utf-8") == email:
    #     print ("passed")
    #     requests.put(
    #         # 'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
    #         'https://saucelabs.com/rest/v1/' + os.environ['SAUCE_USERNAME'] +'/jobs/' + driver.session_id,
    #         headers = { 'Content-Type': 'application/json',},
    #         data = '{"passed": true}', # Update this to pass either True or False depending on your requirements
    #     ),
    #
    # else:
    #     print ("failed")
    #     requests.put(
    #         # 'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
    #         'https://saucelabs.com/rest/v1/' + os.environ['SAUCE_USERNAME'] +'/jobs/' + driver.session_id,
    #         headers = { 'Content-Type': 'application/json',},
    #         data = '{"passed": true}', # Update this to pass either True or False depending on your requirements
    #         # data = '{"passed": false}' # Update this to pass either True or False depending on your requirements
    #     ),
        # requests.put(
        #     'https://saucelabs.com/rest/v1/TheTeejers/jobs/' + driver.session_id,
        #     headers = { 'Content-Type': 'application/json',},
        #     data = '{"passed": true}', # Update this to pass either True or False depending on your requirements
        # ),
    # sauce_result = "failed" if  driver.title != "Tryit Editor v3.7" else "passed"
    # driver.execute_script("sauce:job-result={}".format(sauce_result))
    # print('https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/')
    # print("testobject_device_session_id=  " + driver.capabilities['testobject_device_session_id'])
    # print("session_id=  " + driver.session_id)

    # Ending the test session
    #__________________________________________________________________
    # sauce_result = "failed" if 1 != 2 else "passed"
    # # sauce_result = "failed" if 1 != 1 else "passed"
    # driver.execute_script("sauce:job-result={}".format(sauce_result))


    # driver.execute_script('sauce:context=Change name of test')
    # driver.execute_script('sauce:job-name=Name Changed via JavascriptExecutor')
    # driver.execute_script('sauce:job-name=Name Changed via JavascriptExecutor ' + sauceParameters["name"])

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
