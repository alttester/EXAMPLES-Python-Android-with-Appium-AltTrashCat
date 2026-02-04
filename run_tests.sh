#!/bin/bash

# Detect OS and set Python command
if [[ "$OSTYPE" == "darwin"* ]]; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Set environment variables for the test
export APPIUM_APPFILE=$PWD/app/AltTesterUnrealSDK.apk 
export APPIUM_URL="http://localhost:4723"
export APPIUM_DEVICE="Local Device"
# export APPIUM_UDID="[REPLACE_WITH_DEVICE_UDID]"
export APPIUM_PLATFORM="Android"
export APPIUM_AUTOMATION="UIAutomator2"

# Install dependencies
echo "Installing dependencies"
chmod 0755 requirements.txt
$PYTHON_CMD -m pip install -r requirements.txt

# Decide which Appium driver to check/install based on APPIUM_PLATFORM
platform_lc=$(echo "${APPIUM_PLATFORM:-Android}" | tr '[:upper:]' '[:lower:]')
if [[ "$platform_lc" == "android" ]]; then
    echo "Checking Appium UIAutomator2 driver..."
    if appium driver list --installed 2>&1 | grep -qi "uiautomator2"; then
        echo "UIAutomator2 driver already installed"
    else
        echo "Installing UIAutomator2 driver..."
        appium driver install uiautomator2
    fi
elif [[ "$platform_lc" == "ios" ]]; then
    echo "Checking Appium XCUITest driver..."
    if appium driver list --installed 2>&1 | grep -qi "xcuitest"; then
        echo "XCUITest driver already installed"
    else
        echo "Installing XCUITest driver..."
        appium driver install xcuitest
    fi
fi

# Stop any existing Appium instances
echo "Stopping any existing Appium instances..."
pkill -f appium 2>/dev/null || true
sleep 2

# Start Appium server
echo "Starting Appium..."
appium --log-no-colors --log-timestamp -p 4723 --keep-alive-timeout 60 > appium.log 2>&1 &

# Wait for Appium to start
echo "Waiting for Appium to start..."
MAX_WAIT=30
COUNTER=0
while [ $COUNTER -lt $MAX_WAIT ]; do
    if lsof -i :4723 >/dev/null 2>&1; then
        echo "Appium started successfully!"
        break
    fi
    echo "Waiting... ($COUNTER/$MAX_WAIT)"
    sleep 1
    COUNTER=$((COUNTER + 1))
done

if [ $COUNTER -eq $MAX_WAIT ]; then
    echo "Error: Appium failed to start within $MAX_WAIT seconds"
    exit 1
fi

ps -ef|grep appium

# Clean up old screenshots
rm -rf screenshots

# Run tests
echo "Running tests"
$PYTHON_CMD -m pytest tests/ -s

echo "Tests done"
