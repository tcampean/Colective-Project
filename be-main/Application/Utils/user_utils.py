import bcrypt

from Application.Model import Patients, Doctors


def is_doctor(id):
    # if id[0] == "D":
    #     return True
    return False


def get_user_name(id):
    if not is_doctor(id):
        user = Patients.Patients.query.filter_by(cnp_patient=id).first()
        return user.first_name + " " + user.last_name

def get_doctor_name(id):
    user = Doctors.Doctors.query.filter_by(id_doctor=id).first()
    return user.first_name + " " + user.last_name

def get_patient_from_name(name):
    patients = Patients.Patients.query.all()
    for patient in patients:
        if patient.first_name + " " + patient.last_name == name:
            return patient

