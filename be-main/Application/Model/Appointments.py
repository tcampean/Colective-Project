from Application.Utils.user_utils import get_user_name, get_doctor_name
from Application.database import database


class Appointments(database.Model):
    __tablename__ = "Appointments"
    __table_args__ = {'extend_existing': True}

    id_appointment = database.Column(database.Integer, primary_key=True)
    patient_id = database.Column(database.String, database.ForeignKey('Patients.cnp_patient'))
    doctor_id = database.Column(database.String, database.ForeignKey('Doctors.id_doctor'))
    location = database.Column(database.String, nullable=False)
    date = database.Column(database.Date, nullable=False)
    time = database.Column(database.Time, nullable=False)
    type = database.Column(database.String, nullable=False)

    def __init__(self, patient_id, doctor_name, location, appointment_date, appointment_time, appointment_type):
        self.patient_id = patient_id
        self.doctor_id = doctor_name
        self.location = location
        self.date = appointment_date
        self.time = appointment_time
        self.type = appointment_type

    def __str__(self):
        return str(self.id_appointment) + "," + str(self.patient_id) + "," + self.doctor_id + "," + self.location + "," + str(self.date) + "," + str(self.time) + "," + self.type

    def __repr__(self):
        return str(self.id_appointment) + "," + str(self.patient_id) + "," + self.doctor_id + "," + self.location + "," + str(self.date) + "," + str(self.time) + "," + self.type

    def get_id(self):
        return self.id_appointment

    def serialize(self):
        return {
            "id_appointment": str(self.id_appointment),
            "patient_name": get_user_name(self.patient_id),
            "patient_cnp": self.patient_id,
            "doctor_name": get_doctor_name(self.doctor_id),
            "location": self.location,
            "date": str(self.date),
            "time": str(self.time),
            "type": self.type
        }
