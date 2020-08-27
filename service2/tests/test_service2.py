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

class TestService2(TestBase):
    #check if the author returned is in the list of authors
    #line 13-15 routes.py
    def test_getanimal(self):
        response = self.client.get(url_for('get_author'))
        check = False
        for item in ['Albert Einstein','Walt Disney','Winston Churchill',
                'Nelson Mandela','Henry Ford','George Addair','Amelia Earhart',
                'Vincent Van Gogh','Confucius','Francis of Assisi','Denzel Washington',
                'Theodore Roosevelt','Pele','Michelangelo']:
            if bytes.decode(response.data) == item:
                check = True
        self.assertTrue(check)
