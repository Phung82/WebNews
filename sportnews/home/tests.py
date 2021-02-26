#from django.test import TestCase

# Create your tests here.
from django.test import TestCase, SimpleTestCase
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        respone = self.client.get('/')
        self.assertEquals(respone.status_code,200)