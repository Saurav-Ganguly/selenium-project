from selenium import webdriver

def get_driver(url="http://automated.pythonanywhere.com/"):
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
    driver.get(url)
    return driver