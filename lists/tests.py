from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_root_url_resolves_tohome_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))

# Create your tests here.

# class SmokeTest(TestCase):
    # '''тест на токсичность'''
    
    # def test_bad_math(self):
        # ''' тест: не правильные матемвтические расчеты '''
        # self.assertEqual(1+1,3)

