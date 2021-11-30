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

# useApp = True
# appLocation = 'https://github.com/truongsinh/android_flutter_host/releases/download/0.0.1/app-free-debug.apk'
# appLocation = 'maps'
# appLocation = ""
appLocation = 'storage:25e76be0-bc67-49d1-a785-a22bfd0e1d90'
# appLocation = 'storage:f9232cab-fb1c-4340-b3f9-e3d8f2398abb'
# appLocation = 'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'



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
        # 'app': 'storage:f5988b56-89f1-4db8-b9a8-d4e2a8f0887c', #ios smartsheets
        # 'app': 'storage:59549449-8b97-47c5-9343-f76799cc4fe4', #android smartsheets
        # 'app':'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'
    }

    androidParameters = { # Define Android parameters here
        # 'deviceName' : "Google Pixel GoogleAPI Emulator",
        # 'deviceName' : 'Android',
        # 'platformVersion' : '8.1',
        # 'platformName' : 'Android',
        # 'appium:deviceName': 'Android',
        'deviceOrientation' : 'portrait',
        # 'relaxedSecurityEnabled': True,
        # 'autoGrantPermissions': True,
        # 'ignoreUnimportantViews': True,
        # 'automationName': 'UiAutomator2',
        # 'gpsEnabled': True,
        # 'maxDuration': 10800,
        # 'recordScreenshots': False
        'browserName': '',
        # 'platformVersion': 'latest',

        # 'deviceName': 'Amazon_Kindle_Fire_HD_10_real',
        'deviceName': 'Android GoogleAPI Emulator',
        'platformVersion': '11.0',
        'platformName': 'Android',
        # 'gpsEnabled': False


    }

    iosParameters = { # Define iOS Parameters here

        # 'deviceName' : 'iPhone X Simulator',
        'deviceName' : 'iPhone 11 Simulator',
        'deviceOrientation' : 'portrait',
        'platformVersion' : '14.0',
        'platformName' : 'iOS',
        'avoidProxy': True,
        # 'platformName' : 'iOS',
        # 'autoWebview': 'true',
        # 'bundleId': 'com.apple.Maps',
        # 'browserName': 'safari',
        # 'nativeWebTap': True, # iOS only capability.
        'autoAcceptAlerts': True,
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
        # print (colored("You are using the US data center", 'green'))
        driver = webdriver.Remote(
            # command_executor='https://jaxon.lee:f7958d00-80d2-413b-8bb2-2c86fa1bd419@ondemand.saucelabs.com:443/wd/hub',
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
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
    # # Navigating to a website
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
        print (colored("looking for username", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'username')))
        show = EC.presence_of_element_located((By.ID, 'username'))
        print (show)
        interact = driver.find_element_by_id("username")
        interact.click()
        print (colored("found username!!!", 'green'))
        interact.send_keys("Srinatha.gangadharaiah+Automation@unqork.com")
    except:
        print (colored("Can not find username", 'red'))

    try:
        print (colored("looking for password", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
        interact = driver.find_element_by_id("password")
        interact.click()
        print (colored("found password!!!", 'green'))
        interact.send_keys("Automation123")
        interact.submit()
    except:
        print (colored("Can not find password", 'red'))


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

    try:
        print (colored("looking for Search...", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Search...']")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//div[text()='Search...']")
        interact.click()
        # interact.clear()
        print (colored("found Search...!!!", 'green'))
        # interact.send_keys("11162001")


    except:
        print (colored("Can not find Search...", 'red'))

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
        print (colored("looking for react-select-2-input", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-select-2-input\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        print (colored("found react-select-2-input!!!", 'green'))
        interact = driver.find_element_by_xpath("//*[@id=\"react-select-2-input\"]")
        interact.click()
        print (colored("clicked react-select-2-input!!!", 'green'))

        interact.clear()
        print (colored("cleared react-select-2-input!!!", 'green'))
        interact.send_keys("2201 University Blvd, Tuscaloosa, AL 35401")


    except:
        print (colored("Can not find react-select-2-input", 'red'))


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
        print (colored("looking for insuredIDType", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[@id=\"insuredIDType\"]")
        print (interact)
        print (type(interact))
        # interact.click()
        # interact.clear()
        print (colored("found insuredIDType!!!", 'green'))
        # interact.send_keys("021891234")
        driver.execute_script("arguments[0].scrollIntoView(true);", interact)
        action = ActionChains(driver)
        action.move_to_element(interact).perform()




    except:
        print (colored("Can not find insuredIDType", 'red'))

    try:
        print (colored("looking for insuredIDType", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        # interact = driver.find_element_by_xpath("//*[@id='insuredIDType'][@value='select']")
        # interact = driver.find_element_by_xpath("//*[@value='select']")
        # interact.click()
        interact.get_attribute("name")
        print (colored("found insuredIDType!!!", 'green'))
        # interact.send_keys("021891234")


    except:
        print (colored("Can not find insuredIDType", 'red'))

    try:
        print (colored("looking for option", 'green'))
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "option")))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))

        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        print ('made it here')
        interact = driver.find_elements_by_xpath("//*[@id=\"insuredIDType\"]/option")
        print ('and here')
        interact
        print ('also here')
        # interact1 = driver.find_element_by_xpath("//*[@id=\"insuredIDType\"]/option/")

        # interact = driver.find_elements_by_tag_name("option")
        # interact.click()
        # interact.clear()
        # interact.get_attribute()
        print (len(interact))

        for i in range(len(interact)):

            # interact.get_attribute('label')
            # print(interact.get_attribute('label'))

            # print (interact[i].text)
            print (interact[i].tag_name)
            print (type(interact[i]))
            print (interact[i].get_attribute("label"))
            # print (interact[i].element)

            if interact[i].get_attribute("label") == "State ID Number":
                interact[i].click()
                print("clicked")

        print (colored("found option!!!", 'green'))
        # print (interact.value)
        # interact.send_keys("021891234")


    except:
        print (colored("Can not find option", 'red'))

    try:
        print (colored("looking for insuredStateIDNumber", 'green'))
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredStateIDNumber\"]")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"insuredStateIDNumber\"]")))

        # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
        # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
        interact = driver.find_element_by_xpath("//*[@id='insuredStateIDNumber']")
        # interact = driver.find_element_by_xpath("//*[@value='select']")
        interact.click()
        # interact.clear()
        print (colored("found insuredStateIDNumber!!!", 'green'))
        interact.send_keys("H12345678901234")


    except:
        print (colored("Can not find insuredStateIDNumber", 'red'))

    try:
        print (colored("looking for option", 'green'))
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "option")))
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
        print (colored("looking for form-group-haveConvictedGuiltyInLastTwoYears", 'green'))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span]")))
        interact = driver.find_element_by_xpath("//*[@id=form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span]")

        print (colored("found form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span!!!", 'green'))
        interact.click()


    except:
        print (colored("Can not find form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span", 'red'))
    #_________________________________
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
