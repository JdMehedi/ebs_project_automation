import pytest
from selenium import webdriver
from base_pages.Login_Admin_page import LoginAdminPage
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker



class Test_01_Admin_Login:
    project_url = Read_Config.get_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_user_name ="hasan@ba-systems.com"
    expected_url = "https://uat-crm.oss.net.bd/dashboard"
    err_message_xpath = "//span[@id='input-error']"
    logger = Log_Maker.log_gen()

    def test_invalid_login(self, setup):
        self.logger.info("************Test_01_Admin_Login****************")
        self.logger.info("************ verification of test_invalid_login****************")
        self.driver = setup
        self.driver.get(self.project_url)
        self.logged_in = LoginAdminPage(self.driver)
        self.logged_in.click_login_button()
        self.logged_in.enter_username(self.invalid_user_name)
        self.logged_in.enter_password(self.password)
        self.logged_in.finally_click_login_button()
        error_msg = self.driver.find_element(By.XPATH, self.err_message_xpath)
        sleep(5)
        if error_msg.text == "Invalid username or password.":
            self.logger.info("************ assertion is true ****************")
            assert True
            self.driver.close()
        else:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            ss_name = f"./screenshots/test_invalid_login_{current_time}.png"
            self.driver.save_screenshot(ss_name)
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.project_url)
        self.logged_in = LoginAdminPage(self.driver)
        self.logged_in.click_login_button()
        sleep(3)
        self.logged_in.enter_username(self.username)
        self.logged_in.enter_password(self.password)
        self.logged_in.finally_click_login_button()
        sleep(5)
        if self.driver.current_url == self.expected_url:
            assert True
            print("Login Test Passed")
            self.driver.close()
        else:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"./screenshots/test_login{current_time}.png"
            self.driver.save_screenshot(screenshot_name)
            self.driver.close()
            print("Login Test Failed")
            assert False




