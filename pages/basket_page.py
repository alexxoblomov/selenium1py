from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_ROW), \
            "Basket is not empty"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "No empty basket message"

    def is_basket_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_ROW), \
            "Basket is empty"
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "The message is present on the page"
