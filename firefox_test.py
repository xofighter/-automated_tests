# coding = utf-8
from selenium import webdriver
import unittest

class VisitSougouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\\geckodriver")

    def test_visitSougou(self):
        self.driver.get("http://www.sougou.com")
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
