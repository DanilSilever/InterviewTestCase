from ..base_page import BasePage
from .checkbox_page_locators import CheckboxPageLocators as Loc


class CheckboxPage(BasePage):
    def collapse_home_dir(self):
        self.browser.find_element(*Loc.home_collapse_btn).click()

    def collapse_download_dir(self):
        self.browser.find_element(*Loc.download_collapse_btn).click()

    def select_word_file(self):
        self.browser.find_element(*Loc.word_file_checkbox).click()

    def should_be_wordfile_in_success_message(self):
        assert "wordFile" in self.browser.find_element(*Loc.text_selected_file).text, "Wrong success message"

    def should_be_checkbox_page_url(self):
        assert self.is_url_contains("checkbox"), "This isn't checkbox page"
