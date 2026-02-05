# TrashCat Testing with AltTester® and Appium

This project contains automated tests for the TrashCat game using AltTester® with Appium. The tests validate game functionality through the AltTester® Unity SDK.

## What This Project Contains

- **Page Object Models** (`pages/`): Reusable page objects for different game screens
- **Test Suite** (`tests/`): Automated test cases for the TrashCat game
- **Test Runner Script** (`run_tests_android.sh`): Automated script that starts Appium, installs the app, and runs all tests

## Prerequisites

Before running the tests, you need:

1. **AltTester® Desktop** (version 2.0.0 or later)
   - Download from: https://alttester.com/downloads/
   - ❗ **Must be running during test execution**

2. **Appium Server Setup**
   - Follow the setup guide: https://alttester.com/docs/sdk/latest/pages/alttester-with-appium.html

3. **Python Environment**
   - Python 3.x installed
   - Dependencies will be installed automatically by the script

## Setup Instructions

### Step 1: Build the TrashCat APK

You need to create an instrumented `TrashCat.apk` file:

1. Clone the TrashCat Unity project with AltTester® Unity SDK:
   ```bash
   git clone --recursive https://github.com/alttester/trashcat.git
   ```

2. Open the project in Unity

3. Instrument the application using the latest version of AltTester® Unity SDK
   - Detailed instrumentation instructions: https://alttester.com/docs/sdk/latest/pages/get-started.html

4. Build the Android APK from Unity

### Step 2: Add the APK to This Project

1. Create an `app` folder in the project root (if it doesn't exist):
   ```bash
   mkdir app
   ```

2. Copy your instrumented `TrashCat.apk` into the `app/` folder:
   ```
   app/
   └── TrashCat.apk
   ```

## Running the Tests

1. **Start AltTester® Desktop**
   - Open the AltTester® Desktop application

2. **Connect Your Android Device or Emulator**
   - Ensure your device is connected via USB with USB debugging enabled, OR
   - Start an Android emulator

3. **Run the Test Script**
   ```bash
   ./run_tests_android.sh
   ```

### What the Script Does

The `run_tests_android.sh` script automatically:
- Installs/updates all Python dependencies from `requirements.txt`
- Starts the Appium server
- Installs the TrashCat app from the `app/` folder onto your device
- Executes all test cases in the `tests/` folder
- Generates a test report

## Additional Resources

- [AltTester® Documentation](https://alttester.com/docs/sdk/latest/)
- [AltTester® with Appium Guide](https://alttester.com/docs/sdk/latest/pages/alttester-with-appium.html)
- [TrashCat Unity Project](https://github.com/alttester/trashcat)
