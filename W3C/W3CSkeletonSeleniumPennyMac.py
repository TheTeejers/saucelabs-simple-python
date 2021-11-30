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
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from datetime import datetime, date, time, timezone
import datetime

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
# from reusableFxns import *
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# import KEYS
from selenium.webdriver.common.keys import Keys

import requests
import json
from termcolor import colored

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

region = 'US'

###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs Tests
###################################################################
sauceParameters = {
    # Required platform information
    # 'platformName': 'macOS 10.13',
    # 'browserName': 'safari',
    # 'browserVersion': 'latest',
    # 'name': 'Run: ' + str(datetime.datetime.now()),
    #
    # # Options used by Sauce Labs
    # 'sauce:options':{
    #     'tags':['Case', 'NUM',],
    #     # 'name': 'Run: ' + str(datetime.datetime.now()),
    #     # 'extendedDebugging': 'true',
    #     # 'capturePerformance': 'true',
    #     # "webdriver.remote.quietExceptions": 'true',
    #     # 'tunnelIdentifier':'Phill Tunnel One',
    #     # 'screenResolution':'1920x1080',
    #     # 'seleniumVersion': '3.141.59',
    #     # 'iedriverVersion': '3.4.0',
    #     # 'chromedriverVersion': '2.40',
    #     # 'requireWindowFocus' : True,
        'maxDuration': 5000,
    #     # 'idleTimeout': 1000,
    #     # 'commandTimeout': 600,
    #     # 'videoUploadOnPass':False,
    #     # 'extendedDebugging':'true',
    # "prerun":"https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat",

    # },
    # 'count': 1,
    'platformName': 'macos 11.00',
    # 'platformName': 'windows 10',
    'browserName': 'firefox',
    'acceptInsecureCerts': True,
    # 'browserName': 'MicrosoftEdge',
    # 'browserName': 'internet explorer',
    # 'browserName': 'chrome',
    # 'browserName': 'safari',
    # 'version': '13',
    # 'browserVersion': 'dev',
    'browserVersion': '92',
    # 'extendedDebugging':'true',

    # 'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    # 'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',
    # 'public':'private',
    'sauce:options': {
        'name':'Penny Mac Testing',
        # 'tags':'13128733',
        # 'extendedDebugging':'true',
        # 'prerun':{
        #     'executable':'storage:filename=disable_fraud.sh',
        #     'background': 'false'
        # }
        'build':'Penny Mac Testing',
        # 'screenResolution':'2560x1600',

        # 'avoidProxy': 'true',
        # 'capturePerformance': 'true',
        # 'seleniumVersion': '4.0.0',
        "idleTimeout": 450,
        # 'public':'private',
        # 'name': 'https://dev.testinghub.autodesk.com/ test of drop down menu',
        # 'extendedDebugging':'true',
        # "timeZone": "New_York",
        # 'tunnelIdentifier': 'newguy'
        # 'tunnelIdentifier': 'tj111::sauce::468f60825c404ca889c5b420c790c80b'
    # 'safari.options':{},

        # 'name': 'UI-Mobile-QA-Regression-tests-Hari',
        # 'build': 'Trying to break it',
        #
        #
        # 'tunnelIdentifier': 'tj',
    },

    # 'sauce:options': {
    #     # 'name': 'UI-Mobile-QA-Regression-tests-Hari',
    #     # 'build': 'Trying to break it',
    #     #
    #     #
    #     # 'tunnelIdentifier': 'tj',
    # },


    # Options used by Chrome
    # 'goog:chromeOptions':{
    #     # 'w3c': True,    # Required for a W3C Chrome test
    #     # 'mobileEmulation':{'deviceName':'iPhone X'},
    #     # 'prefs': {
    #     #     'profile': {
    #     #         'password_manager_enabled': False
    #     #         },
    #     #         'credentials_enable_service': False,
    #     #     },
    #     'args': ['--auto-open-devtools-for-tabs'],
    # },
    # 'moz:firefoxOptions':{
    #     # "log": {"level": "trace"},
    #     # 'geckodriverVersion':'0.27.0',
    #     # 'args': ['--headless']
    # },
    # 'moz:debuggerAddress': True
}


# This concatenates the tags key above to add the build parameter
# sauceParameters['sauce:options'].update({'build': '-'.join(sauceParameters['sauce:options'].get('tags'))})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print("You are using the US data center")
    driver = webdriver.Remote(
        # command_executor='https://sso-discover-blane:939627a8-6f4d-426e-bc5a-7d3853e6981c@ondemand.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

elif region == 'EU':
    print ("You are using the EU data center")
    driver = webdriver.Remote(
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-east-1.saucelabs.com:443/wd/hub',
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
#__________________________________________________________________
# driver.get('https://staging-one.newrelic.com')
# # interact = driver.find_element_by_css_selector("[data-selenium='addToCartButton']")
# # interact.click()
# # driver.get('http://www.bhphotovideo.com/find/cart.jsp')
# #
# # sleep(05)
# # interact = driver.find_element_by_css_selector("[data-selenium='qtyInput']").clear()
# # interact = driver.find_element_by_css_selector("[data-selenium='qtyInput']").send_keys('3')
#
#
print (driver.capabilities)

# testURL = 'https://cgi-lib.berkeley.edu/ex/fup.html'
# testURL = 'http://localhost:8000'
# testURL = 'https://localhost:8000'
testURL = 'https://6451889658.encompasstpoconnect.com/#/content/home_336257'
# testURL = 'https://media.raven.news/'
# testURL = "https://www.filebin.net"
# testURL = 'https://saucelabs.com'

#
#


driver.execute_script('sauce:job-name=Testing ' + driver.capabilities['browserName'] + ' ' + driver.capabilities['browserVersion'] + ' for ' + testURL +' ')
# driver.execute_script('sauce:throttleCPU', {
#     "rate": 4
# })



driver.get(testURL)
#
# driver.execute_script("sauce:intercept", {
#     "url": "https://saucelabs.com/",
#         "response": {
#             "status": 400,
#             "headers": {
#                 "x-custom-header": "foobar"
#             },
#             "body": [{
#                 "title": "Hello",
#                 "order": 1,
#                 "completed": False,
#                 "url": "https://google.com"
#             }]
#         }
#     })
# driver.get("https://saucelabs.com")
#
# driver.execute_script("sauce:intercept", {
#     "url": "https://saucelabs.com/*",
#     "error": "Failed"})
# sleep(5)
# driver.get("https://saucelabs.com/pricing")
# sleep(2)
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://saucelabs.com/",
# #     "redirect": "https://google.com"
# # })
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://saucelabs.com/",
# #     "redirect": "https://google.com"
# # })
# # sleep(2)
# driver.execute_script("sauce:intercept", {
#     "url": "*saucelabs*",
#     "error": "Failed"})
#
# driver.get("https://docs.saucelabs.com/insights/debug/#sauceintercept--redirect")
# sleep(2)

# driver.execute_script("sauce:intercept", {
#     "url": "https://*media.raven.news/",
#     "error": "Failed"})
# sleep(5)
# driver.get("https://media.raven.news")
# sleep(2)
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://saucelabs.com/",
# #     "redirect": "https://google.com"
# # })
# # driver.execute_script('sauce:intercept', {
# #     "url": "https://saucelabs.com/",
# #     "redirect": "https://google.com"
# # })
# # sleep(2)
# driver.execute_script("sauce:intercept", {
#     "url": "https://*media.raven.news/**",
#     "error": "Failed"})
#
# driver.get("https://media.raven.news")
# sleep(2)

# performance = driver.execute('sauce:log', {type: 'sauce:performance'});
# lighthouseScore = performance.score;
# driver.execute_script("sauce:break")

# #filebin.net testing
# driver.get("https://www.filebin.net")
#
try:
    print (colored("looking for input type '[ng-submit='vm.loadIdpLogin()']'", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-submit='vm.loadIdpLogin()']")))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "react-fine-uploader-file-input")))
    print (colored("found [ng-submit='vm.loadIdpLogin()']", 'green'))

    interact = driver.find_element_by_css_selector("[ng-submit='vm.loadIdpLogin()']")
    # interact
    interact.click()
    # JavascriptExecutor driver = (JavascriptExecutor)getDriver();
    # driver.execute_script("arguments[0].click();", interact);
    # driver.execute_script("sauce:job-result={}".format(sauce_result))
    # interact.send_keys('/Users/terranceloughry/Desktop/possumSmall.jpeg')
    print (colored("clicked [ng-submit='vm.loadIdpLogin()']", 'green'))
    # print (colored(driver.contexts, 'blue'))
    seq = driver.find_elements_by_tag_name('iframe')

    print("No of frames present in the web page are: ", len(seq))
    for index in range(len(seq)):

        # driver.switch_to_default_content()

        iframe = driver.find_elements_by_tag_name('iframe')[index]

        driver.switch_to.frame(iframe)
    interact = driver.find_element_by_xpath("//*[@id='userId']")
    # interact
    interact.click()
    interact.clear()
    interact.send_keys("tpouser@pnmac.com")

    interact = driver.find_element_by_xpath("//*[@id='password']")
    # interact
    interact.click()
    interact.clear()
    interact.send_keys("Pnmac$5678")
    interact.submit()
except:
    print (colored("Can not find [ng-submit='vm.loadIdpLogin()']", 'red'))


try:
    print (colored("looking for input type './/input[@id='userId']'", 'green'))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'userId')))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    #     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
# path('//input[@id=\"userID\"')
    seq = driver.find_elements_by_tag_name('iframe')

    print("No of frames present in the web page are: ", len(seq))
    for index in range(len(seq)):

        # driver.switch_to_default_content()

        iframe = driver.find_elements_by_tag_name('iframe')[index]

        driver.switch_to.frame(iframe)
    print (colored("found //*input[@id='userId']", 'green'))

    interact = driver.find_element_by_xpath("//*[@id='userId']")
    # interact
    interact.click()
    interact.clear()
    interact.send_keys("tpouser@pnmac.com")

    interact = driver.find_element_by_xpath("//*[@id='password']")
    # interact
    interact.click()
    interact.clear()
    interact.send_keys("Pnmac$5678")
    interact.submit()

    # JavascriptExecutor driver = (JavascriptExecutor)getDriver();
    # driver.execute_script("arguments[0].click();", interact);
    # driver.execute_script("sauce:job-result={}".format(sauce_result))
    # interact.send_keys('/Users/terranceloughry/Desktop/possumSmall.jpeg')
    print (colored("clicked .//input[@id='userId']", 'green'))
    # print (colored(driver.contexts, 'blue'))
except:
    print (colored("Can not find .//input[@id='userId']", 'red'))
    # source = driver.page_source
    # print(colored(source, 'red'))
    seq = driver.find_elements_by_tag_name('iframe')

    print("No of frames present in the web page are: ", len(seq))
    for index in range(len(seq)):

        # driver.switch_to_default_content()

        iframe = driver.find_elements_by_tag_name('iframe')[index]

        driver.switch_to.frame(iframe)
        source = driver.page_source
        print(colored(source, 'red'))
# try:
#     print (colored("looking for input type 'submit'", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "upfile")))
#     # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "react-fine-uploader-submit-input")))
#     print (colored("found input type 'submit'", 'green'))
#
#     interact = driver.find_element_by_css_selector("[type='submit']")
#     # interact
#     interact.click()
#     # JavascriptExecutor driver = (JavascriptExecutor)getDriver();
#     # driver.execute_script("arguments[0].click();", interact);
#     # driver.execute_script("sauce:job-result={}".format(sauce_result))
#
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find input type 'submit'", 'red'))

sleep(10)
# driver.execute_script("sauce:job-result={}".format('passed'))
# driver.execute_script("sauce:job-result={}".format('failed'))

# def test_speed_index(self, driver):
# self.setUpClass(driver)
# metrics = ["load", "speedIndex", "pageWeight", "pageWeightEncoded", "timeToFirstByte",
#            "timeToFirstInteractive", "firstContentfulPaint", "perceptualSpeedIndex", "domContentLoaded"]
# performance = driver.execute_script("sauce:log", {"type": "sauce:performance"})
# print (metrics)
# for metric in metrics:
#     assert performance["speedIndex"] < 1000


# try:
#     print (colored("looking for Message", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "message")))
# #
# #
# #     interact = driver.find_element_by_id("box1")
# #     interact.click()
# #     print ("placed X")
# #     interact = driver.find_element_by_id("box2")
# #     interact.click()
# #     print ("placed O")
# #     interact = driver.find_element_by_id("box3")
# #     interact.click()
# #     print ("placed X")
# #     interact = driver.find_element_by_id("box5")
# #     interact.click()
# #     print ("placed O")
# #     interact = driver.find_element_by_id("box6")
# #     interact.click()
# #     print ("placed X")
# #     interact = driver.find_element_by_id("box4")
# #     interact.click()
# #     print ("placed O")
# #     interact = driver.find_element_by_id("box8")
# #     interact.click()
# #     print ("placed X")
# #     interact = driver.find_element_by_id("box9")
# #     interact.click()
# #     print ("placed O")
# #     interact = driver.find_element_by_id("box7")
# #     interact.click()
# #     print ("placed X")
# #     sleep(5)
# #     interact = driver.find_element_by_link_text("Emergency Bees")
# #     interact.click()
# #     driver.execute_script('sauce:context=Emergency Bees')
# #     sleep(15)
#     driver.execute_script("sauce:job-result={}".format('passed'))
# #     # print (driver.current_url)
# except:
#     print (colored("Can not find message", 'red'))
#     driver.execute_script("sauce:job-result={}".format('failed'))
#
#     # print (driver.current_url)
#
#
#
# driver.execute_script('sauce:job-info={"public":"share"}')

# driver.execute_script("sauce:job-result={}".format('passed'))

# driver.current_url

# driver.get('https://google.com')
# driver.get('https://orca-dcc-dev2.wh-engmnt.dev.watson-health.ibm.com/?qrid=1773c72f145-678e71cf-8df6-4898-98de-e08e6832b165')

# driver.key_down(Keys.COMMAND)
# ActionChains(driver).key_down(Keys.COMMAND).key_down(Keys.ALT).send_keys('j').perform()
# driver.key_down(Keys.COMMAND).key_down(Keys.OPTION).send_keys("j").key_up(Keys.COMMAND).key_up(Keys.OPTION).build().perform();
#
# sleep(05)
#
#
# # Setup for finding an element and sending keystrokes
# #__________________________________________________________________
# # interact = driver.find_element_by_name('figure')
# interact = driver.find_element_by_css_selector("input[name='login[email]']")
# interact.click()
# interact.send_keys("infrauiqaautomation1@gmail.com")
# # interact.submit()
#
# interact = driver.find_element_by_css_selector("input[type='password']")
# interact.click()
# interact.send_keys("password123")
# driver.set_location(49, 123, 10)
# print sauceParameters
# driver.get('https://connect-web.staging.dataservices.theice.com')
# driver.get('https://master.dx.traegergrills.com/recipes/smoked-chili-con-carne')
#
# datetime_object = datetime.datetime.now()
# print(datetime_object)

# interact = driver.find_element_by_id("i0116")
# try:
#     print (colored("looking for jsx-1421156901.cookie_notification.row.no-gutters.position-fixed.p-3.w-100", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "jsx-1421156901.cookie_notification.row.no-gutters.position-fixed.p-3.w-100")))
#
#
#     interact = driver.find_element_by_css_selector("btn.btn-outline-primary.mx-auto")
#     # interact.click()
#     print (colored("found button.btn.btn-outline-primary.mx-auto", 'green'))
#     interact.click()
#     print (colored("clicked button.btn.btn-outline-primary.mx-auto", 'green'))
# except:
#     print (colored("Can not find button.btn.btn-outline-primary.mx-auto", 'red'))

# try:
#     print (colored("looking for button.btn.btn-outline-primary.mx-auto", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mx-auto")))
#     interact = driver.find_element_by_css_selector("button.btn.btn-outline-primary.mx-auto")
#     interact.click()
#     print (colored("found button.btn.btn-outline-primary.mx-auto", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find button.btn.btn-outline-primary.mx-auto", 'red'))
#
# try:
#     print (colored("looking for Print", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.jsx-898850507.secondary-button")))
#     print (colored("found Print", 'green'))
#     print(driver.current_window_handle)
#     interact = driver.find_element_by_css_selector("button.jsx-898850507.secondary-button")
#     print (colored("found Print", 'green'))
#     ids = driver.find_elements_by_xpath('//*[@id]')
#     # print (ids)
#     # for ii in ids:
#     #print ii.tag_name
#         # print (ii.get_attribute('id'))
#     print(driver.current_window_handle + "   yo")
#
#
#     interact.click()
#
#     print (windowHandles = driver.get_window_handles() + "this")
#     # if windowHandles.is_empty()
#     #     driver.switchTo().window((String) windowHandles.toArray()[windowHandles.size() - 1]);
#     #
#     # # //Now work with the dialog as with an ordinary page:
#     # driver.find_element(By.className("cancel")).click();
#
#
#     print("here")
#
#     # javaScript = "document.getElementsByTagName(\"button\")[2].setAttribute(\"id\", \"printButton\")"
#     # driver.execute_script(javaScript)
#     # window1 = driver.window_handles[1]
#     # driver.switch_to.window(window1)
#     print(driver.current_window_handle)
#     print (colored("clicked button.jsx-898850507.secondary-button", 'green'))
#
#     print (colored("found button.jsx-898850507.secondary-button", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find button.jsx-898850507.secondary-button", 'red'))
#     interact.click()
#
#
# sleep(5)
# driver.window_handles
# print(driver.current_window_handle)
# print(driver.window_handles)
#
# # var el = document.getElementById('printButton'); setTimeout(function() { el.click(); }, 100);
#
# # jsx-898850507 button-container
# # interact = driver.find_element_by_id("i0118")
# # try:
# #     print (colored("looking for i0118", 'green'))
# #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "i0118")))
# #     interact = driver.find_element_by_id("i0118")
# #     interact.click()
# #     print (colored("found i0118", 'green'))
# #     # print (colored(driver.contexts, 'blue'))
# # except:
# #     print (colored("Can not find i0118", 'red'))
# #
# # interact.click()
# #
# # interact.clear()
# #
# # interact.send_keys("q3M97RYtf2R1VzAyb5br24UWZUpss8")
# #
# # interact = driver.find_element_by_id("idSIButton9")
# #
# # interact.click()
# #
# # try:
# #     print (colored("looking for Help", 'green'))
# #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Help")))
# #     interact = driver.find_element_by_css_selector("div:nth-of-type(1) > .menu-dropdown-title > img")
# #     interact.click()
# #     print (colored("found Help", 'green'))
# #     # print (colored(driver.contexts, 'blue'))
# # except:
# #     print (colored("Can not find Help", 'red'))
# #
# # try:
# #     print (colored("looking for Customer journey testing", 'green'))
# #     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu-dropdown-trigger')))
# #     interact = driver.find_element_by_class_name("menu-dropdown-trigger")
# #     interact.click()
# #     print (colored("found Customer journey testing", 'green'))
# #     # print (colored(driver.contexts, 'blue'))
# # except:
# #     print (colored("Can not find Customer journey testing", 'red'))
#
#
#
# try:
#     print (colored("looking for Order Fulfillment", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Order Fulfillment")))
#     interact = driver.find_element_by_link_text("Order Fulfillment")
#     interact.click()
#     print (colored("found Order Fulfillment", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find Order Fulfillment", 'red'))
#
# try:
#     print (colored("looking for OWhat is this link", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "What is this?")))
#     interact = driver.find_element_by_link_text("What is this?")
#     interact.click()
#     print (colored("found OWhat is this link", 'green'))
#     # print (colored(driver.contexts, 'blue'))
# except:
#     print (colored("Can not find OWhat is this link", 'red'))


# interact = driver.find_elements_by_xpath('//*[@id=\"pageLogin\"]/div/h1')
# driver.navigate().refresh()

# javaScript = "document.find_element_by_class_name('.apple-icon-button'[0]).click()"
# driver.execute_script(javaScript)
# driver.execute_script("arguments[0].click()", driver.find_element_by_css_selector('.apple-icon-button'));

# interact = driver.find_element_by_css_selector(".privacy")
# interact = driver.find_element_by_css_selector(".apple-icon-button")
# sleep(15)

# interact.click()
# interact.click()
# sleep(15)

# driver.execute_script("sauce:intercept", {
#    "url": "https://www.google.com",
#       "response": {
#           "headers": {
#               "Authorization": "Basic YWRtaW46aFY2YzJxPmU="
#           },
#           "body": [{
#              "url": "http://10.53.125.8/web?q=shoes&p2=%5Ezs%5Eyyyyyy%5Ettab02%5Eus&st=hp&tpr=sbt"
#           }]
#       }
#  })
#
#
#
# driver.execute_script('sauce:intercept', {
#     "url": "https://www.google.com",
#     "redirect": "https://saucelabs.com"
# })
# driver.get('https://www.ancestry.com/account/signin?returnUrl=https%3A%2F%2Fwww.ancestry.com')
# driver.get('https://google.com')
# driver.get()

# driver.execute_script('sauce:intercept', {
#     "url": "https://google.com",
#     "redirect": "https://saucelabs.com"
# })

# driver.execute_script('sauce:intercept', {
#     "url": "https://google.com/*",
#     # "error": "Failed"
#     "response": {
#         "status": 500,
#             "body": [{
#                 "title": "Hello, the page has a 500 error",
#             }],
#     }
# })
#
# interact = driver.find_element_by_name('q')
# interact.click()
#
# interact.clear()
# interact.send_keys("local time")
#
# interact.submit()
#
#
#
# try:
#     print (colored("looking for Timezone info", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "Uo8X3b")))
#     timeElement = driver.find_elements_by_class_name('KfQeJ')
#
#     print (colored("found element", 'green'))
#     # print (colored(interact.get_text, 'blue'))
#     for x in range (len(timeElement)):
#         print(colored(timeElement[x].text, 'blue'))
#         print(type(timeElement[x]))
#     print(timeElement)
#     print(type(timeElement))
#     print(len(timeElement))
# except:
#     print (colored("Can not find find_element_by_name('Uo8X3b')", 'red'))# wait = WebDriverWait(driver, 20)

# try:
#     print (colored("looking for cd_login_button", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "cd_login_button")))
#     cd_login_button = driver.find_element_by_id('cd_login_button')
#     print (colored("found element", 'green'))
#
#
#
# except:
#     print (colored("Can not find find_element_by_ID('cd_login_button')", 'red'))# wait = WebDriverWait(driver, 20)
#
#
# try:
#     print (colored("looking for email", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "email")))
#
#     print (colored("found element", 'green'))
#     interact = driver.find_element_by_id('email')
#     interact.click()
#     interact.send_keys("test@email.com")
#
#
#
# except:
#     print (colored("Can not find find_element_by_ID('cd_login_button')", 'red'))# wait
#
#
# try:
#     print (colored("looking for password", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "password")))
#
#     print (colored("found element", 'green'))
#     interact = driver.find_element_by_id('password')
#     interact.click()
#     interact.send_keys("test_password")
#     cd_login_button.click()
#
#
# except:
#     print (colored("Can not find find_element_by_ID('cd_login_button')", 'red'))# wa
# driver.implicitly_wait(5000)
# sleep(5)
# driver.switch_to.frame("signInFrame");
# sleep(5)


# print ("things")
# #
# metrics = ["load", "speedIndex", "pageWeight", "pageWeightEncoded", "timeToFirstByte",
#            "timeToFirstInteractive", "firstContentfulPaint", "perceptualSpeedIndex", "domContentLoaded", "result"]
# performance = driver.execute_script("sauce:log", {"type": "sauce:performance"})
# performance

# if(performance["load"] < 10000)
# for metric in metrics:
# #     print ("hello " + metric)
# #     print (performance["speedIndex"])
# #     print (performance["result"])
#     # print(performance)
# #     print ("hello")
#     if(2 == 2):
#       assert performance["load"] < 5000, "it did the thing"
#       driver.execute_script("sauce:job-result={}".format('passsed'))
#     else:
#       print (performance)
#       driver.execute_script("sauce:job-result={}".format('failed'))
#       print ("made it")
#       assert performance["load"] < 5, "it did not do the thing"
# performance["load"]
# if(2 == 2):
#   driver.execute_script("sauce:job-result={}".format('passsed'))
#   assert performance["load"] > 5000, "it did the thing"
#
# else:
#   print (performance)
#   driver.execute_script("sauce:job-result={}".format('failed'))
#   print ("made it")
#   assert performance["load"] < 5, "it did not do the thing"
#
#
#
# # assert performance["load"] > 100000
# print(performance["load"])
# print (metrics)

# print(performance["result"])


# performance = driver.execute_script("sauce:performance", {
#                                   "name": "name this", "metrics": ["firstInteractive"]})
# print(performance["result"])
# print (performance)
# if(performance["result"] != "pass"):
#   print (performance["details"])
#   print (performance["actual "])
#   print (performance["firstInteractive"])
#   assert performance["details"]["firstInteractive"]["actual "] < 5000
# else:
#   print (performance)
#   print ("made it")
#   assert performance["result"] == "fail", "this failed"
# javaScript = "driver.find_element_by_id('login-button')[0].click()"
# driver.execute_script(javaScript)
# driver.execute_script("arguments[0].click()", driver.find_element_by_id('login-button'));
# login = driver.find_element_by_id("login-button")
# driver.execute_script("arguments[0].click();", login)
# # interact.click()
#
# element = WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.ID,"signInName")))
#
#

#
# interact.send_keys("email address")


#
# ids = driver.find_elements_by_xpath('//*[@id]')
# for ii in ids:
#     print "name: ",  ii.get_attribute('name')
#     print "class: ", ii.get_attribute('class')
#     print "id: ", ii.get_attribute('id')
#
# # interact = driver.find_element_by_css_selector("input[id='login_submit']")
# # interact.submit()
# #
# # sleep(05)
# driver.get('https://www.cbtnuggets.com/login')
# print(driver.session_id)
# # driver.get('https://gauntface.github.io/simple-push-demo/')
# # driver.get('https://www.qa.apartmentguide.com')
# # popup = driver.switch_to_alert
#
# # sleep(90)
# # Setup for finding an element and clicking it
# #__________________________________________________________________
# # interactive tabbed-standard
#
#
# # interact = driver.find_element_by_css_selector("a[href='/support']").click()
# # interact = driver.find_element_by_css_selector("a[href='https://wiki.saucelabs.com/']").click()
#
# sleep(15)
# # iframe = driver.switch_to.frame(find_element_by_class('interactive'))
# # iframe = driver.switch_to.frame(find_element_by_class_name('interactive'))
# # interact = driver.find_element_by_link_text("Documentation").click()
# # interact = driver.find_element_by_id("i_am_a_textbox").send_keys("Sauce")
#
# # interact = driver.find_element_by_name("q")
#
# # try:
# #     element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((driver.find_element_by_id("email"))))
# # finally:
# #     driver.quit()
# # wait = WebDriverWait(driver, 10)
# try:
#     # Wait as long as required, or maximum of 5 sec for element to appear
#     # If successful, retrieves the element
#     interact = WebDriverWait(driver,60).until(
#          EC.presence_of_element_located((By.ID, "email")))
#
#     # Type "selenium"
#     # element.send_keys("selenium")
#
#     #Type Enter
#     # element.send_keys(Keys.ENTER)
#
# # except TimeoutException:
#     print("Failed to load search bar at www.google.com")
# finally:
#     print("Failed to load search bar at www.google.com!!!!!!")
#     print(driver.session_id)
# # element = wait.until(EC.presence_of_element_located((driver.find_element_by_id("email"))))
# # interact = driver.find_element_by_id("email")
# # interact = driver.find_element_by_class_name("mdl-switch__ripple-container ").click()
# interact.click()
# # interact.send_keys('atesting+444bop@cbtnuggets.com')
# interact.send_keys('email@email.email')
# interact = driver.find_element_by_id("password")
# interact.click()
# interact.send_keys('password123')
# # interact.send_keys('XJstgWsu3dwchRyDr')
# interact.submit()

# sleep(15)
# Setup for using random Python commands
#__________________________________________________________________
# driver.save_screenshot('screenshot.png')
# sleep(50)
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
