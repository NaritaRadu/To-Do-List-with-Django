from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_todo_list(self):
        # Stan has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get("http://localhost:8000")
        
        # He notices the page title and header mention to-do lists
        self.assertIn("To-Do",self.browser.title)
        # He is invited to enter a to-do item straight away
        self.fail("Finish the test!")
    
if __name__=='__main__':
    unittest.main()
