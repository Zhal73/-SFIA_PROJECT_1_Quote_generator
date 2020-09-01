# import render_template, url_for and request functions from the flask module
from flask import request,Response,jsonify
import requests
# import the app object from the ./application/__init__.py
from application import app
#import the random function to generate a random number
import random

#generates a the name of a random author 
@app.route('/get_genuinity',methods=['GET','POST'])
def get_genuinity():
    
    quotes = {
        "Anton Ego in Ratatouille": "Not everyone can become a great artist, but a great artist can come from anywhere.",
        "Santa Claus in The Polar Express": "There is no greater gift than friendship.",
        "Mickey Mouse" : "To laugh at yourself, is to love yourself.",
        "Peter Pan": "All it takes is little faith and trust.",
    }
    #retrieves the json data sent from service1
    data_sent = request.get_json()
    #create a list containing the author sent by service1
    author = data_sent.keys()
    #create a list containing the quote sent by service1
    quote = data_sent.values()
    
    #checks if the quote is genuine and prepares an appropriate response
    for key in author:
        for value in quote:
            if quotes[key] == value:
                data_returned = "Awsome!!! This is a pearl of wisdom"
            else:
                data_returned = "Not quite! But is still a good one!!!"
    
    return Response(data_returned, mimetype='text/plain') 
