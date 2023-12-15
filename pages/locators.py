from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span >a")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_STRING = (By.ID, "id_registration-email")
    PASSWORD_STRING = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_STRING = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_BASKET = (By.ID, "add_to_basket_form")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BOOK_NAME_IN_MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_ON_THE_DISPLAY = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    PRICE_IN_MESSAGE_AFTER_ADDING = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")


class BasketPageLocators:
    PRODUCT_IN_BASKET_ROW = (By.CSS_SELECTOR, "#basket_formset > div > div")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")