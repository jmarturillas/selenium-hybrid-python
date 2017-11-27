from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory(object):

    driver = None

    def __init__(self, browser=None):
        self.browser = browser
        self.driver = None

    def start_browser(self):
        if self.browser is not None:
            if self.browser == "chrome":
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            elif self.browser == "firefox":
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            else:
                raise Exception("Cannot recognize browser.")

            self.driver.maximize_window()
        else:
            raise Exception("Unable to initialize with empty parameter.")


class Invoker(object):

    def __init__(self, browser):
        self.browser = browser
        self.start_driver()
        self.driver = None

    def start_driver(self):
        BrowserFactory(self.browser).start_browser()

    def get_driver(self):
        self.driver = BrowserFactory.driver


if __name__ == "__main__":
    """ Used to test this class if each browser is working. """
    driver = Invoker("firefox")

# TODO :: Create a global method that reflects WebDriver as return type
