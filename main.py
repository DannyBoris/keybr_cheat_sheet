"""
This script cheats the keybr.com site (blind typing exercise)
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def send_keys_no_input(actions, key):
    """
    When no target is speciefied for a keystroke
    :param actions: :type ActionChains
    :param key: :type String || Keys Object
    :return: None
    """
    actions.send_keys(key).perform()
    return None


def cheat(times=50):
    """
    Makes you the fastest and most accurate typer on the planet
    :param times: :type int
    :return: None
    """
    actions = ActionChains(driver)
    for time in range(times):
        spans = driver.find_elements_by_class_name('TextInput-item')
        for span in spans:
            if span.text == '␣':
                send_keys_no_input(actions=actions, key=Keys.SPACE)
            else:
                send_keys_no_input(actions=actions, key=span.text)
            sleep(.05)
    return None


def create_driver(browser=webdriver.Chrome):
    """
    Creates a driver
    :param browser: :type webdriver
    :return: driver
    """
    global driver
    selenium_path = 'C:\\Users\danny\\Downloads\\chromedriver_win32\\chromedriver.exe'
    website = 'https://www.keybr.com/'
    driver = browser(selenium_path)
    driver.get(website)
    return driver


def main():
    driver = create_driver()
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    click_to_start_elem = driver.find_element_by_css_selector('.TextInput.TextInput--sizeX0')
    start_click = ActionChains(driver).move_to_element(click_to_start_elem)
    start_click.click().perform()
    cheat()


if __name__ == "__main__":
    main()










# driver.quit()