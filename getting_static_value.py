from my_driver import get_driver


def get_data(xpath):
    driver = get_driver()
    element = driver.find_element("xpath", xpath)
    return element.text
