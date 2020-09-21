import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org/")

    def tearDown(self):
        self.driver.close()

if __name__ = "__main__":
    unittest.main()
