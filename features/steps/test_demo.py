from behave import *
from selenium import webdriver

@given(u'launch chrome browser')
def launchBrowser(context):
    # context.driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    context.driver=webdriver.Chrome()

@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")


@then(u'verity that the logo present on page')
def verifyLogo(context):
    status=context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
