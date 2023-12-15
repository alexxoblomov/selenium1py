from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """
        1) Открываем страницу
        2) Переходим на страницу логина
        3) Проверяем страницу на корректность ссылки, формы регистрации и логина
        """
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)

        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        """
        1) Открываем страницу
        2) Проверяем станицу на корректность ссылки, формы регистрации и логина
        """
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)

        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    1) Открываем страницу
    2) Переходим в корзину
    3) Ожидаем, что в корзине нет товаров
    4) Ожидаем, что есть текст о том, что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)

    page.open()
    page.go_to_basket()
    page.is_basket_empty()
