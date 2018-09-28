#step1

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BRRegistrationStep1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_b_r_registration_step1(self):
        driver = self.driver
        driver.get("https://qa-delivery-br-master.moneyman.ru/registration-gf/static/#/step1")
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Demo Demosson")
        driver.find_element_by_id("mothersName").click()
        driver.find_element_by_id("mothersName").clear()
        driver.find_element_by_id("mothersName").send_keys("Demo Demosson")
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("(10)925978979")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("(10)925978979")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("tetst@mail.ru")
        driver.find_element_by_name("nextBtn").click()
        driver.find_element_by_id("confirmationCode").click()
        driver.find_element_by_id("confirmationCode").clear()
        driver.find_element_by_id("confirmationCode").send_keys("1111")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Termos e Condições Gerais'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Enviar novo código'])[1]/following::span[1]").click()
        driver.find_element_by_name("confirmMobileBtn").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


######################################################################################step2
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BRRegistrationStep2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_b_r_registration_step2(self):
        driver = self.driver
        driver.get("https://qa-delivery-br-master.moneyman.ru/registration-gf/static/#/step2")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::label[2]").click()
        driver.find_element_by_id("birthday").click()
        driver.find_element_by_id("birthday").clear()
        driver.find_element_by_id("birthday").send_keys("01.01.1980")
        driver.find_element_by_id("birthday").clear()
        driver.find_element_by_id("birthday").send_keys("01.01.1980")
        driver.find_element_by_id("birthday").clear()
        driver.find_element_by_id("birthday").send_keys("01.01.1980")
        driver.find_element_by_id("birthday").clear()
        driver.find_element_by_id("birthday").send_keys("01.01.1980")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[3]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Selecionar...'])[1]/following::div[7]").click()
        driver.find_element_by_id("insuranceNumber").click()
        driver.find_element_by_id("insuranceNumber").clear()
        driver.find_element_by_id("insuranceNumber").send_keys("323.231.313-13")
        driver.find_element_by_id("insuranceNumber").clear()
        driver.find_element_by_id("insuranceNumber").send_keys("323.231.313-13")
        driver.find_element_by_id("docIdentificationNumber").click()
        driver.find_element_by_id("docIdentificationNumber").clear()
        driver.find_element_by_id("docIdentificationNumber").send_keys("142342")
        driver.find_element_by_id("docIdentificationNumber").clear()
        driver.find_element_by_id("docIdentificationNumber").send_keys("142342213")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[7]/following::div[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='SSP'])[1]/following::div[3]").click()
        driver.find_element_by_id("docIssuanceDate").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Sáb'])[1]/following::select[2]").click()
        driver.find_element_by_id("docIssuanceDate").clear()
        driver.find_element_by_id("docIssuanceDate").send_keys("05.01.2010")
        driver.find_element_by_id("docIssuanceDate").clear()
        driver.find_element_by_id("docIssuanceDate").send_keys("05.01.2010")
        driver.find_element_by_id("docIssuanceDate").clear()
        driver.find_element_by_id("docIssuanceDate").send_keys("05.01.2010")
        driver.find_element_by_id("docIssuanceDate").clear()
        driver.find_element_by_id("docIssuanceDate").send_keys("05.01.2010")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[9]/following::div[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Selecionar...'])[4]/following::div[7]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[10]/following::div[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Solteiro(a)'])[1]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[11]/following::div[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Entre R$10,000 e R$50,000'])[1]/following::div[3]").click()
        driver.find_element_by_id("zipCode").click()
        driver.find_element_by_id("zipCode").clear()
        driver.find_element_by_id("zipCode").send_keys("35242342")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[13]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Selecionar...'])[7]/following::div[7]").click()
        driver.find_element_by_id("city").click()
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Copacabana")
        driver.find_element_by_id("street").click()
        driver.find_element_by_id("street").clear()
        driver.find_element_by_id("street").send_keys("1")
        driver.find_element_by_id("houseNumber").click()
        driver.find_element_by_id("houseNumber").clear()
        driver.find_element_by_id("houseNumber").send_keys("2")
        driver.find_element_by_id("neighborhood").click()
        driver.find_element_by_id("neighborhood").clear()
        driver.find_element_by_id("neighborhood").send_keys("a")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Tipo de residência'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Moro com meus Pais'])[1]/following::div[3]").click()
        driver.find_element_by_name("nextBtn").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

######################################################################################step3

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BRRegistrationStep3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_b_r_registration_step3(self):
        driver = self.driver
        driver.get("https://qa-delivery-br-master.moneyman.ru/registration-gf/static/#/step3")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::div[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Ensino Médio'])[1]/following::div[3]").click()
        driver.find_element_by_id("attestedIncome").click()
        driver.find_element_by_id("attestedIncome").clear()
        driver.find_element_by_id("attestedIncome").send_keys("20.000,00")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[3]/following::div[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Funcionário com carteira assinada (CLT)'])[1]/following::div[3]").click()
        driver.find_element_by_id("company").click()
        driver.find_element_by_id("company").clear()
        driver.find_element_by_id("company").send_keys("ArmyOfBrasil")
        driver.find_element_by_id("workPhone").click()
        driver.find_element_by_id("workPhone").clear()
        driver.find_element_by_id("workPhone").send_keys("(10)256642342")
        driver.find_element_by_id("workPhone").clear()
        driver.find_element_by_id("workPhone").send_keys("(10)256642342")
        driver.find_element_by_id("nextSalaryDate").click()
        driver.find_element_by_id("nextSalaryDate").clear()
        driver.find_element_by_id("nextSalaryDate").send_keys("26.09.2018")
        driver.find_element_by_id("nextSalaryDate").clear()
        driver.find_element_by_id("nextSalaryDate").send_keys("26.09.2018")
        driver.find_element_by_id("nextSalaryDate").clear()
        driver.find_element_by_id("nextSalaryDate").send_keys("26.09.2018")
        driver.find_element_by_id("nextSalaryDate").clear()
        driver.find_element_by_id("nextSalaryDate").send_keys("26.09.2018")
        driver.find_element_by_id("monthlyExpenses").click()
        driver.find_element_by_id("monthlyExpenses").clear()
        driver.find_element_by_id("monthlyExpenses").send_keys("2.000,00")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[5]/following::div[4]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Tirar férias'])[1]/following::div[3]").click()
        driver.find_element_by_name("nextBtn").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


######################################################################################step4