from read_csv import first_name, last_name, email, password
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HtmlTestRunner import HTMLTestRunner

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\chrome-driver\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
    
    def test_new_user(self):
        firstname = first_name('MOCK_DATA.csv')
        lastname = last_name('MOCK_DATA.csv')
        e_mail = email('MOCK_DATA.csv')
        password_ind = password('MOCK_DATA.csv')

        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        create_account_button = driver.find_element(By.LINK_TEXT, 'CREATE AN ACCOUNT')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)
        
        for user in range(3, len(firstname)):
            
            slot_firstname = driver.find_element(By.ID, 'firstname')
            slot_lastname = driver.find_element(By.ID, 'lastname')
            slot_email = driver.find_element(By.ID, 'email_address')
            slot_password = driver.find_element(By.ID, 'password')
            slot_confirm_password = driver.find_element(By.ID, 'confirmation')
            slot_newsletter = driver.find_element(By.ID, 'is_subscribed')
            submit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span')
        
            self.assertTrue(slot_firstname.is_enabled() and slot_lastname.is_enabled() and slot_email.is_enabled() and slot_password.is_enabled() and slot_confirm_password.is_enabled() and slot_newsletter.is_enabled() and submit_button.is_enabled())
        
            slot_firstname.send_keys(firstname[user])
            slot_lastname.send_keys(lastname[user])
            slot_email.send_keys(e_mail[user])
            slot_password.send_keys(password_ind[user])
            slot_confirm_password.send_keys(password_ind[user])
            slot_newsletter.click()
            submit_button.click()
            
            
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)