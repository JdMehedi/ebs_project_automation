from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAdminPage:
    source_login_button_link_text = "Login"
    login_button_link_text = "Log In"
    username_textbox_xpath = "//input[@id='username']"
    password_textbox_xpath = "(//input[@id='password'])[1]"
    login_submit_button_xpath = "//input[@id='kc-login']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.source_login_button_link_text))).click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.login_button_link_text))).click()

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_textbox_xpath)))
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_textbox_xpath)))
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def finally_click_login_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_submit_button_xpath))).click()
