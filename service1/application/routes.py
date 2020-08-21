# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request, jsonify
import requests
# import the app object from the ./application/__init__.py
from application import app,db

from application.models import all_quotes

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/generate_quote',methods=['GET','POST'])
def generate_quote():
    author = requests.get('http://service2:5001/get_author')
    quote = requests.get('http://service3:5002/get_quote')
    genuinity = requests.post('http://service4:5003/get_genuinity',json={author.text: quote.text})
    
    db_data = all_quotes(author=author.text,quote=quote.text,genuinity=genuinity.text)
    db.session.add(db_data)
    db.session.commit()
    quote_record=all_quotes.query.all()
    
    return render_template('generate_quote.html',title='Quote Generator',data1=author.text,data2=quote.text,data3=genuinity.text,posts=quote_record)
