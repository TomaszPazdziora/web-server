from flask import Blueprint, request, render_template, jsonify
from .models import Measurement
from . import db
from .solar_tracking import get_angle


views = Blueprint('views', __name__)    

@views.route('/', methods=["GET"])
def hello():
    if request.method == "GET":
        measurements = db.session.query(Measurement).all()
        labels = [m.date.strftime('%H:%M') for m in measurements]
        data = [m.data for m in measurements]

        return render_template("home.html", data=data, labels=labels)
    


@views.route('/angle', methods=["GET"])
def get_ang():
    if request.method == "GET":
        return (get_angle())
    


@views.route('/measurements', methods=["GET", "POST"])
def get_data():
    if request.method == 'GET':     
        meas = Measurement.query.all()
        dates = set(m.date.date() for m in meas)
        for d in dates:
            print(d)
        return render_template('measurements.html', meas=meas, dates=dates)
    
    if request.method == 'POST':
        data = request.get_data().decode('utf-8')
        new_meas = Measurement(data=data)
        db.session.add(new_meas)
        db.session.commit()
        return 'Data added'
    