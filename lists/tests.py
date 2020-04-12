from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_root_url_resolves_tohome_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
# Create your tests here.

# class SmokeTest(TestCase):
    # '''тест на токсичность'''
    
    # def test_bad_math(self):
        # ''' тест: не правильные матемвтические расчеты '''
        # self.assertEqual(1+1,3)

