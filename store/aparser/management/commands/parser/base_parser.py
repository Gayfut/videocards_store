"""file control parser and his specification
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from itertools import groupby
from .settings import (
    request_text,
    product_link_attribute,
    img_link_attribute,
    img_element_selector,
    price_attribute1,
    success_search_selector,
)

from products.models import Product, Image


class BaseParser:
    """control parser specification"""

    LINK_TO_SITE = None
    SEARCH_MARGIN_SELECTOR = None
    SEARCH_BUTTON_SELECTOR = None
    PRODUCT_ELEMENT_SELECTOR = None
    PRICE_SELECTOR = None
    NAME_SELECTOR = None
    ADDRESS_SELECTOR = None
    NEXT_PAGE_SELECTOR = None

    def __init__(self):
        self.__browser = webdriver.Firefox(options=self.__set_options())
        self.main_window = None

    @staticmethod
    def __set_options():
        """return headless options for parser driver"""
        options = Options()
        options.add_argument("--headless")

        return options

    def start_pars(self, pages_count):
        """start parsing"""
        self.__open_site()
        self.__search_in_site()

        success_search = self.__check_success_search()
        while success_search is False:
            self.__search_in_site()
            success_search = self.__check_success_search()

        for _step in range(pages_count):
            self.__save_products_info()
            self.__next_page()

    def __next_page(self):
        """open next page of search for parsing"""
        next_page_button = self.__browser.find_element_by_css_selector(self.NEXT_PAGE_SELECTOR).click()

    def __open_site(self):
        """open site for parsing"""
        self.__browser.get(self.LINK_TO_SITE)
        self.main_window = self.__browser.current_window_handle

    def __search_in_site(self):
        """find search margin, send request and submit"""
        search_margin = self.__browser.find_element_by_css_selector(
            self.SEARCH_MARGIN_SELECTOR
        )
        search_margin.clear()
        search_margin.send_keys(request_text)

        search_button = self.__browser.find_element_by_css_selector(
            self.SEARCH_BUTTON_SELECTOR
        )
        search_button.click()

    def __check_success_search(self):
        """check search success rate"""
        try:
            success_search = self.__browser.find_element_by_css_selector(
                success_search_selector
            )
        except NoSuchElementException:
            return False

        return True

    def __save_products_info(self):
        """open new tab, parse links and return info about products"""
        products_links = self.__get_links()
        products_links = [link for link, _ in groupby(products_links)]

        self.__browser.execute_script("window.open('');")
        self.__browser.switch_to.window(self.__browser.window_handles[1])

        for link_to_product in products_links:
            self.__save_product_info(link_to_product)

        self.__browser.close()
        self.__browser.switch_to.window(self.__browser.window_handles[0])

    def __get_links(self):
        """find elements and return products links"""
        products_elements = self.__browser.find_elements_by_css_selector(
            self.PRODUCT_ELEMENT_SELECTOR
        )
        products_links = []

        for product_element in products_elements:
            product_link = product_element.get_attribute(product_link_attribute)
            products_links.append(product_link)

        return products_links

    def __save_product_info(self, link_to_product):
        """save info about definite product"""
        self.__browser.get(link_to_product)

        img_elements = self.__browser.find_elements_by_css_selector(
            img_element_selector
        )

        try:
            address = self.__browser.find_element_by_css_selector(
                self.ADDRESS_SELECTOR
            ).text
        except NoSuchElementException:
            address = "Адреса нет"

        try:
            product = Product.objects.get(link=link_to_product)
        except Product.DoesNotExist:
            product = Product(link=link_to_product)
        product.name = self.__browser.find_element_by_css_selector(
            self.NAME_SELECTOR
        ).text
        product.price = self.__get_product_price()
        product.address = address
        product.save()

        for img_element in img_elements:
            img_link = img_element.get_attribute(img_link_attribute)
            Image(link=img_link, product=product).save()

    def __get_product_price(self):
        """return product price"""
        try:
            price = self.__browser.find_element_by_css_selector(
                self.PRICE_SELECTOR
            ).get_attribute(price_attribute1)
        except NoSuchElementException:
            price = 0

        return price

    def stop_pars(self):
        """stop parsing"""
        self.__browser.quit()
