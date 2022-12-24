from .base_page import BasePage
from .locators import LoginPageLocators
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        reg_pass1.send_keys(password)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        reg_pass2.send_keys(password)
        reg_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        reg_submit.click()
        WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_SUCCESS))
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_url(self):
        assert "login" in self.url, "The substring 'login' is not present in the current url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

   
