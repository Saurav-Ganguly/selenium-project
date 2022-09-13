from getting_dynamic_data import get_data, clean_text

xpath_dynamic = "/html/body/div[1]/div/h1[2]"


def main():
    return clean_text(xpath_dynamic)

print(main())