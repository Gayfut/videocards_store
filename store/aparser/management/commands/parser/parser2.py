"""file control parser2 specification (parser is not active, need rework)
"""
from selenium.common.exceptions import NoSuchElementException
from parser.base_parser import BaseParser
from parser.settings import (
    link_to_site2,
    search_margin_selector2,
    search_button_selector2,
    product_element_selector2,
    price_selector2,
    name_selector2,
    address_selector2,
)


class Parser2(BaseParser):
    """control parser2"""

    LINK_TO_SITE = link_to_site2
    SEARCH_MARGIN_SELECTOR = search_margin_selector2
    SEARCH_BUTTON_SELECTOR = search_button_selector2
    PRODUCT_ELEMENT_SELECTOR = product_element_selector2
    PRICE_SELECTOR = price_selector2
    NAME_SELECTOR = name_selector2
    ADDRESS_SELECTOR = address_selector2

    def __get_product_price(self):
        """return product price"""
        try:
            price = self.__browser.find_element_by_css_selector(
                self.PRICE_SELECTOR
            ).text
        except NoSuchElementException:
            price = "Цена не указана"

        return price
