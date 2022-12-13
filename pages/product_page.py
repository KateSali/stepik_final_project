from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()
        time.sleep(3) 
        self.should_be_add_to_basket_alert(self.get_book_name())
        self.should_be_price_info_alert(self.get_price())

    def get_book_name(self):
        return(self.browser.find_element(*ProductPageLocators.BOOK_NAME))

    def get_price(self):
        return(self.browser.find_element(*ProductPageLocators.PRICE))

    def should_be_add_to_basket_alert(self, book_name):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_ALERT), "Success alert is not presented"
        success_alert = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_ALERT)
        assert book_name.text == success_alert.text, "Book name is not present in success alert"  

    def should_be_price_info_alert(self, price):
        assert self.is_element_present(*ProductPageLocators.PRICE_INFO_ALERT), "Info alert is not presented"
        info_alert = self.browser.find_element(*ProductPageLocators.PRICE_INFO_ALERT)
        assert price.text == info_alert.text, "Price is not present in info alert"
