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
    #     # 'maxDuration': 1800,
    #     # 'idleTimeout': 1000,
    #     # 'commandTimeout': 600,
    #     # 'videoUploadOnPass':False,
    #     # 'extendedDebugging':'true',
    # "prerun":"https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat",

    # },
    # 'count': 1,
    'platformName': 'windows 10',
    # 'platformName': 'macOS 10.15',
    # 'browserName': 'firefox',
    # 'browserName': 'MicrosoftEdge',
    'browserName': 'internet explorer',
    # 'browserName': 'chrome',
    # 'browserName': 'safari',
    # 'version': '13',
    # 'browserVersion': 'dev',
    'browserVersion': 'latest',
    # 'seleniumVersion': '3.141.59',
    # 'maxDuration': 1800,
    # 'commandTimeout': 300,
    # 'idleTimeout': 90,
    # 'build': 'Trying to break it',
    # 'tunnelIdentifier': 'tj',
    # 'public':'private',
    'sauce:options': {
        'name':'Test One',
        # 'tags':'13128733',
        # 'extendedDebugging':'true',
        'build':'CAT XPath tests',
        'screenResolution':'1600x1200',

        # 'avoidProxy': 'true',
        # 'capturePerformance': 'true',
        # 'seleniumVersion': '3.141.59',
        # 'public':'private',
        # 'name': 'https://dev.testinghub.autodesk.com/ test of drop down menu',
        # 'extendedDebugging':'true',
        # "timeZone": "New_York",
        # 'tunnelIdentifier': 'newtj1'
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
    #     'w3c': True,    # Required for a W3C Chrome test
    #     # 'mobileEmulation':{'deviceName':'iPhone X'},
    #     # 'prefs': {
    #     #     'profile': {
    #     #         'password_manager_enabled': False
    #     #         },
    #     #         'credentials_enable_service': False,
    #     #     },
    #     # 'args': ['--auto-open-devtools-for-tabs'],
    # },
    # 'moz:firefoxOptions':{
    #     "log": {"level": "trace"},
    #     'geckodriverVersion':'0.27.0',
    # },
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
        # command_executor='https://tj.invitationtest3:16e9429a-cc5d-4c36-8caf-087a1e4e899a@ondemand.saucelabs.com:443/wd/hub',
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

# testURL = 'localhost:8000'
testURL = 'https://qa1shop.cat.com/wcs-static/getMyCookie.html'
# testURL = 'https://localhost:8000'
# testURL = 'trytjloughry.com:8000'
# testURL = 'http://trytjloughry.com'
# testURL = 'https://trytjloughry.com'

#
#
driver.get(testURL)

driver.execute_script('sauce:job-name=Testing ' + driver.capabilities['browserName'] + ' ' + driver.capabilities['browserVersion'] + ' for ' + testURL +' To Test XPath')

# driver.execute_script("sauce:job-result={}".format('passed'))
# driver.execute_script("sauce:job-result={}".format('failed'))


try:
    print (colored("looking for Alert Text", 'green'))
    WebDriverWait(driver, 30).until(EC.alert_is_present())
    print ('found Alert Text')

    alert = driver.switch_to.alert

    # alert.getText()
    alert.send_keys('yellow')
    alert.accept()
    alert.accept()
    # sleep(5)

except:
    print (colored("Can not find Alert Text", 'red'))


try:
    print (colored("looking for //a[contains(text(),'Go to CI Retail')]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Go to CI Retail')]")))
    print ("found //a[contains(text(),'Go to CI Retail')]")

    interact = driver.find_element_by_xpath("//a[contains(text(),'Go to CI Retail')]")
    interact.click()

except:
    print (colored("Can not find //a[contains(text(),'Go to CI Retail')]", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]")))
    print ("found //li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]")

    interact = driver.find_element_by_xpath("//li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]")

    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]", 'red'))
    sleep(5)

# try:
#     print (colored("looking for //li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]", 'green'))
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]")))
#     print ("found //li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]")
#
#     interact = driver.find_element_by_xpath("//li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]")
#     driver.execute_script("arguments[0].click();", interact)
#
# except:
#     print (colored("Can not find //li[@class='user-icon']//a[contains(@id,'signInQuickLink')]/span[2]", 'red'))
#
#     # print (driver.current_url)
#
try:
    print (colored("looking for //div[@class='panel signInForm']//input[@name='logonId']", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='panel signInForm']//input[@name='logonId']")))
    print ("found //div[@class='panel signInForm']//input[@name='logonId']")

    interact = driver.find_element_by_xpath("//div[@class='panel signInForm']//input[@name='logonId']")
    print ("clearing")
    # interact.clear()
    print ('sending keys')
    interact.send_keys("e300_bcp_ia_auto")
    interact = driver.find_element_by_xpath("//input[@name='logonPassword']")
    print ("clearing")
    # interact.clear()
    print ('sending keys')
    interact.send_keys("Test.123")
    # interact.submit()
    interact = driver.find_element_by_xpath("//a[contains(@id,'GlobalLogin') and contains(@class,'primary') and @role='button']")
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='panel signInForm']//input[@name='logonId']", 'red'))


try:
    print (colored("looking for //select[@id='dealerStore']/option", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select[@id='dealerStore']/option")))
    print ("found //select[@id='dealerStore']/option")

    interact = driver.find_element_by_xpath("//select[@id='dealerStore']/option")
    interact

except:
    print (colored("Can not find //select[@id='dealerStore']/option", 'red'))

try:
    print (colored("looking for //div[@id='continueDiv']/a", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@id='continueDiv']/a")))
    print ("found //div[@id='continueDiv']/a")

    interact = driver.find_element_by_xpath("//div[@id='continueDiv']/a")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@id='continueDiv']/a", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))


try:
    print (colored("looking for //a[contains(@id,'minishopcar')]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@id,'minishopcar')]")))
    print ("found //a[contains(@id,'minishopcar')]")

    interact = driver.find_element_by_xpath("//a[contains(@id,'minishopcar')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //a[contains(@id,'minishopcar')]", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))


try:
    print (colored("looking for //input[contains(@id,'qty') and @type='number']", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'qty') and @type='number']")))
    print ("found //input[contains(@id,'qty') and @type='number']")

    interact = driver.find_element_by_xpath("//input[contains(@id,'qty') and @type='number']")
    interact


except:
    print (colored("Can not find //input[contains(@id,'qty') and @type='number']", 'red'))

try:
    print (colored("looking for //span[contains(@class,'shopcart__chevron')]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'shopcart__chevron')]")))
    print ("found //span[contains(@class,'shopcart__chevron')]")

    interact = driver.find_element_by_xpath("//span[contains(@class,'shopcart__chevron')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[contains(@class,'shopcart__chevron')]", 'red'))

try:
    print (colored("looking for //a[contains(@id,'Logo')][1]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@id,'Logo')][1]")))
    print ("found //a[contains(@id,'Logo')][1]")

    interact = driver.find_element_by_xpath("//a[contains(@id,'Logo')][1]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //a[contains(@id,'Logo')][1]", 'red'))


try:
    print (colored("looking for //div[@class='top-left-nav']//a[contains(@id,'departmentLink_') and contains(@href,'/machines')][1]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='top-left-nav']//a[contains(@id,'departmentLink_') and contains(@href,'/machines')][1]")))
    print ("found //div[@class='top-left-nav']//a[contains(@id,'departmentLink_') and contains(@href,'/machines')][1]")

    interact = driver.find_element_by_xpath("//div[@class='top-left-nav']//a[contains(@id,'departmentLink_') and contains(@href,'/machines')][1]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='top-left-nav']//a[contains(@id,'departmentLink_') and contains(@href,'/machines')][1]", 'red'))

try:
    print (colored("looking for //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Mini Excavators')]", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Mini Excavators')]")))
    print ("found //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Mini Excavators')]")

    interact = driver.find_element_by_xpath("//div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Mini Excavators')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Mini Excavators')]", 'red'))


try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //span[text()='Your opinion matters!']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your opinion matters!']")))
    print ("found //span[text()='Your opinion matters!']")

    interact = driver.find_element_by_xpath("//span[text()='Your opinion matters!']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[text()='Your opinion matters!']", 'red'))

try:
    print (colored("looking for //div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a")))
    print ("found //div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a")

    interact = driver.find_element_by_xpath("//div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a", 'red'))

try:
    print (colored("looking for //span[text()='Your opinion matters!']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your opinion matters!']")))
    print ("found //span[text()='Your opinion matters!']")

    interact = driver.find_element_by_xpath("//span[text()='Your opinion matters!']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[text()='Your opinion matters!']", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]")))
    print ("found //div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]")

    interact = driver.find_element_by_xpath("//div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //*[contains(@id,'priceBefore') and contains(@style,'none')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'priceBefore') and contains(@style,'none')]")))
    print ("found //*[contains(@id,'priceBefore') and contains(@style,'none')]")

    interact = driver.find_element_by_xpath("//*[contains(@id,'priceBefore') and contains(@style,'none')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //*[contains(@id,'priceBefore') and contains(@style,'none')]", 'red'))

try:
    print (colored("looking for //img[@class='product_main_image']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='product_main_image']")))
    print ("found //img[@class='product_main_image']")

    interact = driver.find_element_by_xpath("//img[@class='product_main_image']")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //img[@class='product_main_image']", 'red'))

try:
    print (colored("looking for //div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]")))
    print ("found //div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]")

    interact = driver.find_element_by_xpath("//div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]", 'red'))


try:
    print (colored("looking for //span[@class='checkmark']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='checkmark']")))
    print ("found //span[@class='checkmark']")

    interact = driver.find_element_by_xpath("//span[@class='checkmark']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[@class='checkmark']", 'red'))


try:
    print (colored("looking for //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")))
    print ("found //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")

    interact = driver.find_element_by_xpath("//div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]", 'red'))

try:
    print (colored("looking for //div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']")))
    print ("found //div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']")

    interact = driver.find_element_by_xpath("//div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']", 'red'))

try:
    print (colored("looking for //div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']")))
    print ("found //div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']")

    interact = driver.find_element_by_xpath("//div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for (//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]")))
    print ("found (//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]")

    interact = driver.find_element_by_xpath("(//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find (//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]", 'red'))

try:
    print (colored("looking for //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]")))
    print ("found //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]")

    interact = driver.find_element_by_xpath("//div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //span[text()='Your opinion matters!']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your opinion matters!']")))
    print ("found //span[text()='Your opinion matters!']")

    interact = driver.find_element_by_xpath("//span[text()='Your opinion matters!']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[text()='Your opinion matters!']", 'red'))

try:
    print (colored("looking for //div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a")))
    print ("found //div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a")

    interact = driver.find_element_by_xpath("//div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@class,'flp__topBanner_textwrapper')]/div[@class='flp__topBanner_button']/a", 'red'))


try:
    print (colored("looking for //span[text()='Your opinion matters!']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your opinion matters!']")))
    print ("found //span[text()='Your opinion matters!']")

    interact = driver.find_element_by_xpath("//span[text()='Your opinion matters!']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[text()='Your opinion matters!']", 'red'))


try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]")))
    print ("found //div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]")

    interact = driver.find_element_by_xpath("//div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='product_info productgridtitle']//a[text()[normalize-space()='300.9D']]", 'red'))


try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //*[contains(@id,'priceBefore') and contains(@style,'none')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'priceBefore') and contains(@style,'none')]")))
    print ("found //*[contains(@id,'priceBefore') and contains(@style,'none')]")

    interact = driver.find_element_by_xpath("//*[contains(@id,'priceBefore') and contains(@style,'none')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //*[contains(@id,'priceBefore') and contains(@style,'none')]", 'red'))

try:
    print (colored("looking for //img[@class='product_main_image']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='product_main_image']")))
    print ("found //img[@class='product_main_image']")

    interact = driver.find_element_by_xpath("//img[@class='product_main_image']")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //img[@class='product_main_image']", 'red'))

try:
    print (colored("looking for //div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]")))
    print ("found //div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]")

    interact = driver.find_element_by_xpath("//div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'monthly_price_display') and contains(@style,'block')]//span[contains(@id,'listPrice')]", 'red'))


try:
    print (colored("looking for //span[@class='checkmark']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='checkmark']")))
    print ("found //span[@class='checkmark']")

    interact = driver.find_element_by_xpath("//span[@class='checkmark']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[@class='checkmark']", 'red'))

try:
    print (colored("looking for //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")))
    print ("found //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")

    interact = driver.find_element_by_xpath("//div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]", 'red'))


try:
    print (colored("looking for //div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']")))
    print ("found //div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']")

    interact = driver.find_element_by_xpath("//div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='col-md-8 col-sm-8 col-xs-8 pdp__addToCartPopup-headerText']", 'red'))


try:
    print (colored("looking for //div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']")))
    print ("found //div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']")

    interact = driver.find_element_by_xpath("//div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='col-md-7 col-sm-7 col-xs-12 pdp__addToCartPopup-continueShoppping']//a[@class='standard-link']", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))


try:
    print (colored("looking for (//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]")))
    print ("found (//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]")

    interact = driver.find_element_by_xpath("(//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find (//div[@class='top-left-nav']//a[contains(@id,'departmentLink')])[1]", 'red'))

try:
    print (colored("looking for //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]")))
    print ("found //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]")

    interact = driver.find_element_by_xpath("//div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@class='top-left-nav']//a[contains(@id,'categoryLink')][contains(text(),'Grapple')]", 'red'))


try:
    print (colored("looking for //span[text()='Your opinion matters!']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your opinion matters!']")))
    print ("found //span[text()='Your opinion matters!']")

    interact = driver.find_element_by_xpath("//span[text()='Your opinion matters!']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[text()='Your opinion matters!']", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //div[contains(@id,'price_display') and contains(@style,'block')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'price_display') and contains(@style,'block')]")))
    print ("found //div[contains(@id,'price_display') and contains(@style,'block')]")

    interact = driver.find_element_by_xpath("//div[contains(@id,'price_display') and contains(@style,'block')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'price_display') and contains(@style,'block')]", 'red'))


try:
    print (colored("looking for //div[contains(@id,'price_display') and contains(@style,'block')]//div[contains(@id, 'Discount')]//span[@class='price']/ancestor::div[@class='product']//img", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'price_display') and contains(@style,'block')]//div[contains(@id, 'Discount')]//span[@class='price']/ancestor::div[@class='product']//img")))
    print ("found //div[contains(@id,'price_display') and contains(@style,'block')]//div[contains(@id, 'Discount')]//span[@class='price']/ancestor::div[@class='product']//img")

    interact = driver.find_element_by_xpath("//div[contains(@id,'price_display') and contains(@style,'block')]//div[contains(@id, 'Discount')]//span[@class='price']/ancestor::div[@class='product']//img")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'price_display') and contains(@style,'block')]//div[contains(@id, 'Discount')]//span[@class='price']/ancestor::div[@class='product']//img", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //*[contains(@id,'priceBefore') and contains(@style,'none')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'priceBefore') and contains(@style,'none')]")))
    print ("found //*[contains(@id,'priceBefore') and contains(@style,'none')]")

    interact = driver.find_element_by_xpath("//*[contains(@id,'priceBefore') and contains(@style,'none')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //*[contains(@id,'priceBefore') and contains(@style,'none')]", 'red'))


try:
    print (colored("looking for //img[@class='product_main_image']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='product_main_image']")))
    print ("found //img[@class='product_main_image']")

    interact = driver.find_element_by_xpath("//img[@class='product_main_image']")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //img[@class='product_main_image']", 'red'))

try:
    print (colored("looking for //span[contains(@id,'offerPrice')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@id,'offerPrice')]")))
    print ("found //span[contains(@id,'offerPrice')]")

    interact = driver.find_element_by_xpath("//span[contains(@id,'offerPrice')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //span[contains(@id,'offerPrice')]", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")))
    print ("found //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")

    interact = driver.find_element_by_xpath("//div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'shopperActionId') and @style='display: block;']//a[@id='add2CartBtn' and contains(text(),'Add equipment to reservation')]", 'red'))

try:
    print (colored("looking for //a[@id='add2CartBtn']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='add2CartBtn']")))
    print ("found //a[@id='add2CartBtn']")

    interact = driver.find_element_by_xpath("//a[@id='add2CartBtn']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //a[@id='add2CartBtn']", 'red'))

try:
    print (colored("looking for //div[@id='progress_bar' and contains(@style,'block')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='progress_bar' and contains(@style,'block')]")))
    print ("found //div[@id='progress_bar' and contains(@style,'block')]")

    interact = driver.find_element_by_xpath("//div[@id='progress_bar' and contains(@style,'block')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[@id='progress_bar' and contains(@style,'block')]", 'red'))

try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))

try:
    print (colored("looking for //div[contains(@class,'add-to-cart-popup')][not(contains(@class,'hidden'))]//a[@class='button button_primary2']", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'add-to-cart-popup')][not(contains(@class,'hidden'))]//a[@class='button button_primary2']")))
    print ("found //div[contains(@class,'add-to-cart-popup')][not(contains(@class,'hidden'))]//a[@class='button button_primary2']")

    interact = driver.find_element_by_xpath("//div[contains(@class,'add-to-cart-popup')][not(contains(@class,'hidden'))]//a[@class='button button_primary2']")
    interact
    driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@class,'add-to-cart-popup')][not(contains(@class,'hidden'))]//a[@class='button button_primary2']", 'red'))


try:
    print (colored("waiting for .readyState", 'green'))
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print ("readyState is complete")

except:
    print (colored("page never ready", 'red'))


try:
    print (colored("looking for //*[contains(@class,'cart-item__price')]", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'cart-item__price')]")))
    print ("found //*[contains(@class,'cart-item__price')]")

    interact = driver.find_element_by_xpath("//*[contains(@class,'cart-item__price')]")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //*[contains(@class,'cart-item__price')]", 'red'))


try:
    print (colored("looking for //div[contains(@id,'cart-availability-table')]//span", 'green'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'cart-availability-table')]//span")))
    print ("found //div[contains(@id,'cart-availability-table')]//span")

    interact = driver.find_element_by_xpath("//div[contains(@id,'cart-availability-table')]//span")
    interact
    # driver.execute_script("arguments[0].click();", interact)

except:
    print (colored("Can not find //div[contains(@id,'cart-availability-table')]//span", 'red'))
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
