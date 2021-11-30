from requests.auth import HTTPBasicAuth
import os, requests
​
SAUCE_USERNAME= os.environ["SAUCE_USERNAME"]
SAUCE_ACCESS_KEY = os.environ["SAUCE_ACCESS_KEY"]
​
devices_with_sdcard = 0
​
response = requests.get("https://api.eu-central-1.saucelabs.com/v1/rdc/devices", auth=HTTPBasicAuth(SAUCE_USERNAME, SAUCE_ACCESS_KEY))
​
for device in response.json():
	if device["sdCardSize"] > 0:
		devices_with_sdcard += 1
​
print("Devices: " + str(devices_with_sdcard))
