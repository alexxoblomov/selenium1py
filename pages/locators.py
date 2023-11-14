from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.ID, "add_to_basket_form")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div:nth-child(1) > div")
    BOOK_NAME_IN_MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_ON_THE_DISPLAY = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    PRICE_IN_MESSAGE_AFTER_ADDING = (By.XPATH,"/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")