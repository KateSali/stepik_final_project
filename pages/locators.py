from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_INFO_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
