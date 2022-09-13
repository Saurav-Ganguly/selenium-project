# adding the login functionality
from my_driver import get_driver
from selenium.webdriver.common.keys import Keys
import time

userid= "automated"
password = "automatedautomated"
loginURL = "http://automated.pythonanywhere.com/login/"

def get_data(element_identifier):
  id_username, id_password, xpath_submit = element_identifier
  driver = get_driver(loginURL)
  # enter username  
  driver.find_element("id", id_username).send_keys(userid)
  time.sleep(2)
  # enter password and press enter
  driver.find_element("id", id_password).send_keys(password + Keys.RETURN)
  print(driver.current_url)
  time.sleep(5)
  #click on home (optional)
  driver.find_element("xpath", "/html/body/nav/div/a").click()
  print(driver.current_url)
  #scrape the current temperature after login (part of exercise)
  time.sleep(5)
  element = driver.find_element("xpath", "/html/body/div[1]/div/h1[2]")
  return element.text
  