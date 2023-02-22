import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HtmlTestRunner import HTMLTestRunner

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/mnt/c/chrome-driver/linux/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo.onestepcheckout.com/")
        

    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        create_account_button = driver.find_element(By.LINK_TEXT, 'CREATE AN ACCOUNT')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID, 'firstname')
        last_name = driver.find_element(By.ID, 'lastname')
        email = driver.find_element(By.ID, 'email_address')
        password = driver.find_element(By.ID, 'password' )
        confirm_password = driver.find_element(By.ID, 'confirmation')
        newsletter = driver.find_element(By.ID, 'is_subscribed')
        submit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email.is_enabled() and password.is_enabled() and confirm_password.is_enabled() and newsletter.is_enabled() and submit_button.is_enabled())
        
        
        first_name.send_keys('Test')
        last_name.send_keys('Test')
        email.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        newsletter.click()
        submit_button.click()
        
        

    def tearDown(self):
        self.driver.quit()
       

if __name__ == '__main__':
    unittest.main(verbosity=2)