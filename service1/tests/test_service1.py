import requests
import unittest
from unittest.mock import patch
import requests_mock
  
from flask import url_for
from flask_testing import TestCase
from application import app,db
from application.models import all_quotes
from os import getenv


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        quote=all_quotes(author="Albert Einsten", quote="In the middle of difficulty lies opportunity", genuinity ="Awsome!!! This is a pearl of wisdom")

        db.session.add(quote)
        db.session.commit()


    def tearDown(self):

        db.session.remove()
        db.drop_all()

   

##### TESTS IMPLEMENTATION  ########
class TestService1(TestBase):
    def test_home_page(self):
        #check if the home page is accessible
        #line 13 routes.py
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_generate_quote(self):
        with self.client:
            with requests_mock.Mocker() as m:
                m.get('http://service2:5001/get_author', text='Albert Einsten')
                m.get('http://service3:5002/get_quote', text='In the middle of difficulty lies opportunity.')
                m.post('http://service4:5003/get_genuinity', text='Awsome!!! This is a pearl of wisdom')                
                resp = self.client.get(url_for('generate_quote'))
                self.assertEqual(resp.status_code, 200)

"""

    def test_generate_quotes(self):
        with patch('requests.get') as a:
            a.return_value.text = "Albert Einstein"
            with patch('requests.get') as q:
                q.return_value.text = "In the middle of difficulty lies opportunity."
                with patch('requests.post') as p:
                    p.return_value.text = "Awsome!!! This is a pearl of wisdom"

                    response = self.client.get(url_for('generate_quote'))
                    self.assertIn(b'Albert Einstein', response.data)
                    self.assertIn(b'In the middle of difficulty lies opportunity.', response.data)
                    self.assertIn(b'Awsome!!! This is a pearl of wisdom', response.data)
                    self.assertEqual(response.status_code, 200)
"""

