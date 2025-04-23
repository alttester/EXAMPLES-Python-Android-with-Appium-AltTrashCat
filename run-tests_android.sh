#!/bin/bash

echo "Installing dependencies"
chmod 0755 requirements.txt
python -m pip install -r requirements.txt

echo "Starting Appium ..."
appium --log-no-colors --log-timestamp  --command-timeout 60  > appium.log 2>&1 &
sleep 10
ps -ef|grep appium

#App file is under the app/ folder inside the current working folder
export APPIUM_APPFILE=$PWD/app/TrashCat.apk 

## Appium Options:
export APPIUM_URL="http://localhost:4723/wd/hub"
export APPIUM_DEVICE="Local Device"
export APPIUM_PLATFORM="android"
export APPIUM_AUTOMATION="uiautomator2"

## Run the test:
echo "Running tests"

rm -rf screenshots
python -m pytest tests/ -s

echo "Tests done"
