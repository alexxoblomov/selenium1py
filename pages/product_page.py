from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def message_about_adding(self):
        self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING)

    def no_message_about_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def message_about_adding_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "The element has not disappeared"

    def book_names_is_match(self):
        book_name_in_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE_ABOUT_ADDING).text
        assert book_name_in_page == book_name_in_message, "the books don't match"

    def book_prices_is_match(self):
        price_on_the_display = self.browser.find_element(*ProductPageLocators.PRICE_ON_THE_DISPLAY).text
        price_in_message_after_adding = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE_AFTER_ADDING).text
        assert price_on_the_display == price_in_message_after_adding, "the prices don't match"