from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class InputOptions(BasePage):

    url = 'https://www.immediateannuities.com/'

    def age(self):
        locator = Locator(By.XPATH,"//select[@name='age']")
        element = BaseElement(self.driver,locator=locator)
        return element.get_option_list()

    def gender(self):
        locator = Locator(By.XPATH,"//select[@name='gender']")
        element = BaseElement(self.driver,locator=locator)
        return element.get_option_list()

    def state(self):
        locator = Locator(By.XPATH,"//select[@name='state']")
        element = BaseElement(self.driver,locator=locator)
        return element.get_option_list()

    def income_start(self):
        locator = Locator(By.CSS_SELECTOR,"#income_start_date")
        element = BaseElement(self.driver,locator=locator)
        return element.get_option_list()


class AnnuityPremium(BasePage):

    url = 'https://www.immediateannuities.com/'

    def age(self,age_input):
        locator = Locator(By.XPATH,"//select[@name='age']")
        element = BaseElement(self.driver,locator=locator)
        element.select(age_input)
        return None

    def gender(self,gender_input):
        locator = Locator(By.XPATH,"//select[@name='gender']")
        element = BaseElement(self.driver,locator=locator)
        element.select(gender_input)
        return None

    def state(self,state_input):
        locator = Locator(By.XPATH,"//select[@name='state']")
        element = BaseElement(self.driver,locator=locator)
        element.select(state_input)
        return None


    def income_start(self,income_start_input):
        locator = Locator(By.CSS_SELECTOR,"#income_start_date")
        element = BaseElement(self.driver,locator=locator)
        element.select(income_start_input)
        return None


    def premium(self,premium_input):
        locator = Locator(By.CSS_SELECTOR,"#premium")
        element = BaseElement(self.driver,locator=locator)
        element.input_text(premium_input)
        return None


    def submit(self):
        locator = Locator(By.CSS_SELECTOR,'#calc-submit > input')
        element = BaseElement(self.driver,locator=locator)
        element.click()
        return None


    def output(self,row):
        locator = Locator(By.CSS_SELECTOR,f'.ar-annuity-table-main tbody tr:nth-of-type({row}) td:nth-of-type(3)')
        element = BaseElement(self.driver,locator=locator)
        return element.text()





    