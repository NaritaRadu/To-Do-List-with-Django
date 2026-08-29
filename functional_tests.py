from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
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
        header_text=self.browser.find_element(By.TAG_NAME,"h1").text
        self.assertIn("To-Do",header_text)
        # He is invited to enter a to-do item straight away
        inputbox=self.browser.find_element(By.ID,"id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"),"Enter a to-do item")
        inputbox.send_keys("Buy peacock feathers")
        # When he hits enter,the page updates, and now the page 
        # lists "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table=self.browser.find_element(By.ID,"id_list_table")
        rows=table.find_elements(By.TAG_NAME,"tr")
        self.assertIn(
        "2: Use peacock feathers to make a fly",
        [row.text for row in rows],
    )
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        # There is still a text box inviting him to add another item
        # He enters " Use peacock feathers to make a fly"
        
        self.fail("Finish the test!")
    
if __name__=='__main__':
    unittest.main()
