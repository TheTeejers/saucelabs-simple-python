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

androidTest = True
# iosTest = True


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
# appLocation = 'storage:4e4adc31-c706-42f8-a531-d8b353f55f16', #android Android_15.03.00_nr_20210311.1.apk
# appLocation = 'storage:74de627f-dc76-4e2a-a899-d6c7b1090372'
# appLocation = 'storage:f9232cab-fb1c-4340-b3f9-e3d8f2398abb'
# appLocation = 'storage:filename=Android_15.03.00_nr_20210311.1.apk'

appLocation = 'storage:filename=sauce-storage:Android_15.03.00_nr_20210311.1.apk'



###################################################################
# Common parameters (desired capabilities)
# For Test Object tests
###################################################################

run = 1

###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    projectParameters = {
        'tags':['W3C Appium'],
        # 'appiumVersion': '1.18.1',
        # 'name': 'Testing URL at Run Time: ' + str(datetime.datetime.now()),
        # 'commandTimeout': 200,
        # "idleTimeout": 200,
        # 'name': 'Testing App ' + appLocation +' at Run Time: ' + str(datetime.datetime.now()),
        # "timeZone": "Alaska",
        # 'sauce:throttleNetwork': 'offline',
        # 'tunnelIdentifier': 'tj1',
        # 'appWaitActivity': "*, .*",
    'sauce:options':{
        # 'platformName': 'WIN10',
        'name': 'Testing interact.ipa at Run Time: ' + str(datetime.datetime.now()),
        # 'appiumVersion': '1.19.0',

        },
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
        # 'app': 'storage:f5988b56-89f1-4db8-b9a8-d4e2a8f0887c', #ios smartsheets
        # 'app': 'storage:273d4796-7238-42c4-ac3a-06e15c10b229', #ios indeed
        # 'app': 'storage:4e4adc31-c706-42f8-a531-d8b353f55f16', #android Android_15.03.00_nr_20210311.1.apk


        # 'app': 'storage:59549449-8b97-47c5-9343-f76799cc4fe4', #android smartsheets
        # 'app':'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'

    }

    androidParameters = { # Define Android parameters here
        # 'appium:deviceName' : "Google Pixel GoogleAPI Emulator",
        # 'appium:deviceName' : 'Android',
        # 'appium:platformVersion' : '8.1',
        # 'platformName' : 'Android',
        # 'appium:appium:deviceName': 'Android',
        'deviceOrientation' : 'portrait',
        # 'relaxedSecurityEnabled': True,
        # 'autoGrantPermissions': True,
        # 'ignoreUnimportantViews': True,
        # 'automationName': 'UiAutomator2',
        # 'gpsEnabled': True,
        # 'maxDuration': 10800,
        # 'recordScreenshots': False
        # 'appium:platformVersion': 'latest',

        # 'appium:deviceName': 'Amazon_Kindle_Fire_HD_10_real',
        'appium:deviceName': 'Samsung Galaxy Tab S3 GoogleAPI Emulator',
        'appium:platformVersion': '8.0',
        'platformName': 'Android',
        # 'gpsEnabled': False


    }

    iosParameters = { # Define iOS Parameters here

        # 'appium:deviceName' : 'iPhone X Simulator',
        # 'deviceName' : 'iPhone Simulator',
		"appium:automationName": "XCuiTest",
		"appium:newCommandTimeout": 60,
		"appium:deviceOrientation": "portrait",
		"appium:deviceName": "iPhone 8",
		"appium:nativeWebScreenshot": True,
		"appium:platformVersion": "12.2",
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
            sauceParameters['appium:app'] = appLocation
            sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' + sauceParameters['platformName'] + ' version: '+ sauceParameters['appium:platformVersion'] + ' device: ' + sauceParameters['appium:deviceName']})  # Use app if it's specified
        else:
            sauceParameters['browserName'] = 'Chrome' # Otherwise use Chrome
            #Note! Replace 'Chrome' with 'Browser' for older versions of Android to use the stock browser
            sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['appium:platformVersion'] + ' device: ' + sauceParameters['appium:deviceName']})

    elif iosTest:
        sauceParameters.update(iosParameters)

        if useApp:
            sauceParameters['app'] = appLocation
            sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['appium:platformVersion'] + ' device: ' + sauceParameters['appium:deviceName']})
        else:
            sauceParameters['browserName'] = 'safari'
            # sauceParameters['browserName'] = 'safari'
            # sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['appium:platformVersion'] + ' device: ' + sauceParameters['appium:deviceName']})
            # sauceParameters.update({'build': ' '.join(sauceParameters.get('tags')) + ' platform: ' +sauceParameters['platformName'] + ' version: '+ sauceParameters['appium:platformVersion'] + ' device: ' + sauceParameters['deviceName']})

    # print colored("Testing on " + str(sauceParameters['platformName']) + ' ' + str(sauceParameters['appium:deviceName']), 'green')


    ###################################################################
    # Connect to Sauce Labs
    ###################################################################
    try:
        region
    except NameError:
        region = 'US'



    if region != 'EU':
        # print (colored("You are using the US data center", 'green'))
        driver = webdriver.Remote(
            # command_executor='https://jaxon.lee:f7958d00-80d2-413b-8bb2-2c86fa1bd419@ondemand.saucelabs.com:443/wd/hub',
            # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',

            desired_capabilities=sauceParameters)
    elif region == 'EU':
        # print (colored("You are using the EU data center", 'green'))
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    # ###################################################################
    # # Test logic goes here
    # ###################################################################
    # # Navigating to a website
    print (colored(str(datetime.datetime.now()), 'green'))
    # datetime.datetime.now()
    # print (driver.capabilities)
    # sleep(15)

    # # console.log(driver.capabilities['testobject_test_report_url'])
    # # print(driver.capabilities['testobject_test_live_view_url'])
    # # print (colored(driver.capabilities['testobject_device'], 'green', attrs=['reverse', 'blink']))
    #
    #
    # # driver.set_location(30.271493, -97.6222673, 14)
    # # sleep(10)
    # # driver.launch_app(com.apple.Preferences)
    # # driver.activate_app("com.apple.Preferences");
    # #
    # driver.get('https://saucelabs.com')
    # # interact = driver.find_element_by_name("q")
    # # interact.click()
    # # interact.send_keys('google')
    # # interact.submit()
    # # sleep(10)
    # # interact = driver.find_element_by_link_text('Maps')
    # # interact.click()
    #
    # sleep(100)
#     try:
#         print (colored("looking for Page", 'green'))
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "store-welcome-txt")))
#         # interact = driver.find_element_by_accessibility_id("I already have an account")
#         # interact.click()
#         print (colored("found page Welcom", 'green'))
#         # print (colored(driver.contexts, 'blue'))
#     except:
#         print (colored("Not loaded", 'red'))
#         # print (colored(interact.get_attribute('value'), 'blue'))
# # interact = driver.find_element_by_css_selector("input[type='email']")
#     sauce_result = "failed" if str(driver.current_url) != 'https://www.gymboree.com/ca/home' else "passed"
#     driver.execute_script("sauce:job-result={}".format(sauce_result))
#     #
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
    # # driver.get('https://app.test.smartsheet.com/b/form/8cc18ae2beac4717aa7156eabf5f1177?Primary+Column=Attachment+on+reloading+form&fakelogin=admin@mobiletest.com&fakepassword=test123123')
    #
    #
    # #
    # try:
    #     print (colored("looking for menu_share_form", 'green'))
    #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu_share_form')))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='menu_share_form']")
    #     interact = driver.find_element_by_name("menu_share_form")
    #     interact.click()
    #     print (colored("found No Thanks Button!!!", 'green'))
    # except:
    #     print (colored("Can not find menu_share_form", 'red'))
    #     # names = driver.find_elements_by_xpath(".//*")
    #     # print(colored(names.get_attribute(), 'green'))
    #     source = driver.page_source
        # interact = driver.find_element_by_class_name("menu_share_form")
        # interact = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Continue\"]").click()
        # interact.click()
        # print (colored("found No Thanks Button", 'green'))

    source = driver.page_source
    print(colored(source, 'red'))

    # dest_path = '/User/Desktop/signature.png'
    # data = bytes('/storage/emulated/0/Download/jpg.jpg', 'utf-8')
    # driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))

    # driver.push_file("storage/emulated/0/Download/mypng.png'","@/User/Desktop/signature.png")

    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_button_container")));
    # # # elementsList = driver.find_element_by_xpath("//*[@id]")
    # # # print elementsList
    # # # ids = driver.find_elements_by_xpath('//*[@name]')
    # # # ids = driver.find_elements_by_xpath('//*')
    # # # for ii in ids:
    # # #     if ii.get_attribute('name'):
    # # #         print colored("name: ", 'green'),  ii.get_attribute('name')
    # # #
    # # #     if ii.get_attribute('class'):
    # # #         print colored("class: ", 'red'), ii.get_attribute('class')
    # # #
    # # #     # if ii.get_attribute('value'):
    # # #         # print colored("class: ", 'red'), ii.get_attribute('value')
    # # #     # if ii.get_attribute('id'):
    # # #     #     print colored("id: ", 'yellow'), ii.get_attribute('id')
    # # #
    # # #     if ii.get_attribute('text'):
    # # #         print colored("text: ", 'blue'), ii.get_attribute('text')
    # #
    # # interact = driver.find_element_by_id("loginEditText")
    # # # interact.click()
    # # # interact.send_keys("AutomationTest")
    # # #
    # # #
    # # # interact = driver.find_element_by_id("passwordEditTtext")
    # # # interact.click()
    # # # interact.send_keys("Automation#123")
    # # # driver.hide_keyboard()
    # # #
    # # #
    # # #
    # # # interact = driver.find_element_by_id("loginButton")
    # # # interact.click()
    # # #
    # # # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # # # interact = driver.find_element_by_class_name("android.widget.Button")
    # # # interact.size
    # # # print interact.size
    # # # location = interact.location
    # # # print location
    # # # ids = driver.find_elements_by_xpath('//*')
    # # # for ii in ids:
    # # #
    # # #
    # # #
    # # #
    # #     if ii.get_attribute('value'):
    # #         print colored("value: ", 'red'), ii.get_attribute('value')
    # #
    # #     if ii.get_attribute('id'):
    # #         print colored("id: ", 'yellow'), ii.get_attribute('id')
    # # # #
    # # #     if ii.get_attribute('text'):
    # # #         print colored("text: ", 'blue'), ii.get_attribute('text')
    # # #         print colored("type: ", 'blue'), type(ii.get_attribute('text'))
    # # #         print colored("location: ", 'blue'), ii.location
    # # #         location = ii.location
    # # # # print location.get('y')
    # driver.switch_to().alert().accept()
    # # # # driver.switch_to().alert().accept()
    # # # # driver.switch_to().alert().accept()
    # # # actions = TouchAction(driver)
    # # # # actions.tap_and_hold(20, 20)
    # # # # actions.move_to(10, 10)
    # # # # actions.release()
    # # # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    # # #
    # # #
    # print "accepted 1"
    # #
    # # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # #
    # # interact = driver.find_element_by_class_name("android.widget.Button")
    # # interact.size
    # # print interact.size
    # # location = interact.location
    # # print location
    # # ids = driver.find_elements_by_xpath('//*')
    # # for ii in ids:
    #
    #
    #
    #
    #     # if ii.get_attribute('value'):
    #     #     print colored("value: ", 'red'), ii.get_attribute('value')
    #     #
    #     # if ii.get_attribute('id'):
    #     #     print colored("id: ", 'yellow'), ii.get_attribute('id')
    #
    # if ii.get_attribute('text'):
    #     print colored("text: ", 'blue'), ii.get_attribute('text')
    #     print colored("type: ", 'blue'), type(ii.get_attribute('text'))
    #     print colored("location: ", 'blue'), ii.location
    #     location = ii.location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    # # interact.click()
    # # alerts = driver.switch_to().alert
    # # alerts.accept()
    # print "accepted 2"
    #
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # ids = driver.find_elements_by_xpath('//*')
    # for ii in ids:
    #
    #
    #
    #
    #     # if ii.get_attribute('value'):
    #     #     print colored("value: ", 'red'), ii.get_attribute('value')
    #     #
    #     # if ii.get_attribute('id'):
    #     #     print colored("id: ", 'yellow'), ii.get_attribute('id')
    #
    #     if ii.get_attribute('text'):
    #         print colored("text: ", 'blue'), ii.get_attribute('text')
    #         print colored("type: ", 'blue'), type(ii.get_attribute('text'))
    #         print colored("location: ", 'blue'), ii.location
    #         location = ii.location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # print "accepted 3"

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # ids = driver.find_elements_by_xpath('//*')
    # for ii in ids:
    #
    #
    #
    #
    #     # if ii.get_attribute('value'):
    #     #     print colored("value: ", 'red'), ii.get_attribute('value')
    #     #
    #     # if ii.get_attribute('id'):
    #     #     print colored("id: ", 'yellow'), ii.get_attribute('id')
    #
    #     if ii.get_attribute('text'):
    #         print colored("text: ", 'blue'), ii.get_attribute('text')
    #         print colored("type: ", 'blue'), type(ii.get_attribute('text'))
    #         print colored("location: ", 'blue'), ii.location
    #         location = ii.location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # print "accepted 4"
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # for ii in ids:
    #     if ii.get_attribute('name'):
    #         print colored("name: ", 'green'),  ii.get_attribute('name')
    #
    #     if ii.get_attribute('class'):
    #         print colored("class: ", 'red'), ii.get_attribute('class')
    #
    #
    #
    #     if ii.get_attribute('text'):
    #         print colored("text: ", 'blue'), ii.get_attribute('text')
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # for ii in ids:
    #     if ii.get_attribute('name'):
    #         print colored("name: ", 'green'),  ii.get_attribute('name')
    #
    #     if ii.get_attribute('class'):
    #         print colored("class: ", 'red'), ii.get_attribute('class')
    #
    #
    #
    #     if ii.get_attribute('text'):
    #         print colored("text: ", 'blue'), ii.get_attribute('text')
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # for ii in ids:
    #     if ii.get_attribute('name'):
    #         print colored("name: ", 'green'),  ii.get_attribute('name')
    #
    #     if ii.get_attribute('class'):
    #         print colored("class: ", 'red'), ii.get_attribute('class')
    #
    #
    #
    #     if ii.get_attribute('text'):
    #         print colored("text: ", 'blue'), ii.get_attribute('text')
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
    # interact = driver.find_element_by_class_name("android.widget.Button")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # interact = driver.find_element_by_id("loginButton")
    # interact.click()
    # ids = driver.find_elements_by_xpath('//*')
    # for ii in ids:
    # #     if ii.get_attribute('name'):
    # #         print colored("name: ", 'green'),  ii.get_attribute('name')
    # #
    #     if ii.get_attribute('class'):
    #         print colored("class: ", 'red'), ii.get_attribute('class')
    #
    #     # if ii.get_attribute('value'):
    #         # print colored("class: ", 'red'), ii.get_attribute('value')
    #     # if ii.get_attribute('id'):
    #     #     print colored("id: ", 'yellow'), ii.get_attribute('id')
    #
    #     if ii.get_attribute('text'):
    #         print colored("text: ", 'blue'), ii.get_attribute('text')

    # WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "Open drawer")))
    # interact = driver.find_element_by_id("Open drawer")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "design_menu_item_text")))
    # interact = driver.find_element_by_id("design_menu_item_text")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fabButton")))
    # interact = driver.find_element_by_class_name("fabButton")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "android.widget.EditText")))
    # interact = driver.find_element_by_class_name("android.widget.EditText")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    # current_time = str(datetime.datetime.now())
    # interact.send_keys("Product " + current_time)
    #
    # interact = driver.find_element_by_class_name("saveButton")
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "android.widget.EditText")))
    # interact = driver.find_element_by_android_uiautomator('new UiSelector().textContains("current_time)')
    # interact.size
    # print interact.size
    # location = interact.location
    # print location
    # actions.tap(None, location.get('x'), location.get('y'), 1).perform()
    #
    # driver.current_activity
    #
    # driver.get_screenshot_as_base64()




    # ids = driver.find_elements_by_xpath('//*[@name]')
    # ids = driver.find_elements_by_xpath('//*[@id]')
    # for ii in ids:
    #     print colored("name: ", 'green'),  ii.get_attribute('name')
    #     print colored("class: ", 'red'), ii.get_attribute('value')
    #     print colored("id: ", 'blue'), ii.get_attribute('id')
    #     print colored("text: ", 'white'), ii.get_attribute('text')
    # print("Looking For Login Button")
    # interact = driver.find_element_by_name("loginButton")
    # print("Found Log In Button")
    # interact.click()
    # print("clicked log in button")
    #
    # ids = driver.find_elements_by_xpath('//*[@name]')
    # # ids = driver.find_elements_by_xpath('//*[@id]')
    # for ii in ids:
    #     print colored("name: ", 'green'),  ii.get_attribute('name')
    #     print colored("class: ", 'red'), ii.get_attribute('value')
        # print colored("id: ", 'blue'), ii.get_attribute('id')
        # print colored("text: ", 'white'), ii.get_attribute('text')

    # print "Setting Location"
    # driver.set_location(33.9137, -98.4934, 948)
    # print "Location Set"
    # # print driver.location();
    # sleep(5)
    # # # driver.execute_script("sauce: break")
    # #
    # print "Checking Google Location"
    # driver.toggle_location_services()
    # sleep(5)
    # driver.get('http://www.google.com/maps')
    # sleep(6)
    # # driver.switch_to().alert().accept()
    #
    # # driver.get('http://127.0.0.1:8000')/
    # driver.launch_app('Settings')
    # sleep(10)
    # print "Launching Maps App"
    # driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.Maps'})
    # sleep(10)
    # # driver.switch_to().alert().accept()
    # try:
    #     WebDriverWait(driver, 3).until(EC.alert_is_present(),
    #                                    'Timed out waiting for PA creation ' +
    #                                    'confirmation popup to appear.')
    #     print "Looking For Alert"
    #
    #     alert = driver.switch_to.alert
    #     print "Switched To Alert"
    #     ids = driver.find_elements_by_xpath('//*[@id]')
    #     # for ii in ids:
    #     #     print colored("name: ", 'green'),  ii.get_attribute('name')
    #     #     print colored("class: ", 'green'), ii.get_attribute('class')
    #     #     print colored("id: ", 'green'), ii.get_attribute('id')
    #     alert.accept()
    #     # driver.switch_to.alert.accept()
    #     print "alert accepted"
    # except TimeoutException:
    #     print "no alert"
    #
    # print "Checking Maps App"
    #
    #
    # sleep(10)

    # driver.get("https://www.ancestry.com/account/signin?returnUrl=https%3A%2F%2Fwww.ancestry.com");
    # driver.get("https://account.t-mobile.com/signin/v2/?redirect_uri=https:%2F%2Fmy.t-mobile.com&scope=TMO_ID_profile%20associated_lines%20billing_information%20associated_billing_accounts%20extended_lines%20token%20openid&client_id=MYTMO&access_type=ONLINE&response_type=code&approval_prompt=auto&device_type=desktop&prompt=select_account");
    #


    #
    #
    # interact.send_keys("4704350341")
    #
    # interact = driver.find_element_by_id("lp1-next-btn")
    # interact.click()
    #
    #
    # interact = driver.find_element_by_id("passwordTextBox")
    # interact.click()
    #
    # interact.send_keys("jawas123")
    #
    # interact = driver.find_element_by_id("lp2-login-btn")
    # interact.click()




    # driver.get('https://download.fromdoctopdf.com/index.jhtml')
    # interact = driver.find_element_by_css_selector(".customButton1_1")
    # interact.click()
    # sleep(5)
    # windows = driver.window_handles;
    # print(windows)
    # # driver.switch_to.alert()
    # windows = driver.window_handles;
    # print(windows)
    # # interact = driver.find_element_by_link_text("Run").click()
    #
    # interact = driver.find_element_by_class_name(".webstore-test-button-label")
    # interact.click()

    #
    # sleep(10)
    # driver.switch_to_frame("signInFrame");
    #
    # interact = driver.find_element_by_css_selector("#username")
    # interact.click()
    # interact.send_keys("cbertsaucelabs");
    #
    # interact = driver.find_element_by_css_selector("#password")
    # interact.click()
    # interact.send_keys("Testing1");
    #
    # interact.submit()
    #
    # sleep(5)
    # driver.switch_to_default_content()
    # sleep(5)
    # driver.get("https://www.ancestry.com/family-tree/person/tree/165320083/person/232153487798/facts");
    # sleep(5)
    # # ancBtn sml silver icon iconAdd optionsButton optionsButton768 hide480 addFactModal
    #
    # interact = driver.find_element_by_class_name("optionsButton768.hide480.addFactModal")
    # # interact = driver.find_element_by_class_name("ancBtn.silver.icon.iconAdd.optionsButton.show480.optionsButtonFacts")
    # sleep(5)
    # interact.click();
    #
    # sleep(15)
    # interact = driver.find_element_by_id("addFactSelect")
    # interact.click();
    #
    # sleep(5)
    # interact = driver.find_element_by_id("customevent")
    # interact.click();
    #
    # sleep(5)
    # interact = driver.find_element_by_id("title")
    # interact.send_keys("Title");
    #
    # interact = driver.find_element_by_id("date")
    # interact.click();
    # sleep(5)
    #__________________________________________________________________
    # driver.get("https://www.ancestry.com/account/signin/frame?returnUrl=https%3A%2F%2Fwww.ancestry.com")
    # # wait = WebDriverWait(driver, 20)
    # #
    # # driver.implicitly_wait(5000)
    # # sleep(5)
    # # driver.switch_to.frame("signInFrame");
    # # sleep(5)
    # # interact = driver.find_element_by_id("signInFrame").click()
    #
    #
    # # ids = driver.find_elements_by_xpath('//*[@id]')
    # # for ii in ids:
    # #     print colored("name: ", 'green'),  ii.get_attribute('name')
    # #     print colored("class: ", 'green'), ii.get_attribute('class')
    # #     print colored("id: ", 'green'), ii.get_attribute('id')
    #  # wait.until(EC.element_to_be_clickable(find_element_by_css_selector("img.signInLogo")));
    #
    # interact = driver.find_element_by_id("signInFrame")
    # interact.click()
    #
    # interact = driver.find_element_by_id("username")
    # interact.click()
    # interact.send_keys("cbertsaucelabs")
    # #
    # interact = driver.find_element_by_id("password")
    # interact.click()
    # interact.send_keys("Testing1")
    # #
    # interact = driver.find_element_by_id("signInBtn")
    # interact.click()



    # driver.switchTo().frame("signInFrame");
    # wait.until(EC.visibilityOfElementLocated(By.cssSelector("#username")));
    # wait.until(EC.visibilityOfElementLocated(By.cssSelector("#password")));
    # driver.findElement(By.cssSelector("#username"));
    # wait.until(EC.visibilityOfElementLocated(By.cssSelector("#username")));
    # driver.findElement(By.cssSelector("#username")).sendKeys("cbertsaucelabs");
    # driver.findElement(By.cssSelector("#password")).sendKeys("Testing1");
    # wait.until(EC.visibilityOfElementLocated(By.id("signInBtn")));
    # driver.findElement(By.id("signInBtn")).click();
    # driver.switchTo().defaultContent();
    #
    # # Setup for finding an element and clicking it
    # #__________________________________________________________________
    # # interact = driver.find_element_by_id('button1')
    # logtypes = driver.log_types
    # print(' ,'.join(logtypes)) #
    #
    # # print first and last 10 lines of logs
    # logs = driver.get_log('logcat')
    # # interact.click()
    # logtypes = driver.log_types
    # print(' ,'.join(logtypes)) #
    #
    # # print first and last 10 lines of logs
    # logs = driver.get_log('logcat')
    #
    # # interact.send_keys("Sauce Labs")
    # interact = driver.find_element_by_xpath("//android.widget.Button[@text='get started']")
    # interact.click()
    #
    # logtypes = driver.log_types
    # print(' ,'.join(logtypes)) #
    #
    # # print first and last 10 lines of logs
    # logs = driver.get_log('logcat')
    #
    # # interact = driver.press_keycode(66)
    # # interact = driver.find_element_by_id('net.ludeke.calculator:id/digit7')
    # # interact.click()
    #
    # logtypes = driver.log_types
    # print(' ,'.join(logtypes)) #
    #
    # # print first and last 10 lines of logs
    # logs = driver.get_log('logcat')
    #
    # sleep(5)
    # # interact = driver.find_element_by_partial_link_text('Sauce Labs')
    # # interact.click()
    # logtypes = driver.log_types
    # print(' ,'.join(logtypes)) #
    #
    # # print first and last 10 lines of logs
    # logs = driver.get_log('logcat')



    # Setup for finding an element and sending keystrokes
    #__________________________________________________________________
    # interact = driver.find_element_by_id('com.acadia.automation:id/signin_fields_login_hintText')
    # interact.click()
    # interact.send_keys('VibQA3+DEV+iyq1idxbtgphw10h@gmail.com')
    #
    # interact = driver.find_element_by_id('com.acadia.automation:id/signin_fields_password')
    # interact.click()
    # interact.send_keys('Password123!')
    #
    # interact = driver.hide_keyboard()
    #
    #
    # interact = driver.find_element_by_id('com.acadia.automation:id/signin_action_signin')
    # interact.click()


    # interact.get_attribute("value")
    #
    # interact.clear()
    # interact.get_attribute("value")
    #
    # interact.set_value('Dryzz')
    # interact.get_attribute("value")
    #
    # # interact.send_keys(BACK_SPACE)
    # sleep(35)
    #
    # interact2 = driver.find_element_by_id('u_0_g')
    # # interact.click()
    # interact2.get_attribute("value")
    #
    # interact2.clear()
    # interact2.get_attribute("value")
    #
    # interact2.set_value('11111')
    # sleep(5)
    # interact2.get_attribute("value")
    #
    # interact2.set_value('')
    # sleep(5)
    # interact2.get_attribute("value")
    #
    # interact2.set_value('Dryzz@@@@@@')
    # interact2.get_attribute("value")
    #
    # sleep(25)
    # result = driver.execute_script('mobile: shell', {
    # })


    # interact.submit()

    # Setup for using random Python commands
    #__________________________________________________________________
    # driver.save_screenshot('screenshot.png')
    # sleep(45)
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


if __name__ == '__main__' and region == 'US':
    jobs = [] # Array for the jobs
    print(colored(str(run) +" Tests running in the US data center.", 'green'))
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() # Start the functions.
        # print('this is the run for: '+ str(i))
        # sauceParameters.update({'name': 'Run ' + str(i) +': ' + str(datetime.datetime.now())})
        # print("You are using the US data center on run " + str(i))
elif __name__ == '__main__' and region != 'US':
    jobs = [] # Array for the jobs
    print(colored(str(run) +" Tests running in the EU data center.", 'green'))
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start()
