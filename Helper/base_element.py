from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BaseElement(object):
    
    def __init__ (self,driver,locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(
            self.driver,10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self,txt):
        self.web_element.clear()
        self.web_element.send_keys(txt)
        return None

    def click(self):
        self.web_element.click()
        return None

    def select(self,option_name):
        Select(self.web_element).select_by_visible_text(option_name)
        return None

    def get_option_list(self):
        options_text = [x.text for x in self.web_element.find_elements_by_tag_name("option")]
        options_value = [x.get_attribute("value") for x in self.web_element.find_elements_by_tag_name("option")]
        return {'value':options_value,'text':options_text}

    def attribute(self,attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def text(self):
        text = self.web_element.text
        return text

    
    

    
    
