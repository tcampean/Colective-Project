import datetime

from flask import request, jsonify, Blueprint, make_response
from flask_cors import cross_origin, CORS
from sqlalchemy import and_, not_

from Application.Model.Appointments import Appointments
from Application.Model.Doctors import Doctors
from Application.Model.Metadata import Metadata
from Application.Model.Response import Response
from Application.Utils.appointments_query_utils import appointments_by_user, query_field_parameters, search_fields, \
    determine_sort_field, paginate, get_total_of_pages
from Application.Utils.user_utils import get_patient_from_name
from Application.database import database

appointments_api = Blueprint('appointments_api', __name__)


@cross_origin()
@appointments_api.route('/appointments/', methods=["GET", "POST", "OPTIONS"])
def index():
    if request.method == "GET":
        query = request.args
        user_appointments = appointments_by_user(Appointments.query, query)
        filtered_appointments = query_field_parameters(user_appointments, query)
        searched_appointments = search_fields(filtered_appointments, query)
        sorted_appointments = determine_sort_field(searched_appointments, query)
        paginated_appointments = paginate(sorted_appointments, query)
        response = Response(Metadata(get_total_of_pages(sorted_appointments)), paginated_appointments)

        return jsonify(response.serialize())

    elif request.method == "POST":
        new_appointment = request.json
        appointment = ""
        if new_appointment["user_type"] == "doctor":
            patient_id = get_patient_from_name(new_appointment["patient_name"]).cnp_patient
            appointment = Appointments(patient_id, new_appointment["token"], new_appointment["location"], datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(new_appointment['time'], '%H:%M').time(), new_appointment["type"])

        if new_appointment["user_type"] == "patient":
            try:
                busy_doctors = Appointments.query.with_entities(Appointments.doctor_id).filter(and_(Appointments.date == datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date(), Appointments.time == datetime.datetime.strptime(new_appointment['time'], '%H:%M').time())).distinct().all()
                busy_doctors_list = [doc for (doc,) in busy_doctors]
                doctor_id = Doctors.query.filter(Doctors.specialization == new_appointment["type"], Doctors.id_doctor.not_in(busy_doctors_list)).first().get_id()
                appointment = Appointments(new_appointment["token"], doctor_id, new_appointment["location"], datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date(),
                                       datetime.datetime.strptime(new_appointment['time'], '%H:%M').time(), new_appointment["type"])
            except:
                return make_response("No doctor available", 400)

        database.session.add(appointment)
        database.session.commit()
        return _corsify_actual_response(jsonify(request.json)), 200

    elif request.method == "OPTIONS":
        return _build_cors_preflight_response()

@cross_origin()
@appointments_api.route('/appointments/<id>', methods=["DELETE", "PUT", "OPTIONS"])
def index2(id):
    if request.method == "DELETE":
        Appointments.query.filter_by(id_appointment=int(id)).delete()
        database.session.commit()
        return jsonify(request.json), 200

    elif request.method == "PUT":
        new_appointment = request.json
        appointment = Appointments.query.filter_by(id_appointment=id).first()
        appointment.location = new_appointment["location"]
        appointment.date = datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date()
        appointment.time = datetime.datetime.strptime(new_appointment['time'], '%H:%M').time()
        appointment.type = new_appointment["type"]
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