import math

from Application.Model.Doctors import Doctors
from Application.Utils import constants
from sqlalchemy import or_, desc


def paginate(doctors, query):
    try:
        page_position = query.get("page")
        if page_position:
            page = int(page_position)
            return doctors[(page - 1) * constants.pagesize: (page - 1) * constants.pagesize + constants.pagesize]
    except:
        return doctors
    return doctors

def query_field_parameters(doctors, query):
    first_name = query.get("first_name")
    if first_name:
        doctors = doctors.filter_by(first_name=first_name)

    last_name = query.get("last_name")
    if last_name:
        doctors = doctors.filter_by(last_name=last_name)

    specialization = query.get("specialization")
    if specialization:
        doctors = doctors.filter_by(specialization=specialization)

    hospital = query.get("hospital")
    if hospital:
        doctors = doctors.filter_by(hospital=hospital)

    position = query.get("position")
    if hospital:
        doctors = doctors.filter_by(position=position)

    return doctors


def search_fields(position, query):
    search = query.get("search")
    if search:
        position = position.filter(
            or_(Doctors.full_name.contains(search),
                Doctors.specialization.contains(search),
                Doctors.hospital.contains(search),
                Doctors.position.contains(search)))
    return position


def determine_sort_field(doctors, query):
    sort_field = query.get("sortField")
    match sort_field:
        case "nameField":
            return sort_name(doctors, query)
        case "specializationField":
            return sort_specialization(doctors, query)
        case "hospitalField":
            return sort_hospital(doctors, query)
        case "positionField":
            return sort_position(doctors, query)
    return doctors


def sort_name(doctors, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            doctors = doctors.order_by(Doctors.first_name, Doctors.last_name)
        else:
            doctors = doctors.order_by(desc(Doctors.first_name), desc(Doctors.last_name))
    return doctors


def sort_specialization(doctors, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            doctors = doctors.order_by(Doctors.specialization)
        else:
            doctors = doctors.order_by(desc(Doctors.specialization))
    return doctors


def sort_hospital(doctors, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            doctors = doctors.order_by(Doctors.hospital)
        else:
            doctors = doctors.order_by(desc(Doctors.hospital))
    return doctors


def sort_position(doctors, query):
    sort = query.get("sortMode")
    if sort:
        if sort == "ASC":
            doctors = doctors.order_by(Doctors.position)
        else:
            doctors = doctors.order_by(desc(Doctors.position))
    return doctors


def get_total_of_pages(doctors):
    return math.ceil(doctors.count() / constants.pagesize)
