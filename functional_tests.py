from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    '''test new visitor'''
    
    def setUp(self):
        # установка 
        #self.browser = webdriver.Chrome()
        #self.browser = webdriver.Firefox(executable_path='D:/Python projects/')
        self.browser = webdriver.Firefox(executable_path='D:/Python projects/geckodriver.exe', firefox_binary='C:/Users/Dad/AppData/Local/Mozilla Firefox/firefox.exe')        
    
    def tearDown(self):
        # демонтаж
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # тест: можно начать список и получить его позже
        self.browser.get('http://localhost:8000')
        
        # Правильные заголовок и шапка окна
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # предложение ввести список
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')#.text
        self.assertTrue(
            any(row.test == '1: Купить павлиньи перья' for row in rows), 
            "New to-do item did not appear in table"
        )
        
        self.fail('Закончить тест!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
##комментарий
