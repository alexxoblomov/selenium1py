import time
import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('link',
 ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    """
    1) Открываем страницу
    2) Добавляем товар в корзину
    3) Даем ответ на задачу и подтверждаем все алерты
    4) Смотрим, что название книги на витрине и в сообщении о добавлении совпадают
    5) Смотрим, что цена на витрине и в сообщении о добавлении в корзину совпадают
    """
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(120)
    page.book_names_is_match()
    page.book_prices_is_match()

@pytest.mark.negative
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    1) Открываем страницу
    2) Добавляем товар в корзину
    3) Ожидаем, что сообщение об успешном добавлении не появилось
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.no_message_about_adding()

@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    """
    1) Открываем страницу
    2) Ожидаем, что сообщение об успешном добавлении не появилось
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)

    page.open()
    page.no_message_about_adding()
@pytest.mark.negative
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1) Открываем страницу
    2) Добавляем в корзину
    3) Ожидаем, что сообщение о добавлении пропадает со временем
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.message_about_adding_disappeared()