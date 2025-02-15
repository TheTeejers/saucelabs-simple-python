####################################################################
# Skeleton for Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
# Not always used for every test
###################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from datetime import datetime
import datetime
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import requests
import json
from selenium.webdriver.common.by import By
from termcolor import colored
import requests
from requests.auth import HTTPBasicAuth
# from reusableFxns import *

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
response = requests.get('https://api.us-west-1.saucelabs.com/team-management/v1/teams/',
            # auth = HTTPBasicAuth('sandeepvar', '01434d00-9812-4379-959b-776bf87e4145'))
            auth = HTTPBasicAuth(os.environ['SAUCE_USERNAME'], os.environ['SAUCE_ACCESS_KEY']))


# print request object
print(response)
print(response.content)

region = 'US'
# region = 'EU'


###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs Tests
###################################################################
sauceParameters = {
    'tags':['New', 'Build',],
    # 'name': 'Run: ' + str(datetime.datetime.now()),
    # 'name': 'Run without search between clicks',
    # 'platform': 'macos 11.00',
    # 'pageLoadStrategy': 'none',
    # 'platform': 'windows 7',
    # 'platform': 'windows 10',
    # 'platform': 'windows 8.1',
    # 'browserName': 'chrome',
    # 'browserName': 'internet explorer',
    # 'browserName': 'MicrosoftEdge',
    # 'browserName': 'firefox',
    'browserName': 'safari',
     "safari.options": {
      },
    # 'cleanSession': 'true',
    # "timeZone": "New_York",
    # 'browserLogLevel': 'SEVERE',
    # 'version': '75',
    # 'public':'share',
    # 'maxInstances': '5',
    # 'version': '11',
    # 'avoidProxy': False,
    }


# This concatenates the tags key above to add the build parameter
# sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

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
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',

        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        # command_executor='https://tj.invitationtest1:24168dc8-0900-4994-9ef9-f3442fb9683a@ondemand.saucelabs.com:443/wd/hub',

        desired_capabilities=sauceParameters)
elif region == 'EU':
    print( colored("You are using the EU data center", 'green'))
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)


###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
#__________________________________________________________________
# driver.set_window_size(1250, 250)

# print ('Platform Set: ' + driver.capabilities['platform'])
print (driver.capabilities)
print (driver.capabilities['webdriver.remote.sessionid'])
# print (sauceParameters)
# print ('Screen Resolution Set: ' + driver.capabilities['screenResolution'])
# driver.delete_all_cookies()
# driver.set_window_size(1,1)
# print('Set window size [set_window_size(1,1)]')
# print(driver.get_window_size)
# print (colored(driver.get_window_size(), 'green'))
# driver.get_window_size()

# print(driver.get_cookies())
# driver.get_cookies()
# driver.execute_script('sauce:throttleNetwork', {
#     "condition": {
#         "download": 1000,
#         "upload": 500,
#         "latency": 2
#     }
# })

# driver.execute_script('sauce:context=Open google.com')
#
# driver.get("https://www-qa1.dominos.com/en/?reset=1")
driver.get("https://google.com")
# document.querySelector(f)?.contentDocument.readyState, frame#
try:
    print (colored("looking for Page", 'green'))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@name='user']")))
    # interact = driver.find_element_by_accessibility_id("I already have an account")
    # interact.click()
    print (colored("user input found", 'red'))
    interact = driver.find_element_by_xpath("//*[@name='user']")
    print (colored("site failed to load", 'red'))

    interact.click()
    interact.send_keys('subrahmanyam.atmakuru@ice.com')
    interact = driver.find_element_by_xpath("//*[@name='password']")
    interact.click()
    interact.send_keys('Ice@9977#')
    interact = driver.find_element_by_xpath("//*[@name='loginPageSubmitBtn']")
    interact.click()

    # sauce_result = "failed"
    # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"

    # driver.execute_script('site failed to load')

    # driver.execute_script("sauce:job-result={}".format(failed))


    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("site loaded", 'green'))

# driver.get("https://the-internet.herokuapp.com/basic_auth")
# # print(driver.get_cookies())
#
#
# # print(driver.get_cookie('name'))
# # driver.get_cookie('name')
# # cookies_list = driver.get_cookies()
# # cookies_dict = {}
# # for cookie in cookies_list:
# #     cookies_dict[cookie['name']] = cookie['value']
# #
# # print(cookies_dict)
# # driver.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# driver.execute_script('sauce:context=Open new tab')
#
# driver.execute_script("window.open('');")
# driver.execute_script('sauce:context=Switch to new tab')
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.execute_script('sauce:context=Open saucelabs.com')
# driver.get("https://saucelabs.com")
#
# driver.execute_script('sauce:context=Get URL')
#
# # driver.current_url
#
# # print(driver.get_cookies())
# # driver.get_cookies()
# # driver.execute_script('sauce:throttleNetwork', {
# #     "condition": "offline"
# # })
# # sleep(180)
# # driver.get("https://admin-61c3464f.test.duosecurity.com/login");
# # #
# # # driver.switch_to_frame("signInFrame");
# # #
# # try:
# #     element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login_emailaddress_field")))
# # finally:
# #     print ("element found")
# #
# # # interact = driver.find_elements_by_xpath('//input[@id=\"login_emailaddress_field\"')
# # interact = driver.find_element_by_id("login_emailaddress_field")
# # interact.click()
# # interact.send_keys("test_au_unrestricted_admin@example.com");
# #
# #
# # interact = driver.find_element_by_id("login_continue_button")
# # interact.click()
# # interact.click()
# #
# #
# # element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "login_password_field")))
#
# # interact = driver.find_element_by_css_selector("#password")
# # interact.click()
# # interact.send_keys("Testing1");
# #
# interact.submit()

# driver.get('http://dev.newyorklife.com/resources/financial-calculators/retirement-savings-calculator')
# driver.execute_script("window.open('','_blank');")
# print(colored ("hello world!", "blue"))
# print(colored (str(driver.title), "red"))
# sleep(10)
#
# driver.execute_script("window.open('','_blank');")


# Setup for finding an element and clicking it
#__________________________________________________________________
# interact = driver.find_element_by_id('menu-item-112')
# interact.click()
# try:
#     print (colored("looking for Page", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@name='user']")))
#     # interact = driver.find_element_by_accessibility_id("I already have an account")
#     # interact.click()
#     print (colored("user input found", 'red'))
#     interact = driver.find_element_by_xpath("//*[@name='user']")
#     print (colored("site failed to load", 'red'))
#
#     interact.click()
#     interact.send_keys('subrahmanyam.atmakuru@ice.com')
#     interact = driver.find_element_by_xpath("//*[@name='password']")
#     interact.click()
#     interact.send_keys('Ice@9977#')
#     interact = driver.find_element_by_xpath("//*[@name='loginPageSubmitBtn']")
#     interact.click()
#
#     # sauce_result = "failed"
#     # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
#
#     # driver.execute_script('site failed to load')
#
#     # driver.execute_script("sauce:job-result={}".format(failed))
#
#
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("site loaded", 'green'))


# try:
#     print (colored("looking for Page", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-automation-id='application-menu-bar']")))
#     # interact = driver.find_element_by_accessibility_id("I already have an account")
#     # interact.click()
#     print (colored("user input found", 'red'))
#     interact = driver.find_element_by_xpath("//*[contains(text(),'Broker Share')]")
#     print (colored("site failed to load", 'red'))
#
#     interact.click()
#
#
#     # sauce_result = "failed"
#     # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
#
#     # driver.execute_script('site failed to load')
#
#     # driver.execute_script("sauce:job-result={}".format(failed))
#
#
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("site loaded", 'green'))


# try:
#     print (colored("looking for Page", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@title='Symbol linking']")))
#     # interact = driver.find_element_by_accessibility_id("I already have an account")
#     # interact.click()
#     print (colored("user input found", 'red'))
#     interact = driver.find_element_by_xpath("//*[@title='Symbol linking']")
#     print (colored("site failed to load", 'red'))
#
#     interact.click()
#
#
#     # sauce_result = "failed"
#     # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
#
#     # driver.execute_script('site failed to load')
#
#     # driver.execute_script("sauce:job-result={}".format(failed))
#
#
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("site loaded", 'green'))
#
#
#
# try:
#     print (colored("looking for Page", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@title,'Export to CSV')]")))
#     # interact = driver.find_element_by_accessibility_id("I already have an account")
#     # interact.click()
#     print (colored("user input found", 'red'))
#     interact = driver.find_element_by_xpath("//*[contains(@title,'Export to CSV')]")
#     print (colored("site failed to load", 'red'))
#
#     interact.click()
#     sleep(5)
#
#
#     # sauce_result = "failed"
#     # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
#
#     # driver.execute_script('site failed to load')
#
#     # driver.execute_script("sauce:job-result={}".format(failed))
#
#
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("site loaded", 'green'))
#
#
# try:
#     WebDriverWait(driver, 15).until(EC.alert_is_present())
#
#     alert = driver.switch_to.alert
#     alert.accept()
#     print("alert accepted")
# except TimeoutException:
#     print("no alert")
#
# sleep(10)
#
# try:
#     print (colored("looking for Page", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@title,'Export to CSV')]")))
#     # interact = driver.find_element_by_accessibility_id("I already have an account")
#     # interact.click()
#     print (colored("user input found", 'red'))
#     interact = driver.find_element_by_xpath("//*[contains(@title,'Export to CSV')]")
#     print (colored("site failed to load", 'red'))
#
#     interact.click()
#     sleep(5)
#
#
#     # sauce_result = "failed"
#     # sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
#
#     # driver.execute_script('site failed to load')
#
#     # driver.execute_script("sauce:job-result={}".format(failed))
#
#
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("site loaded", 'green'))

sleep(10)
# sauce_result = "passed" if str(driver.title) != 'dev.newyorklife.com' else "failed"
#
# # driver.execute_script('site failed to load')
#
# driver.execute_script("sauce:job-result={}".format(sauce_result))
# # # print(driver.get_cookies())
#
#
# # print(driver.get_cookie('name'))
# # driver.get_cookie('name')
# # cookies_list = driver.get_cookies()
# # cookies_dict = {}
# # for cookie in cookies_list:
# #     cookies_dict[cookie['name']] = cookie['value']
# #
# # print(cookies_dict)
# # driver.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# # driver.execute_script('sauce:context=Open new tab')
# #
# # driver.execute_script("window.open('');")
# # driver.execute_script('sauce:context=Switch to new tab')
# #
# # driver.switch_to.window(driver.window_handles[1])
#
# # driver.execute_script('sauce:context=Open saucelabs.com')
#
# # driver.execute_script('sauce:context=Get URL')
# try:
#     print (colored("looking for username", 'green'))
#     WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, 'username')))
#     show = driver.presence_of_element_located((By.ID, 'username'))
#     print (show)
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_id("username")
#     interact.click()
#     print (colored("found username!!!", 'green'))
#     interact.send_keys("Srinatha.gangadharaiah+Automation@unqork.com")
# except:
#     print (colored("Can not find username", 'red'))
#
# try:
#     print (colored("looking for password", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_id("password")
#     interact.click()
#     print (colored("found password!!!", 'green'))
#     interact.send_keys("Automation123")
#     interact.submit()
# except:
#     print (colored("Can not find password", 'red'))
#
#
# try:
#     print (colored("looking for remove", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Remove ']")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//button[text()=' Remove ']")
#     interact.click()
#     print (colored("found remove!!!", 'green'))
#
# except:
#     print (colored("Can not find remove", 'red'))
#
# try:
#     print (colored("looking for btnGetStarted", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"btnGetStarted\"]/span")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id=\"btnGetStarted\"]/span")
#     interact.click()
#     print (colored("found btnGetStarted!!!", 'green'))
#
# except:
#     print (colored("Can not find btnGetStarted", 'red'))
#
# try:
#     print (colored("looking for insuredFirstName", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredFirstName\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     if driver.presence_of_element_located((By.XPATH, "//button[text()=' Remove ']"))) ==
#         interact = find_element_by_xpath("//button[text()=' Remove ']")
#         interact.click()
#     interact = driver.find_element_by_xpath("//*[@id=\"insuredFirstName\"]")
#     interact.click()
#     interact.clear()
#     print (colored("found insuredFirstName!!!", 'green'))
#     interact.send_keys("Nineteen AL")
#
#
# except:
#     print (colored("Can not find insuredFirstName", 'red'))
#
# try:
#     print (colored("looking for insuredLastName", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredLastName\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id=\"insuredLastName\"]")
#     interact.click()
#     interact.clear()
#     print (colored("found insuredLastName!!!", 'green'))
#     interact.send_keys("Moore")
#
#
# except:
#     print (colored("Can not find insuredLastName", 'red'))
#
# try:
#     print (colored("looking for insuredDOB", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredDOB\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id=\"insuredDOB\"]")
#     interact.click()
#     interact.clear()
#     print (colored("found insuredDOB!!!", 'green'))
#     interact.send_keys("11162001")
#
#
# except:
#     print (colored("Can not find insuredDOB", 'red'))
#
# try:
#     print (colored("looking for Male", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),\"Male\")]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[contains(text(),\"Male\")]")
#     interact.click()
#     # interact.clear()
#     print (colored("found Male!!!", 'green'))
#     # interact.send_keys("11162001")
#
#
# except:
#     print (colored("Can not find Male", 'red'))
#
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
#
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
#
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
#
#
# # POST keys....?
# # try:
# #     print (colored("looking for react-select-2-input", 'green'))
# #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-select-2-input\"]")))
# #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
# #     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
# #     interact = driver.find_element_by_xpath("//*[@id=\"react-select-2-input\"]")
# #     interact.click()
# #     interact.clear()
# #     print (colored("found react-select-2-input!!!", 'green'))
# #     interact.send_keys("2201 University Blvd, Tuscaloosa, AL 35401")
# #
# #
# # except:
# #     print (colored("Can not find react-select-2-input", 'red'))
#
# try:
#     print (colored("looking for insuredMobilePhone", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredMobilePhone\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id=\"insuredMobilePhone\"]")
#     print ('before click mobile phone number Value is ' + interact.get_attribute("value"))
#
#     interact.click()
#     print ('after click mobile phone number Value is ' + interact.get_attribute("value"))
#
#     interact.clear()
#     print ('after clear mobile phone number Value is ' + interact.get_attribute("value"))
#     # print (interact.get_attribute("value"))
#
#
#     print (colored("found insuredMobilePhone!!!", 'green'))
#     interact.send_keys("6466171203")
#     # sleep(5)
#     # print (interact.attribute(value))
#
#
#
# except:
#     print (colored("Can not find insuredMobilePhone", 'red'))
#
# try:
#     print (colored("looking for insuredSSN", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredSSN\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id=\"insuredSSN\"]")
#     print ('before click SSN Value is ' + interact.get_attribute("value"))
#
#     interact.click()
#     print ('after click SSN Value is ' + interact.get_attribute("value"))
#
#     interact.clear()
#     print ('after clear SSN Value is ' + interact.get_attribute("value"))
#
#     print (colored("found insuredSSN!!!", 'green'))
#     interact.send_keys("021891234")
#     print ('after send keys SSN Value is ' + interact.get_attribute("value"))
#
#
# except:
#     print (colored("Can not find insuredSSN", 'red'))
#
# try:
#     print (colored("looking for insuredIDType", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id=\"insuredIDType\"]")
#     print (interact)
#     print (type(interact))
#     # interact.click()
#     # interact.clear()
#     print (colored("found insuredIDType!!!", 'green'))
#     # interact.send_keys("021891234")
#     driver.execute_script("arguments[0].scrollIntoView(true);", interact)
#     action = ActionChains(driver)
#     action.move_to_element(interact).perform()
#
#
#
#
# except:
#     print (colored("Can not find insuredIDType", 'red'))
#
# try:
#     print (colored("looking for insuredIDType", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     # interact = driver.find_element_by_xpath("//*[@id='insuredIDType'][@value='select']")
#     # interact = driver.find_element_by_xpath("//*[@value='select']")
#     # interact.click()
#     interact.get_attribute("name")
#     print (colored("found insuredIDType!!!", 'green'))
#     # interact.send_keys("021891234")
#
#
# except:
#     print (colored("Can not find insuredIDType", 'red'))
#
# try:
#     print (colored("looking for option", 'green'))
#     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "option")))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDType\"]")))
#
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     print ('made it here')
#     interact = driver.find_elements_by_xpath("//*[@id=\"insuredIDType\"]/option")
#     print ('and here')
#     interact
#     print ('also here')
#     # interact1 = driver.find_element_by_xpath("//*[@id=\"insuredIDType\"]/option/")
#
#     # interact = driver.find_elements_by_tag_name("option")
#     # interact.click()
#     # interact.clear()
#     # interact.get_attribute()
#     print (len(interact))
#
#     for i in range(len(interact)):
#
#         # interact.get_attribute('label')
#         # print(interact.get_attribute('label'))
#
#         # print (interact[i].text)
#         print (interact[i].tag_name)
#         print (type(interact[i]))
#         print (interact[i].get_attribute("label"))
#         # print (interact[i].element)
#
#         if interact[i].get_attribute("label") == "State ID Number":
#             interact[i].click()
#
#     print (colored("found option!!!", 'green'))
#     # print (interact.value)
#     # interact.send_keys("021891234")
#
#
# except:
#     print (colored("Can not find option", 'red'))
#
# try:
#     print (colored("looking for insuredIDType", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredStateIDNumber\"]")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
#     # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='noThanks_btn']")
#     interact = driver.find_element_by_xpath("//*[@id='insuredStateIDNumber']")
#     # interact = driver.find_element_by_xpath("//*[@value='select']")
#     # interact.click()
#     # interact.clear()
#     print (colored("found insuredStateIDNumber!!!", 'green'))
#     interact.send_keys("H12345678901234")
#
#
# except:
#     print (colored("Can not find insuredStateIDNumber", 'red'))
#
# try:
#     print (colored("looking for option", 'green'))
#     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "option")))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"insuredIDState\"]")))
#
#     interact = driver.find_elements_by_xpath("//*[@id=\"insuredIDState\"]/option")
#
#     interact
#     print (len(interact))
#
#     for i in range(len(interact)):
#
#         # print (interact[i].tag_name)
#         # print (type(interact[i]))
#         # print (interact[i].get_attribute("label"))
#         # print (interact[i].element)
#
#         if interact[i].get_attribute("label") == "Alabama":
#             interact[i].click()
#
#     print (colored("found Alabama!!!", 'green'))
#     # print (interact.value)
#     # interact.send_keys("021891234")
#
#
# except:
#     print (colored("Can not find Alabama", 'red'))
#
# try:
#     print (colored("looking for insuredIDType", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"btnContinue\"]")))
#     interact = driver.find_element_by_xpath("//*[@id=\"btnContinue\"]")
#
#     print (colored("found btnContinue!!!", 'green'))
#     interact.click()
#
#
# except:
#     print (colored("Can not find btnContinue", 'red'))
#
#
#
#
# try:
#     print (colored("looking for insuredIDType", 'green'))
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span]")))
#     interact = driver.find_element_by_xpath("//*[@id=form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span]")
#
#     print (colored("found form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span!!!", 'green'))
#     interact.click()
#
#
# except:
#     print (colored("Can not find form-group-haveConvictedGuiltyInLastTwoYears\"]/div[1]/div[3]/label/span", 'red'))
#
# # sleep(5)
# # driver.switch_to_default_content()
# # sleep(5)
# # driver.get("https://www.ancestry.com/family-tree/person/tree/165320083/person/232153487798/facts");
# # sleep(5)
# # # ancBtn sml silver icon iconAdd optionsButton optionsButton768 hide480 addFactModal
# #
# # interact = driver.find_element_by_class_name("optionsButton768.hide480.addFactModal")
# # # interact = driver.find_element_by_class_name("ancBtn.silver.icon.iconAdd.optionsButton.show480.optionsButtonFacts")
# # sleep(5)
# # interact.click();
# #
# # sleep(15)
# # interact = driver.find_element_by_id("addFactSelect")
# # interact.click();
# #
# # sleep(5)
# # interact = driver.find_element_by_id("customevent")
# # interact.click();
# #
# # sleep(5)
# # interact = driver.find_element_by_id("title")
# # interact.send_keys("Title");
# #
# # interact = driver.find_element_by_id("date")
# # interact.click();
# # sleep(5)
# # ids = driver.find_elements_by_xpath('//*[@id]')
# # for ii in ids:
# #     print( colored("name: ", 'green'),  ii.get_attribute('name'))
# #     print( colored("class: ", 'red'), ii.get_attribute('class'))
# #     print( colored("id: ", 'blue'), ii.get_attribute('id'))
#
# # _browser_profile = webdriver.FirefoxProfile()
# # _browser_profile.set_preference("dom.webnotifications.enabled", False)
# # webdriver.Firefox(firefox_profile=_browser_profile)
# #
# # driver.get('https://www.cbtnuggets.com/login')
# # driver.get('https://gauntface.github.io/simple-push-demo/')
# # driver.get('https://www.qa.apartmentguide.com')
# # popup = driver.switch_to_alert
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://saucelabs.com/",
# #     "response": {
# #         "statusCode": 200,
# #
# #
# #     }
# # })
#
#
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://google.com",
# #     # "error": "Failed"
# #     "response": {
# #         "status": 500,
# #             "body": [{
# #                 "title": "Hello, the page has a 500 error",
# #             }],
# #     }
# # })
#
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://google.com",
# #     "redirect": "https://saucelabs.com"
# # })
# # sleep(5)
# #
# # driver.get('https://login.tigerconnect.com/env7/app/messenger/')
# # driver.get('https://google.com')
# # driver.get()
# # driver.get('https://qa-app.pactsafe.com/')
# # driver.implicitly_wait(30)
# # driver.get('https://phishstaging.infosecinstitute.com/Training/Dv89eX/17')
#
# # Setup for finding an element and clicking it
# #__________________________________________________________________
# # interact = driver.find_element_by_id('ps-login-email')
# # interact.send_keys('tyler+saucetest@pactsafe.com')
# # # interact.send_keys('zaphodbeeblebrox_usqa@mailinator.com')
# # interact = driver.find_element_by_id('ps-login-password')
# # # interact.send_keys('test1234')
# # interact.send_keys('317brydonrd')
# # interact = driver.find_element_by_id('submit-login')
# # interact.click()
# # interact = driver.find_element_by_name('q')
# # interact.click()
# # # sleep(20)
# # interact.clear()
# # interact.send_keys("local time")
# #
# # interact.submit()
# # sleep(5)
# #
# # source = driver.page_source
# # # print(colored(source.split(' '), 'red'))
# # print(colored(type(source), 'red'))
# # print(colored(len(source), 'red'))
# # print(colored(driver.get_source, 'green'))
#
# # for elm in driver.find_elements_by_css_selector("*"):
# #     print(elm)
# # header = driver.find_element_by_id("gsr")
# #
# # # start from your target element, here for example, "header"
# #
# # all_children_by_css = header.find_elements_by_css_selector("*")
# #
# # all_children_by_xpath = header.find_element_by_xpath(".//*")
# # # all_children_by_xpath = header.find_elements_by_xpath(".//*")
# #
# # print ('len(all_children_by_css): ' + str(len(all_children_by_css)))
# #
# # # print ('len(all_children_by_xpath): ' + str(len(all_children_by_xpath)))
# # print ('len(all_children_by_xpath): ' + all_children_by_xpath.get_attribute("outerHTML"))
# #
# # print ('str(all_children_by_css): ' + all_children_by_css.get_attribute("outerHTML"))
#
# # ids = driver.find_elements_by_xpath('//*[@id]')
# # for ii in ids:
# #     # print (ii)
# #     # print (ii.value)
# #     print (ii.get_attribute('id'))
#
# # driver.get('https://connect-web.staging.dataservices.theice.com')
#
# # interact = driver.find_element_by_tag_name("body")
# #
# # interact.send_keys(Keys.CONTROL + Keys.ADD)
# # interact.send_keys(Keys.CONTROL + Keys.ADD)
# # interact.send_keys(Keys.CONTROL + Keys.ADD)
# # interact.send_keys(Keys.CONTROL + Keys.ADD)
# # interact.send_keys(Keys.CONTROL + Keys.ADD)
#
# # #
# # # sleep(5)
# #
# # driver.get('https://www.epochconverter.com/')
#
#
# # print((driver.get_cookies()))
# # driver.delete_all_cookies()
# # print((driver.get_cookies()))
# # driver.add_cookie({ "name": "isAutomation", "value": "true" })
# # print((driver.get_cookies()))
#
# # sleep(15)
# # ids = driver.find_elements_by_xpath('//*')
# # for ii in ids:
# #     if ii.get_attribute('name'):
# #         print( colored("name: ", 'green'),  ii.get_attribute('name'))
# #
# #     if ii.get_attribute('class'):
# #         print( colored("class: ", 'red'), ii.get_attribute('class'))
# #
# #     if ii.get_attribute('value'):
# #         print( colored("class: ", 'red'), ii.get_attribute('value'))
# #
# #     if ii.get_attribute('id'):
# #         print( colored("id: ", 'yellow'), ii.get_attribute('id'))
# #
# #     if ii.get_attribute('text'):
# #         print( colored("text: ", 'blue'), ii.get_attribute('text'))
# # driver.save_screenshot('screenie.png')
# # driver.get('https://hp.myway.com/packagetracer/ttab02/index.html')
#
#
# #
#
#
#
#
# #
# # driver.delete_all_cookies()
# # sleep(5)
# # get_title = driver.title
# # print((get_title))
# #
# # interact = driver.find_elements_by_xpath("//*[@id='ProductSearchOnBoardingModalModal']")
# #
# # interact = driver.find_element_by_css_selector("#appModalModal")
# # interact = driver.find_element_by_css_selector("#ProductSearchOnBoardingModalModal")
# # const event = new Date('August 19, 1975 23:15:30');
# # event.setHours(20);
# #
# # console.log(event);
# # // expected output: Tue Aug 19 1975 20:15:30 GMT+0200 (CEST)
# # // (note: your timezone may vary)
# #
# # event.setHours(20, 21, 22);
# #
# # console.log(event);
# # // expected output: Tue Aug 19 1975 20:21:22 GMT+0200 (CEST)
# #
# #
# # var date = new Date();
# # date.setHours(0, 0, 0, 0);
# # var numberOfDaysToAdd = 0;
# # date.setDate(date.getDate() + numberOfDaysToAdd);
# #
# #
# #
# #
# #
# #
# #
# #
# # interact = driver.find_elements_by_xpath("//[@id='root']//input']")
# # # #
# # interact = driver.find_element_by_id("ecinput")
# #
# # interact.click()
# # interact.clear()
# #
# # interact.send_keys(1593147600000)
# # interact.submit()
# # # interact = driver.find_element_by_id("id_email")
# # interact.click()
# # # interact = driver.find_element_by_id("id_email")
# # interact.click()
# # # interact = driver.find_element_by_id("id_email")
# # interact.click()
#
# # driver.close()
#
# # sleep(5)
#
#
#
# # THIS AREA TO USE FOR THE TMOBILE TEST
#
# # driver.get('https://download.fromdoctopdf.com/index.jhtml')
# # interact = driver.find_element_by_css_selector(".customButton1_1")
# # interact.click()
# # sleep(5)
# # windows = driver.window_handles;
# # print((windows))
# # # driver.switch_to.alert()
# # windows = driver.window_handles;
# # print((windows))
# # # interact = driver.find_element_by_link_text("Run").click()
# #
# # interact = driver.find_element_by_class_name(".webstore-test-button-label")
# # interact.click()
#
# # Setup for finding an element and clicking it
# #__________________________________________________________________
# # interact = driver.find_element_by_id('theTime')
# # # interact.click()
# # print((interact.text))
# # print(('datetime: ' + str(datetime.datetime.now())))
# # interact = driver.get('https://freegeoip.app/xml/')
# #
# # interact = driver.find_element_by_id('collapsible0')
# # print((interact.text))
# # sleep(89)
#
# # driver.get("https://www.msn.com");
# #
# #
# #
# # loc = driver.find_element_by_id("sb_form_go1")
# # print((loc.location))
# # print((loc.size))
# # sleep(90)
# # Setup for finding an element and clicking it
# #__________________________________________________________________
# # interactive tabbed-standard
#
#
# # interact = driver.find_element_by_css_selector("a[href='/support']").click()
# # interact = driver.find_element_by_css_selector("a[href='https://wiki.saucelabs.com/']").click()
#
# # sleep(15)
# # iframe = driver.switch_to.frame(find_element_by_class('interactive'))
# # iframe = driver.switch_to.frame(find_element_by_class_name('interactive'))
# # interact = driver.find_element_by_link_text("Documentation").click()
# # interact = driver.find_element_by_id("i_am_a_textbox").send_keys("Sauce")
#
# # interact = driver.find_element_by_name("q")
#
# # try:
# # element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((driver.find_element_by_id("email"))))
# # finally:
#     # driver.quit()
# # interact = driver.find_element_by_id("email")
# # interact = driver.find_element_by_class_name("layer-wiziwig ")
# # interact.click()
# # interact.send_keys('atesting+444bop@cbtnuggets.com')
# # interact = driver.find_element_by_id("password")
# # interact.click()
# # interact.send_keys('XJstgWsu3dwchRyDr')
# # interact.submit()
# #
# # fun sendKeys(element: WebElement, value: String) {
# # val length = element.getAttribute("value").length
# # for (i in 0 until length)
# # element.sendKeys("\u0008")
# # element.sendKeys(value)
# # }
#
# # Setup for finding an element and sending keystrokes
# #__________________________________________________________________
# # interact = driver.find_element_by_class_name('_1MDYA').click()
# # chrome_options = webdriver.ChromeOptions()
# # prefs = {"profile.default_content_setting_values.notifications" : 2}
# # chrome_options.add_experimental_option("prefs",prefs)
# # driver = webdriver.Chrome(chrome_options=chrome_options)
#
#
# # interact.send_keys('Leonard, TX')
# # interact.send_keys('Leonard, TX')
# # interact.submit()
#
# # Setup for using random Python commands
# #__________________________________________________________________
# # driver.save_screenshot('screenshot.png')
# # sleep(15)
# # print ('Message')
# # interact = driver.find_element_by_class_name("mdl-button__ripple-container").click()
# # sleep(15)
#
# # Setup for using Action chains
# #__________________________________________________________________
# # ActionChains(driver).move_to_element(interact).perform()
#
# # Setup for random script executions
# #__________________________________________________________________
# # driver.execute_script('sauce: break')
#
# driver.execute_script('sauce:context=Change name of test')
# driver.execute_script('sauce:job-name=Name Changed via JavascriptExecutor')
# # driver.execute_script('sauce:job-name=Name Changed via JavascriptExecutor ' + sauceParameters["name"])
#
# # print (driver.current_url)
# sauce_result = "failed" if str(driver.current_url) != 'https://saucelabs.com/' else "passed"
#
# driver.execute_script('sauce:job-name=Status changed via JavascriptExecutor if driver.current_url == https://saucelabs.com/')
#
# driver.execute_script("sauce:job-result={}".format(sauce_result))

# Ending the test session
# driver.download_(driver.session_id(), "/var/tmp/");
#__________________________________________________________________
driver.quit()
# sauce.downloadHAR("job_id", "/var/tmp/");
