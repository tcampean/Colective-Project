from sqlalchemy.ext.hybrid import hybrid_property

from Application.database import database


class Patients(database.Model):
    __tablename__ = "Patients"
    __table_args__ = {'extend_existing': True}

    cnp_patient = database.Column(database.String, primary_key=True)
    email = database.Column(database.String, nullable=False)
    password = database.Column(database.String, nullable=False)
    first_name = database.Column(database.String, nullable=False)
    last_name = database.Column(database.String, nullable=False)
    address = database.Column(database.String, nullable=False)
    city = database.Column(database.String, nullable=False)
    county = database.Column(database.String, nullable=False)
    country = database.Column(database.String, nullable=False)
    date_of_birth = database.Column(database.Date, nullable=False)

    def __init__(self, cnp_patient, email, password, first_name, last_name, address, city, county, country, date_of_birth):
        self.cnp_patient = cnp_patient
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.county = county
        self.country = country
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.cnp_patient + "," + self.email + "," + self.password + "," + self.first_name + "," + self.last_name + "," + self.address + "," + self.city + "," + self.county + "," + self.country + "," + str(self.date_of_birth)

    def __repr__(self):
        return self.cnp_patient + "," + self.email + "," + self.password + "," + self.first_name + "," + self.last_name + "," + self.address + "," + self.city + "," + self.county + "," + self.country + "," + str(self.date_of_birth)

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def get_id(self):
        return str(self.cnp_patient)

    def serialize(self):
        return {
            "cnp_patient": self.cnp_patient,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "city": self.city,
            "county": self.county,
            "country": self.country,
            "date_of_birth": str(self.date_of_birth)
        }
