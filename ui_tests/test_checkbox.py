import pytest
import allure
from pages.main_page.main_page import MainPage


class TestCheckbox:
    link = "https://demoqa.com/"

    @allure.title("Test word file checkbox")
    def test_checkbox_word_file(self, browser):
        page = MainPage(browser, self.link)
        page.open()

        page = page.go_to_elements_page()
        page.should_be_elements_page_url()

        page = page.go_to_checkbox_page()
        page.should_be_checkbox_page_url()
        page.collapse_home_dir()
        page.collapse_download_dir()
        page.select_word_file()
        page.should_be_wordfile_in_success_message()
