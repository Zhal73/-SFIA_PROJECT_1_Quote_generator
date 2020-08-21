# import render_template, url_for and request functions from the flask module
from flask import request,Response
import requests
# import the app object from the ./application/__init__.py
from application import app
#import the random function to generate a random number
import random


#generates a the name of a random author 
@app.route('/get_author',methods=['GET'])
def get_author():
    authors = ['Albert Einstein','Walt Disney','Winston Churchill','Nelson Mandela','Henry Ford','George Addair','Amelia Earhart','Vincent Van Gogh','Confucius','Francis of Assisi','Denzel Washington','Theodore Roosevelt','Pele','Michelangelo']
    author = authors[random.randrange(14)]
    return Response(author,mimetype='text/plain')

