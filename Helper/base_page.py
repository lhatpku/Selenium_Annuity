class BasePage(object):

    url = None

    def __init__(self,driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def back(self):
        self.driver.back()

    