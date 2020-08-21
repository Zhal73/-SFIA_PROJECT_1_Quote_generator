# import render_template, url_for and request functions from the flask module
from flask import request,Response
import requests
# import the app object from the ./application/__init__.py
from application import app
#import the random function to generate a random number
import random


#generates a random quote from a list of quotes 
@app.route('/get_quote',methods=['GET'])
def get_quote():
    quotes = ['In the middle of difficulty lies opportunity.',
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
            'The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.']
    quote = quotes[random.randrange(14)]
    return Response(quote,mimetype='text/plain')

