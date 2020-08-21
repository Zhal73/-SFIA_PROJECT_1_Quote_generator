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
        "Albert Einstein": "In the middle of difficulty lies opportunity.",
        "Walt Disney": "The way to get started is to quit talking and begin doing.",
        "Winston Churchill" : "The pessimist sees difficulty in every opportunity. the optimist sees opportunity in every difficulty.",
        "Nelson Mandela": "A winner is a dreamer who never gives up",
        "Henry Ford": "Whether you think you can or you think you can not, you are right.",
        "George Addair": "Everything great you can ever wanted is on the other side of your fear.",
        "Amelia Earhart": "The most difficult thing is the decision to act, the rest is merely tenacity.",
        "Vincent Van Gogh": "If you hear a voice within you say -you cannot paint!- then by all means paint and that voice will be silenced.",
        "Confucius": "Our greatest glory is not in never falling, but in rising every time we fall.",
        "Francis of Assisi": "Start by doing what is necessary; then do what is possible; and suddenly you are doing the impossible.",
        "Denzel Washington": "Without commitment you never start but  without consistency you never finish.",
        "Theodore Roosevelt": "Believe you can and you are halfway there.",
        "Pele": "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.",
        "Michelangelo": "The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it."
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
