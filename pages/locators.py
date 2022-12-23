from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASS1 = (By.NAME, "registration-password1")
    REGISTER_PASS2 = (By.NAME, "registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")
    REGISTER_SUCCESS = (By.CLASS_NAME, "alert-success")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_INFO_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CLASS_NAME, "btn-group>:nth-child(1)")
    BASKET_ITEM = (By.CLASS_NAME, "basket-item")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
