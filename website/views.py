from flask import Blueprint, request, render_template, jsonify
from .models import Measurment
from . import db
from .solar_tracking import getAngle

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("base.html")
    


@views.route('/time', methods=["GET", "POST"])
def get_angle():
    if request.method == "GET":
        return (getAngle())
    


@views.route('/measurments', methods=["GET", "POST"])
def get_data():
    if request.method == 'GET':     
        measurements = Measurment.query.all()
        return render_template('measurments.html', measurements=measurements)
    
    if request.method == 'POST':
        data = request.get_data().decode('utf-8')
        new_meas = Measurment(data=data)
        db.session.add(new_meas)
        db.session.commit()
        return 'Data added'