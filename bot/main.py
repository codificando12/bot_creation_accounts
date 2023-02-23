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
        email = first_name('MOCK_DATA.csv')
        email = first_name('MOCK_DATA.csv')

        print(firstname)



if __name__ == '__main__':
    unittest.main(verbosity=2)