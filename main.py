# from login import get_data as login_automated
# from getting_dynamic_data import clean_text
# import time

# xpath_dynamic = "/html/body/div[1]/div/h1[2]"
# #when an element has id use the id insted of xpath
# id_username_textbox = "id_username"
# id_password_textbox = "id_password"
# xpath_submit_btn = "/html/body/div[1]/div/div/div[3]/form/button"

# def main():
#   return login_automated((id_username_textbox, id_password_textbox, xpath_submit_btn))

# print(main())

#--------------------------------------------------
# Exercise (Writing the dynamic data to file)
import time
from datetime import datetime
from exercise_dynamic_value_tofile import get_temp, write_text_tofile


def get_dateandtime():
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)

    hour = str(datetime.now().hour)
    min = str(datetime.now().minute)
    sec = str(datetime.now().second)
    return f"{day}-{month}-{year} {hour}:{min}:{sec}"


def main():
    temp = str(get_temp())
    date_now = get_dateandtime()
    write_text_tofile(temp, date_now + ".txt")


while True:
    main()
    time.sleep(2)
