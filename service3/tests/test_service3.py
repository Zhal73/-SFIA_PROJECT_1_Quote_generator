from unittest.mock import patch
  
from flask import url_for
from flask_testing import TestCase
from application import app
class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
class TestService3(TestBase):
    #check if the quote returned is in the list of quotes
    #line 13-28 of routes.py
    def test_getanimal(self):
        response = self.client.get(url_for('get_quote'))
        check = False
        for item in ['Not everyone can become a great artist, but a great artist can come from anywhere.',
            'There is no greater gift than friendship.',
            'To laugh at yourself, is to love yourself.',
            '"All it takes is little faith and trust.']:
            if bytes.decode(response.data) == item:
                check = True
        self.assertTrue(check)
