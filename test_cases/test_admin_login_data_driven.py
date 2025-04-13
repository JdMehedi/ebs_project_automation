import pytest
from selenium import webdriver
from base_pages.Login_Admin_page import LoginAdminPage
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test_02_Admin_Login:
    logger = Log_Maker.log_gen()
    expected_url = "https://uat-crm.oss.net.bd/dashboard"
    err_message_xpath = "//span[@id='input-error']"
    path = ".//test_data//login_ddt.xlsx"

    def test_login_data_driven(self, setup):
        self.logger.info("************Test_01_Admin_Login****************")
        self.logger.info("************ test_login_data_driven****************")
        project_url = Read_Config.get_page_url()
        self.driver = setup
        self.driver.implicitly_wait(10)
        print("URL is:", project_url)
        self.driver.get(project_url)
        self.logged_in = LoginAdminPage(self.driver)
        sleep(3)
        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print("num of rows:", self.rows)
        for r in range(2, self.rows + 1):
            self.logged_in.click_login_button()
            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            sleep(4)
            self.logged_in.enter_username(self.username)
            self.logged_in.enter_password(self.password)
            self.logged_in.finally_click_login_button()
            if self.driver.current_url == self.expected_url:
                assert True
                print("Login Test Passed")
                self.driver.find_element(By.XPATH,
                                         "//li[@class='dropdown user user-menu']//a[@class='dropdown-toggle']").click()
                sleep(3)
                self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign out']").click()
            else:
                current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_name = f"./screenshots/test_login{current_time}.png"
                self.driver.save_screenshot(screenshot_name)
                self.driver.close()
                print("Login Test Failed")
                assert False

        self.driver.close()
