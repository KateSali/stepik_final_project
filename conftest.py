import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose the language")

@pytest.fixture(scope="function")
def user_language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="function")
def browser(request, user_language):
    options = Options()
    options.add_experimental_option(
    'prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
