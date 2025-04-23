Info about the required setup and how to run these tests can be found here:
https://alttester.com/docs/sdk/latest/pages/alttester-with-appium.html This should include properly setting up Appium server too.

### Running the tests on Android
**Prerequisite**:

❗ Starting with version 2.0.0, the AltTester® Desktop must be running on your PC while the tests are running. You can take it from https://alttester.com/downloads/.

**How to run the tests:**
1. Open the AltTester® Desktop
2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x).
3. Create a folder `app` and include the instrumented app under the folder.
3. `./run-tests_android.sh` command in your terminal

This script will:

* update/install dependencies listed in requirements.txt
* start appium which will install the TrashCat app from the `app/` folder
* remove any screenshots taken previously
* run all tests under `tests/` folder
