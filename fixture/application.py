import pytest, unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fixture.login import Login
from fixture.group import Interes


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome("/Applications/chromedriver")
        self.driver.implicitly_wait(60)
        self.login = Login(self)
        self.group = Interes(self)
        self.vars = {}

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_page_vk(self):
        self.driver.get("https://vk.com/")
        self.driver.set_window_size(1200, 682)

    def click_mypage_left(self):
        self.driver.find_element_by_css_selector("#l_pr").click()

    def menu__top(self):
        self.driver.find_element_by_id("top_profile_link").click()
        self.driver.find_element_by_id("top_edit_link").click()
        element = self.driver.find_element_by_id("ui_rmenu_contacts")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element_by_css_selector("body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element_by_css_selector("#ui_rmenu_interests > span").click()
        element = self.driver.find_element_by_css_selector("#ui_rmenu_interests > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def logout(self):
        element = self.driver.find_element_by_id("top_profile_link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element_by_css_selector("body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element_by_css_selector(".top_profile_arrow").click()
        self.driver.find_element_by_id("top_logout_link").click()

    def destroy(self):
        self.driver.quit()
