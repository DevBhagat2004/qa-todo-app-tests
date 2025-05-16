import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

@pytest.fixture
def driver():
    caps = {
        'platformName': 'Android',
        'deviceName': 'Pixel 6',
        'app': 'https://example.com/todo_app.apk',
        'automationName': 'UiAutomator2'
    }
    driver = webdriver.Remote('http://localhost:4723', caps)
    yield driver
    driver.quit()

def test_add_task(driver):
    driver.find_element_by_id('add_btn').click()
    driver.find_element_by_id('task_input').send_keys('Automated test')
    driver.find_element_by_id('save_btn').click()
    assert 'Automated test' in driver.page_source

def test_swipe_to_delete(driver):
    # Add test task
    driver.find_element_by_id('add_btn').click()
    driver.find_element_by_id('task_input').send_keys('To delete')
    driver.find_element_by_id('save_btn').click()
    
    # Swipe to delete
    task = driver.find_element_by_xpath('//android.widget.TextView[@text="To delete"]')
    TouchAction(driver).press(task).wait(1000).move_to(x=-300, y=0).release().perform()
    driver.find_element_by_id('delete_btn').click()
    assert 'To delete' not in driver.page_source

def test_offline_behavior(driver):
    # Toggle airplane mode
    driver.set_network_connection(0)
    try:
        driver.find_element_by_id('add_btn').click()
        assert driver.find_element_by_id('offline_warning').is_displayed()
    finally:
        driver.set_network_connection(6)
