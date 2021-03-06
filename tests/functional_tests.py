from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage

        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Ender a to-do item'
        )



        # We type "Buy peacock feathers" into a text box (because we like fly fishing)
        inputbox.send_keys('Buy peacock feathers')

        # When we hit ender, the page updates, and now the page lists:
        # 1: Buy peacock feathers. as an item in a to-do list

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )




        # There is sill a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')         


# The page updates again, and now shows both items on the list

# We wonder whether the site will remember our list. Then we see that the
# site has generated a uniqu URL for her -- thereis some explanatory text to
# that effect.

# She visits that URL -  her to-do list is still there.

# Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

