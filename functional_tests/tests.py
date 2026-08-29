from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_can_start_a_todo_list(self):
        # Stan has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get(self.live_server_url)
        
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
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        
       
        # There is still a text box inviting him to add another item
        # He enters " Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        
        #self.fail("Finish the test!")
    
if __name__=='__main__':
    unittest.main()
