#import the db instance
from application import db

#creates a table to save the pair animal-noise
class all_quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable = False)
    quote = db.Column(db.String(300), nullable = False)
    genuinity = db.Column(db.String(100), nullable = False)
