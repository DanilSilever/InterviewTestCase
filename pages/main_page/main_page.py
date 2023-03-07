from ..base_page import BasePage
from .main_page_locators import MainPageLocators as Loc
from ..elements_page.elements_page import ElementsPage


class MainPage(BasePage):
    def go_to_elements_page(self):
        self.browser.find_element(*Loc.elements_btn).click()
        return ElementsPage(self.browser, self.browser.current_url)
