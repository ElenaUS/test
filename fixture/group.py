from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Interes:
    def __init__(self, app):
        self.app = app

    def add_text(self, text):
        self.app.driver.find_element_by_id("pedit_interests_interests").click()
        self.app.driver.find_element_by_id("pedit_interests_interests").send_keys(text.text)
        self.app.driver.find_element_by_id("page_body").click()
        self.app.driver.find_element_by_css_selector(".flat_button").click()
        element = self.app.driver.find_element_by_css_selector(".flat_button")
        actions = ActionChains(self.app.driver)

