from selenium import webdriver
#webdriver -> web browser


def get_driver():
    #options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    # on linux machine
    options.add_argument("disable-dev-shm-usage")
    #sandboxing -> to avoid security
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("diable-blink-features-AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element("xpath", "/html/body/div[1]/div/h1[1]")
    return element.text


print(main())
