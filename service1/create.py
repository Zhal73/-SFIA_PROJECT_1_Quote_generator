# import the SQLAlchemy instance
from application import db


from application.models import all_quotes
db.drop_all()

db.create_all()
