from ..base_page import BasePage
from .button_page_locators import ButtonPageLocators as Loc
from selenium.webdriver import ActionChains


class ButtonPage(BasePage):
    def double_click(self):
        double_click_btn = self.browser.find_element(*Loc.double_click_button)
        action = ActionChains(self.browser)
        action.double_click(on_element=double_click_btn)
        action.perform()

    def should_be_double_click_result(self):
        assert self.browser.find_element(*Loc.double_click_result).text == "You have done a double click", \
            "Wrong double_click result"

    def right_click(self):
        right_click_btn = self.browser.find_element(*Loc.right_click_button)
        action = ActionChains(self.browser)
        action.context_click(on_element=right_click_btn)
        action.perform()

    def should_be_right_click_result(self):
        assert self.browser.find_element(*Loc.right_click_result).text == "You have done a right click", \
            "Wrong right_click result"

    def click_me(self):
        self.browser.find_element(*Loc.click_me_button).click()

    def should_be_click_me_result(self):
        assert self.browser.find_element(*Loc.click_me_result).text == "You have done a dynamic click", \
            "Wrong click_me result"
