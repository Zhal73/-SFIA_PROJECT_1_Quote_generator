from unittest.mock import patch
import unittest
import requests

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
    
class TestService4(TestBase):
    def test_genuinity1(self):
        with patch('requests.get') as g:
              #  ppp=json.dumps({'Albert Einstein': 'In the middle of difficulty lies opportunity.'})
            #g.return_value=ppp
              #  response = self.client.post(url_for('get_genuinity'),data=g.return_value,content_type='application/json')
            response = self.client.post(url_for('get_genuinity'),json={'Albert Einstein': 'In the middle of difficulty lies opportunity.'})
            self.assertIn(b'Awsome!!! This is a pearl of wisdom', response.data)

    def test_genuinity2(self):
        with patch('requests.get') as g:
              #  ppp=json.dumps({'Confucius': 'In the middle of difficulty lies opportunity.'})
            #g.return_value=ppp
              #  response = self.client.post(url_for('get_genuinity'),data=g.return_value,content_type='application/json')
            response = self.client.post(url_for('get_genuinity'),json={'Confucius': 'In the middle of difficulty lies opportunity.'})
            self.assertIn(b'Not quite! But is still a good one!!!', response.data)
