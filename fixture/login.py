class Login:
    def __init__(self, app):
        self.app = app

    def login_page(self, username, password):
        self.app.open_page_vk()
        self.app.driver.find_element_by_id("index_email").click()
        self.app.driver.find_element_by_id("index_email").send_keys(username)
        self.app.driver.find_element_by_id("index_pass").click()
        self.app.driver.find_element_by_id("index_pass").send_keys(password)
        self.app.driver.find_element_by_id("index_login_button").click()