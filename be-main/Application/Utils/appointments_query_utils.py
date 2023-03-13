import datetime
import math

import bcrypt
from sqlalchemy import or_, desc
from Application.Model.Appointments import Appointments
from Application.Model.Doctors import Doctors
from Application.Model.Patients import Patients
from Application.Utils import constants
from Application.Utils.user_utils import is_doctor, get_user_name, get_doctor_name


def appointments_by_user(appointments, query):
    user_id = query.get("id")
    if user_id:
        if query.get("user_type") == "patient":
            appointments = appointments.filter_by(patient_id=user_id)
        else:
            appointments = appointments.filter_by(doctor_id=user_id)

    return appointments

def query_field_parameters(appointments, query):
    patient_name = query.get("patient")
    if patient_name:
        appointments = appointments.filter_by(patient_id=patient_name)

    doctor_name = query.get("doctor")
    if doctor_name:
        appointments = appointments.filter_by(doctor_id=doctor_name)

    location = query.get("location")
    if location:
        appointments = appointments.filter_by(location=location)

    date = query.get("date")
    if date:
        appointments = appointments.filter_by(date=datetime.datetime.strptime(date, '%Y-%m-%d').date())

    time = query.get("time")
    if time:
        appointments = appointments.filter_by(time=datetime.datetime.strptime(time, '%H:%M').time())

    type = query.get("type")
    if type:
        appointments = appointments.filter_by(type=type)

    return appointments


def paginate(appointments, query):
    try:
        page_position = query.get("page")
        if page_position:
            page = int(page_position)
            return appointments[(page - 1) * constants.pagesize: (page - 1) * constants.pagesize + constants.pagesize]
    except:
        return appointments
    return appointments


def get_total_of_pages(appointments):
    return math.ceil(appointments.count() / constants.pagesize)


def search_fields(appointments, query):
    search = query.get("search")
    if search:
        appointments = appointments.join(Doctors).join(Patients).filter(
            or_(Doctors.full_name.contains(search),
                Patients.full_name.contains(search),
                Appointments.location.contains(search),
                Appointments.type.contains(search)))
    return appointments


def determine_sort_field(appointments, query):
    sort_field = query.get("sortField")
    match sort_field:
        case "patientField":
            return sort_patient_name(appointments, query)
        case "doctorField":
            return sort_doctor_name(appointments, query)
        case "locationField":
            return sort_location(appointments, query)
        case "dateField":
            return sort_date(appointments, query)
        case "timeField":
            return sort_time(appointments, query)
        case "typeField":
            return sort_type(appointments, query)
    return appointments


def sort_patient_name(appointments, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            appointments = appointments.join(Patients).order_by(Patients.full_name)
        else:
            appointments = appointments.join(Patients).order_by(desc(Patients.full_name))
    return appointments


def sort_doctor_name(appointments, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            appointments = appointments.join(Doctors).order_by(Doctors.full_name)
        else:
            appointments = appointments.join(Doctors).order_by(desc(Doctors.full_name))
    return appointments


def sort_location(appointments, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.location)
        else:
            appointments = appointments.order_by(desc(Appointments.location))
    return appointments


def sort_date(appointments, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.date)
        else:
            appointments = appointments.order_by(desc(Appointments.date))
    return appointments


def sort_time(appointments, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.time)
        else:
            appointments = appointments.order_by(desc(Appointments.time))
    return appointments


def sort_type(appointments, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.type)
        else:
            appointments = appointments.order_by(desc(Appointments.type))
    return appointments
