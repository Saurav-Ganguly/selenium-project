from login import get_data as login_automated
from getting_dynamic_data import clean_text
import time

xpath_dynamic = "/html/body/div[1]/div/h1[2]"
#when an element has id use the id insted of xpath
id_username_textbox = "id_username"
id_password_textbox = "id_password"
xpath_submit_btn = "/html/body/div[1]/div/div/div[3]/form/button"


def main():
  return login_automated((id_username_textbox, id_password_textbox, xpath_submit_btn))
    

print(main())