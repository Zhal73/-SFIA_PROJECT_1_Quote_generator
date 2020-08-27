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
        for item in ['In the middle of difficulty lies opportunity.',
            'The way to get started is to quit talking and begin doing.',
            'The pessimist sees difficulty in every opportunity. the optimist sees opportunity in every difficulty.',
            'A winner is a dreamer who never gives up.',
            'Whether you think you can or you think you can not, you are right.',
            'Everything great you can ever wanted is on the other side of your fear.',
            'The most difficult thing is the decision to act, the rest is merely tenacity.',
            'If you hear a voice within you say -you cannot paint!- then by all means paint and that voice will be silenced.',
            'Our greatest glory is not in never falling, but in rising every time we fall.',
            'Start by doing what is necessary; then do what is possible; and suddenly you are doing the impossible.',
            'Without commitment you never start but  without consistency you never finish.',
            'Believe you can and you are halfway there.',
            'Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.',
            'The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.']:
            if bytes.decode(response.data) == item:
                check = True
        self.assertTrue(check)
