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
    quotes = ['Not everyone can become a great artist, but a great artist can come from anywhere.',
            'There is no greater gift than friendship.',
            'To laugh at yourself, is to love yourself.',
            '"All it takes is little faith and trust.']
    quote = quotes[random.randrange(4)]
    return Response(quote,mimetype='text/plain')

