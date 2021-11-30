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

region = 'US'


###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs Tests
###################################################################
sauceParameters = {
    'tags':['New', 'Build',],
    'name': 'Run: ' + str(datetime.datetime.now()),

    # "browserName": "chrome",


    # 'name': 'Run without search between clicks',
    'platform': 'macos 10.15',
    # 'platformName': 'windows 10',
    # 'browserName': 'MicrosoftEdge',
    # 'browserName': 'internet explorer',
    # 'browserName': 'chrome',

    'browserName': 'safari',
    # 'cleanSession': 'true',
    # 'version': '11.285',
    # 'timeZone': 'Chicago',

    'version': 'latest',
    # 'browserVersion': 'latest',

        # "prerun":"sauce-storage:disable-intranet-compatibility-mode-in-ie.bat",
            # 'prerun':{
            #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
            #     'args': ['--silent'],
            #     'timeout': 500,
            #     'background': 'false',
            # },
    # 'browserVersion':'latest',
    # 'sauce:options': {
        # 'seleniumVersion': '3.141.59',
        # },
    'extendedDebugging': 'true',
    # 'chromedriverVersion': 'beta',
    # 'capturePerformance': 'true',
    # 'screenResolution':'1280x1024',
    # 'name': 'Run: ' + getNumber(),
    # 'tunnelIdentifier':"sharedmaybe",
    # 'parentTunnel':"tj.invitationtest4"
    # 'seleniumVersion': '3.141.59',
    # 'iedriverVersion': '3.141.59',
    # 'chromedriverVersion': '2.40',
    # 'requireWindowFocus' : True,
    # 'maxDuration': 1800,
    # 'idleTimeout': 1000,
    # 'commandTimeout': 600,
    # 'videoUploadOnPass':False,
    # 'extendedDebugging':'true',
    # 'prerun':{
    #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
    #     'args': ['--silent'],
    #     'timeout': 500,
    #     'background': 'false',
    # },
    # 'chromeOptions':{
    #      # "binary": "D:\\Program Files\\Chrome 66\\chrome.exe",
    #      "args": [ '--auto-open-devtools-for-tabs' ],
    # #     # mobileEmulation':{'deviceName':'iPhone X'},
    # #     # 'prefs': {
    # #     #     'profile': {
    # #     #         'password_manager_enabled': False
    # #     #         },
    # #     #         'credentials_enable_service': False,
    # #     #     },
    # #     'args': ['test-type', 'disable-infobars'],
    # },
    # 'moz:firefoxOptions':{
    #
    #     'geckodriverVersion':'0.27.0',
    # },
    # "sauce:options":{
    #     "seleniumVersion": "3.141.0",
    #     "name": "Test using W3C protocol",
    #     "iedriverVersion": "3.150.1",
    # },
    #     "acceptSslCerts": 'false',
    #     "idleTimeout": "120",
    #     "name": "AFW - TTAB02CHR PackageTracer https://hp.myway.com/packagetracer/ttab02chr/ [ Windows 10 ] - [ Inter...",
    #     "platform": "Windows 10",
    #     "browserName": "Internet Explorer",
    #     "version": "11",
    #     "iedriverVersion": "3.150.1",
    #     "screenResolution": "1024x768",
    #     "seleniumVersion":  "3.141.0"
    }


# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

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
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        # command_executor='https://tj.invitationtest3:16e9429a-cc5d-4c36-8caf-087a1e4e899a@ondemand.saucelabs.com:443/wd/hub',
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

print (driver.capabilities)

# driver.get("https://admin-61c3464f.test.duosecurity.com/login");
# #
# # driver.switch_to_frame("signInFrame");
# #
# try:
#     element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login_emailaddress_field")))
# finally:
#     print ("element found")
#
# # interact = driver.find_elements_by_xpath('//input[@id=\"login_emailaddress_field\"')
# interact = driver.find_element_by_id("login_emailaddress_field")
# interact.click()
# interact.send_keys("test_au_unrestricted_admin@example.com");
#
#
# interact = driver.find_element_by_id("login_continue_button")
# interact.click()
# interact.click()
#
#
# element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "login_password_field")))

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
# ids = driver.find_elements_by_xpath('//*[@id]')
# for ii in ids:
#     print( colored("name: ", 'green'),  ii.get_attribute('name'))
#     print( colored("class: ", 'red'), ii.get_attribute('class'))
#     print( colored("id: ", 'blue'), ii.get_attribute('id'))

# _browser_profile = webdriver.FirefoxProfile()
# _browser_profile.set_preference("dom.webnotifications.enabled", False)
# webdriver.Firefox(firefox_profile=_browser_profile)
#
# driver.get('https://www.cbtnuggets.com/login')
# driver.get('https://gauntface.github.io/simple-push-demo/')
# driver.get('https://www.qa.apartmentguide.com')
# popup = driver.switch_to_alert
# driver.execute_script('sauce:intercept', {
#     "url": "https://saucelabs.com/",
#     "response": {
#         "statusCode": 200,
#
#
#     }
# })


# driver.execute_script('sauce:intercept', {
#     "url": "https://saucelabs*",
#     # "error": "Failed"
#     "response": {
#         "status": 500,
#             "body": [{
#                 "title": "Hello, the page has a 500 error",
#             }],
#     }
# })

# sleep(5)
#
driver.get('https://www.google.com')
# driver.get('http://the-internet.herokuapp.com/windows')




#
#
# #
try:
    print (colored("looking for search", 'green'))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'q')))
    print (colored("found tryhome", 'green'))

    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Try it']")))
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@name='quickBalance_header']")))
    # interact = driver.find_element_by_xpath("//*XCUIElementTypeButton[@name='menu_share_form']")
    # interact = driver.find_element_by_link_text("Click Here")
    # interact = driver.find_element_by_class_name("VDXfz")
    interact = driver.find_element_by_name("9")
    print(interact)
    # iframe = driver.find_elements_by_tag_name('iframe')
    # print(colored(iframe, 'blue'))
    # iframe = driver.find_elements_by_tag_name('iframe')
    print(colored(iframe, 'blue'))
    # print(colored(iframe[1], 'blue'))
    # print(colored(iframe[2], 'blue'))
    # print(colored(iframe[3], 'blue'))
    # print(colored(iframe[4], 'blue'))
    # print(colored(iframe[5], 'blue'))
    # print(colored(iframe[6], 'blue'))
    # interact = driver.find_elements_by_xpath("//iframe[@id='iframeResult']")
    # print(interact)

    # driver.switch_to().frame("5001");

    # driver.switch_to().frame("5001");
    # print (colored("found and Try It", 'green'))
    # names = driver.find_elements_by_xpath(".//*")
    # print(colored(names.get_attribute(), 'green'))
except:
    print (colored("Can not find Search", 'red'))
# sleep(5)
#


#
# driver.delete_all_cookies()
# sleep(5)
# get_title = driver.title
# print((get_title))
#
# interact = driver.find_elements_by_xpath("//*[@id='ProductSearchOnBoardingModalModal']")
#
# interact = driver.find_element_by_css_selector("#appModalModal")
# interact = driver.find_element_by_css_selector("#ProductSearchOnBoardingModalModal")
# const event = new Date('August 19, 1975 23:15:30');
# event.setHours(20);
#
# console.log(event);
# // expected output: Tue Aug 19 1975 20:15:30 GMT+0200 (CEST)
# // (note: your timezone may vary)
#
# event.setHours(20, 21, 22);
#
# console.log(event);
# // expected output: Tue Aug 19 1975 20:21:22 GMT+0200 (CEST)
#
#
# var date = new Date();
# date.setHours(0, 0, 0, 0);
# var numberOfDaysToAdd = 0;
# date.setDate(date.getDate() + numberOfDaysToAdd);
#
#
#
#
#
#
#
#
# # interact = driver.find_elements_by_xpath("//[@id='root']//input']")
# # #
# interact = driver.find_element_by_id("ecinput")
#
# interact.click()
# interact.clear()
#
# interact.send_keys(1593147600000)
# interact.submit()
# # interact = driver.find_element_by_id("id_email")
# interact.click()
# # interact = driver.find_element_by_id("id_email")
# interact.click()
# # interact = driver.find_element_by_id("id_email")
# interact.click()

# driver.close()

# sleep(5)



# THIS AREA TO USE FOR THE TMOBILE TEST

# driver.get('https://download.fromdoctopdf.com/index.jhtml')
# interact = driver.find_element_by_css_selector(".customButton1_1")
# interact.click()
# sleep(5)
# windows = driver.window_handles;
# print((windows))
# # driver.switch_to.alert()
# windows = driver.window_handles;
# print((windows))
# # interact = driver.find_element_by_link_text("Run").click()
#
# interact = driver.find_element_by_class_name(".webstore-test-button-label")
# interact.click()

# Setup for finding an element and clicking it
#__________________________________________________________________
# interact = driver.find_element_by_id('theTime')
# # interact.click()
# print((interact.text))
# print(('datetime: ' + str(datetime.datetime.now())))
# interact = driver.get('https://freegeoip.app/xml/')
#
# interact = driver.find_element_by_id('collapsible0')
# print((interact.text))
# sleep(89)

# driver.get("https://www.msn.com");
#
#
#
# loc = driver.find_element_by_id("sb_form_go1")
# print((loc.location))
# print((loc.size))
# sleep(90)
# Setup for finding an element and clicking it
#__________________________________________________________________
# interactive tabbed-standard


# interact = driver.find_element_by_css_selector("a[href='/support']").click()
# interact = driver.find_element_by_css_selector("a[href='https://wiki.saucelabs.com/']").click()

# sleep(15)
# iframe = driver.switch_to.frame(find_element_by_class('interactive'))
# iframe = driver.switch_to.frame(find_element_by_class_name('interactive'))
# interact = driver.find_element_by_link_text("Documentation").click()
# interact = driver.find_element_by_id("i_am_a_textbox").send_keys("Sauce")

# interact = driver.find_element_by_name("q")

# try:
# element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((driver.find_element_by_id("email"))))
# finally:
    # driver.quit()
# interact = driver.find_element_by_id("email")
# interact = driver.find_element_by_class_name("layer-wiziwig ")
# interact.click()
# interact.send_keys('atesting+444bop@cbtnuggets.com')
# interact = driver.find_element_by_id("password")
# interact.click()
# interact.send_keys('XJstgWsu3dwchRyDr')
# interact.submit()
#
# fun sendKeys(element: WebElement, value: String) {
# val length = element.getAttribute("value").length
# for (i in 0 until length)
# element.sendKeys("\u0008")
# element.sendKeys(value)
# }

# Setup for finding an element and sending keystrokes
#__________________________________________________________________
# interact = driver.find_element_by_class_name('_1MDYA').click()
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)


# interact.send_keys('Leonard, TX')
# interact.set_value('Leonard, TX')
# interact.submit()

# Setup for using random Python commands
#__________________________________________________________________
# driver.save_screenshot('screenshot.png')
# sleep(15)
# print('Message')
# interact = driver.find_element_by_class_name("mdl-button__ripple-container").click()
# sleep(15)

# Setup for using Action chains
#__________________________________________________________________
# ActionChains(driver).move_to_element(interact).perform()

# Setup for random script executions
#__________________________________________________________________
# driver.execute_script('sauce: break')
# driver.execute_script('sauce:context=Place words here for notes')

# Ending the test session
# driver.download_(driver.session_id(), "/var/tmp/");
#__________________________________________________________________
driver.quit()
# sauce.downloadHAR("job_id", "/var/tmp/");
