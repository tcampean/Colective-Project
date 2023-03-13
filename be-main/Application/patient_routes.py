import datetime

from flask import request, Blueprint, make_response

from Application.Model.Patients import Patients
from Application.database import database
from flask import jsonify
from flask_cors import cross_origin

patients_api = Blueprint('patients_api', __name__)

@cross_origin()
@patients_api.route('/patient/<cnp>', methods=["GET", "PUT", "OPTIONS"])
def patient_home(cnp):
    if request.method == "GET":
        patient = Patients.query.filter_by(cnp_patient=cnp).first()
        return jsonify(patient.serialize())

    elif request.method == "PUT":
        new_patient = request.json
        patient = Patients.query.filter_by(cnp_patient=cnp).first()
        patient.first_name = new_patient["first_name"]
        patient.last_name = new_patient["last_name"]
        patient.address = new_patient["address"]
        patient.city = new_patient["city"]
        patient.county = new_patient["county"]
        patient.country = new_patient["country"]
        database.session.commit()
        return _corsify_actual_response(jsonify(request.json)), 200

    elif request.method == "OPTIONS":
        return _build_cors_preflight_response()


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response