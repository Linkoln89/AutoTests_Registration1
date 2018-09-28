import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class RegistrationFirstStep(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_first_step(self):
        driver = self.driver
        driver.get("https://moneyman:1005@qa-delivery-br-master.moneyman.ru/registration-gf/static/#/step1")
        
        elem = driver.find_element_by_name("name")
        elem.send_keys("Demo Demosson")
        
        elem = driver.find_element_by_name("mothersName")
        elem.send_keys("Demo Demossona")
        
        elem = driver.find_element_by_name("phone")
        elem.send_keys("10925545432")
        
        elem = driver.find_element_by_name("email")
        elem.send_keys("tetete777777@mail.ru")
        
        elem = driver.find_element_by_name('nextBtn'). click()

        elem = driver.switch_to_active_element

        elem = driver.find_element_by_name ("confirmationCode")
        elem.send_keys("1111")

        elem = driver.find_element_by_class ('form__checkbox-box'). click()

        elem = driver.find_element_by_name ('confirmMobileBtn'). click()

        elem = driver.switch_to_active_element

if __name__ == "__main__":
    unittest.main()

#print('Done!!')