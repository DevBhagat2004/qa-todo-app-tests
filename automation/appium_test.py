from appium import webdriver

caps = {
    "platformName": "Android",
    "appium:deviceName": "Pixel 6",
    "appium:app": "https://github.com/amitshekhariitbhu/ToDo/blob/master/apk/todo.apk?raw=true",
    "automationName": "UiAutomator2"
}

def test_add_task():
    driver = webdriver.Remote("http://localhost:4723", caps)
    driver.find_element("id", "com.todoist:id/add_task").click()
    driver.find_element("id", "com.todoist:id/text").send_keys("Automated test")
    driver.find_element("id", "com.todoist:id/submit").click()
    assert "Automated test" in driver.page_source
    driver.quit()
