from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_todo_list(self):
        # Stan has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get(self.live_server_url)
        
        # He notices the page title and header mention to-do lists
        self.assertIn("To-Do",self.browser.title)
        header_text=self.browser.find_element(By.TAG_NAME,"h1").text
        self.assertIn("To-Do",header_text)
        # He is invited to enter a to-do item straight away
        inputbox=self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute("placeholder"),"Enter a to-do item")
        inputbox.send_keys("Buy peacock feathers")
        # When he hits enter,the page updates, and now the page 
        # lists "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        
       
        # There is still a text box inviting him to add another item
        # He enters " Use peacock feathers to make a fly"
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        
        
        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        
        #self.fail("Finish the test!")
    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox=self.get_item_input_box()
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        
        stan_list_url=self.browser.current_url
        self.assertRegex(stan_list_url,"/lists/.+")
        
        self.browser.delete_all_cookies()
        
        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element(By.TAG_NAME,"body").text
        self.assertNotIn("Buy peacock feathers",page_text)
        
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

    
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, stan_list_url)

    
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)
    
