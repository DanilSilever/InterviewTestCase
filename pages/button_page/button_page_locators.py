from selenium.webdriver.common.by import By


class ButtonPageLocators:
    double_click_button = (By.ID, "doubleClickBtn")
    double_click_result = (By.ID, "doubleClickMessage")
    right_click_button = (By.ID, "rightClickBtn")
    right_click_result = (By.ID, "rightClickMessage")
    click_me_button = (By.XPATH, "//button[text()='Click Me']")
    click_me_result = (By.ID, "dynamicClickMessage")
