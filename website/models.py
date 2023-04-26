from . import db
from sqlalchemy.sql import func
import datetime

class Measurment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)