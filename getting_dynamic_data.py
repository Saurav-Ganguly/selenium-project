import time

from my_driver import get_driver


def get_data(xpath):
    driver = get_driver()
    # vlaue will not apper immediately
    time.sleep(5)
    element = driver.find_element("xpath", xpath)
    return element.text


def clean_text(xpath):
    """Extract only the temperature from text"""
    text = get_data(xpath)
    output = float(text.split(": ")[1])
    return output
