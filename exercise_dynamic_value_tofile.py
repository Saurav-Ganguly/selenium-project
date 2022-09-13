from my_driver import get_driver
import time

def get_temp():
  xpath = "/html/body/div[1]/div/h1[2]"
  driver = get_driver()
  time.sleep(2)
  el = driver.find_element(by="xpath", value = xpath)
  output = float(el.text.split(": ")[1])
  return output

def write_text_tofile(txt, file_name):
  with open(file_name, 'w') as f:
    f.write(txt)
  