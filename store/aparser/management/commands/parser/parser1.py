"""file control parser1 specification
"""
from .base_parser import BaseParser
from .settings import (
    link_to_site1,
    search_margin_selector1,
    search_button_selector1,
    product_element_selector1,
    price_selector1,
    name_selector1,
    address_selector1,
    next_page_selector1,
)


class Parser1(BaseParser):
    """control parser1"""

    LINK_TO_SITE = link_to_site1
    SEARCH_MARGIN_SELECTOR = search_margin_selector1
    SEARCH_BUTTON_SELECTOR = search_button_selector1
    PRODUCT_ELEMENT_SELECTOR = product_element_selector1
    PRICE_SELECTOR = price_selector1
    NAME_SELECTOR = name_selector1
    ADDRESS_SELECTOR = address_selector1
    NEXT_PAGE_SELECTOR = next_page_selector1
