from selenium.webdriver.common.by import By


class CheckboxPageLocators:
    home_collapse_btn = (By.XPATH, '//span[contains(@class, "rct-text")]/button')
    download_collapse_btn = (By.XPATH, '//li[contains(@class, "rct-node")]/ol/li[3]/span/button')
    word_file_checkbox = (By.XPATH, '//span[contains(@class, "rct-title") and text()="Word File.doc"]')
    text_selected_file = (By.CSS_SELECTOR, ".text-success")

