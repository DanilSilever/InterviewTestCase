from ..base_page import BasePage
from .elements_page_locators import ElementsPageLocators as Loc
from ..checkbox_page.checkbox_page import CheckboxPage
from ..button_page.button_page import ButtonPage


class ElementsPage(BasePage):
    def go_to_checkbox_page(self):
        self.browser.find_element(*Loc.checkbox_btn).click()
        return CheckboxPage(self.browser, self.browser.current_url)

    def go_to_buttons_page(self):
        self.browser.find_element(*Loc.buttons_page).click()
        return ButtonPage(self.browser, self.browser.current_url)

    def should_be_elements_page_url(self):
        assert self.is_url_contains("elements"), "This isn't elements page"
