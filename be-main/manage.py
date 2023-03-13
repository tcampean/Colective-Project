import datetime
from datetime import date, time, timedelta

import bcrypt

from Application.Model import Diagnostic


def deploy():
    from Application.app import app
    from Application.database import database
    from Application.Model import Appointments, Patients
    from Application.Model.Doctors import Doctors
    from Application.Model.Appointments import Appointments

    app.app_context().push()
    database.create_all()

    database.session.add(
        Patients.Patients("1", "mihaivasile@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Mihai Alexandru", "Vasile", "Str. Observatorului nr. 15", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1970, 8, 23)))

    database.session.add(
        Patients.Patients("2", "mihaelamaria23@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Mihaela", "Maria", "Str. Observatorului nr. 7", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1988, 9, 21)))

    database.session.add(
        Patients.Patients("3", "andreeamaria@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Andreea", "Maria", "Str. Bucegi nr. 23", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1955, 2, 22)))

    database.session.add(
        Patients.Patients("4", "larisamarian@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Larisa", "Marian", "Str. Bucegi nr. 55", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1940, 5, 12)))

    database.session.add(
        Patients.Patients("5", "alexandraiulia@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Alexandra", "Iulia", "Str. Observatorului nr. 44", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1910, 9, 22)))

    database.session.add(
        Patients.Patients("6", "vladimirinocentiu@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Vladimir", "Inocentiu", "Str. Vasile Alecsandri nr. 22", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1999, 4, 23)))

    database.session.add(
        Patients.Patients("7", "anamariapatrova@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Anamaria", "Patrova", "Str. Vasile Alecsandri nr. 25", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1999, 4, 23)))

    database.session.add(
        Patients.Patients("8", "ellenhelen@gmail.com", str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())),
                          "Ellen", "Helen", "Str. ", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date(1922, 4, 23)))

    database.session.add(Appointments("1", "D5", "Johns Hopkins Hospital", date(2023, 1, 27), time(10), "Consult"))
    database.session.add(Appointments("1", "D8", "Mayo Clinic", date(2023, 1, 20), time(11), "Oncology"))
    database.session.add(Appointments("1", "D10", "Duke University Hospital", date(2023, 1, 24), time(12), "Urology"))
    database.session.add(
        Appointments("1", "D11", "University of Chicago Medicine", date(2023, 1, 29), time(13), "Ophthalmology"))
    database.session.add(
        Appointments("1", "D8", "Mayo Clinic", date(2023, 3, 29), time(13), "Oncology"))
    database.session.add(
        Appointments("1", "D14", "Mayo Clinic", date(2023, 4, 29), time(13), "Endocrinology"))
    database.session.add(
        Appointments("1", "D12", "Mayo Clinic", date(2023, 4, 29), time(13), "Rheumatology"))

    database.session.add(Appointments("2", "D6", "Cleveland Clinic", date(2023, 1, 25), time(11), "Orthopedics"))
    database.session.add(
        Appointments("2", "D7", "New York Presbyterian Hospital", date(2023, 1, 25), time(10), "Neurology"))
    database.session.add(
        Appointments("2", "D9", "University of Pittsburgh Medical Center", date(2023, 1, 24), time(11), "Cardiology"))
    database.session.add(
        Appointments("2", "D12", "University of California, Los Angeles Medical Center", date(2023, 1, 25), time(12),
                     "Rheumatology"))
    database.session.add(
        Appointments("2", "D8", "University of California, Los Angeles Medical Center", date(2023, 7, 25), time(12),
                     "Oncology"))

    database.session.add(
        Appointments("3", "D7", "Massachusetts General Hospital", date(2023, 1, 23), time(12), "Neurology"))
    database.session.add(Appointments("3", "D5", "Barnes-Jewish Hospital", date(2023, 3, 1), time(14), "Surgery"))
    database.session.add(
        Appointments("3", "D8", "Brigham and Women's Hospital", date(2023, 1, 28), time(15), "Oncology"))
    database.session.add(
        Appointments("3", "D11", "Dana-Farber Cancer Institute", date(2023, 1, 26), time(16), "Ophthalmology"))
    database.session.add(
        Appointments("3", "D12", "Boston Children's Hospital", date(2023, 1, 29), time(17), "Rheumatology"))

    database.session.add(
        Appointments("4", "D8", "Memorial Sloan Kettering Cancer Center", date(2023, 1, 23), time(13), "Oncology"))
    today = date.today()
    database.session.add(
        Appointments("4", "D5", "University of Texas MD Anderson Cancer Center", today + timedelta(days=1), time(9),
                     "Surgery"))
    database.session.add(
        Appointments("4", "D8", "Cedars-Sinai Medical Center", today + timedelta(days=2), time(10), "Oncology"))
    database.session.add(
        Appointments("4", "D11", "Keck Medicine of USC", today + timedelta(days=3), time(11), "Ophthalmology"))
    database.session.add(
        Appointments("4", "D12", "University of Alabama at Birmingham Hospital", today + timedelta(days=4), time(12),
                     "Rheumatology"))

    database.session.add(
        Appointments("5", "D9", "Christiana Care Health System", date(2023, 1, 24), time(14), "Cardiology"))
    database.session.add(
        Appointments("5", "D6", "University of California, San Francisco Medical Center", today + timedelta(days=5),
                     time(9), "Orthopedics"))
    database.session.add(
        Appointments("5", "D7", "Stanford Health Care", today + timedelta(days=6), time(10), "Neurology"))
    database.session.add(
        Appointments("5", "D9", "University of Utah Hospitals and Clinics", today + timedelta(days=7), time(11),
                     "Cardiology"))
    database.session.add(
        Appointments("5", "D12", "University of Iowa Hospitals and Clinics", today + timedelta(days=8), time(12),
                     "Rheumatology"))

    database.session.add(
        Appointments("6", "D10", "University of Michigan Health System", date(2023, 1, 22), time(15), "Urology"))
    database.session.add(
        Appointments("6", "D5", "University of Washington Medical Center", today + timedelta(days=9), time(9),
                     "Surgery"))
    database.session.add(
        Appointments("6", "D8", "University of Virginia Medical Center", today + timedelta(days=10), time(10),
                     "Oncology"))
    database.session.add(
        Appointments("6", "D11", "Vanderbilt University Medical Center", today + timedelta(days=11), time(11),
                     "Ophthalmology"))
    database.session.add(
        Appointments("6", "D12", "University of Texas Southwestern Medical Center", today + timedelta(days=12),
                     time(12), "Rheumatology"))

    database.session.add(
        Appointments("7", "D11", "Bascom Palmer Eye Institute", date(2023, 1, 28), time(16), "Ophthalmology"))
    database.session.add(
        Appointments("7", "D13", "University of Kansas Medical Center", today + timedelta(days=3), time(9),
                     "Anesthesiology"))
    database.session.add(
        Appointments("7", "D14", "University of Kentucky Chandler Medical Center", today + timedelta(days=2), time(10),
                     "Dermatology"))
    database.session.add(
        Appointments("7", "D5", "University of Kansas Medical Center", today + timedelta(days=5), time(11), "Surgery"))
    database.session.add(
        Appointments("7", "D8", "University of Virginia Medical Center", today + timedelta(days=6), time(12),
                     "Oncology"))

    database.session.add(
        Appointments("8", "D12", "Hospital for Special Surgery", date(2023, 1, 30), time(17), "Rheumatology"))
    database.session.add(
        Appointments("8", "D6", "University of California, San Francisco Medical Center", today + timedelta(days=7),
                     time(9), "Orthopedics"))
    database.session.add(
        Appointments("8", "D7", "Stanford Health Care", today + timedelta(days=5), time(10), "Neurology"))
    database.session.add(
        Appointments("8", "D9", "University of Utah Hospitals and Clinics", today + timedelta(days=6), time(11),
                     "Cardiology"))
    database.session.add(
        Appointments("8", "D12", "University of Iowa Hospitals and Clinics", today + timedelta(days=4), time(12),
                     "Rheumatology"))
    database.session.add(
        Appointments("8", "D8", "Brigham and Women's Hospital", date(2023, 10, 28), time(15), "Oncology"))


    database.session.add(
       Diagnostic.Diagnostic(2, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning", date(2023, 1, 20), date(2023, 3, 23), 1))

    database.session.add(
        Diagnostic.Diagnostic(5, "Voltaren EMULGEL 200mg before bed", date(2023, 1, 25), date(2023, 6, 25), 0))

    database.session.add(
        Diagnostic.Diagnostic(5, "Epilepsy pills 1 in the morning, 1 at night, for 1 month",  date(2023, 1, 23), date(2023, 9, 20), 1))


    database.session.add(Doctors("D5", "Joshua", "Jones", "joshua.jones@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Gastroenterology",
                                 "Mayo Clinic", "Specialist"))
    database.session.add(Doctors("D6", "Ashley", "Miller", "ashley.miller@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Orthopedics",
                                 "Cleveland Clinic", "Surgeon"))
    database.session.add(Doctors("D7", "Jacob", "Taylor", "jacob.taylor@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Neurology",
                                 "Massachusetts General Hospital", "Specialist"))
    database.session.add(Doctors("D8", "Michael", "Thomas", "michael.thomas@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Oncology",
                                 "Memorial Sloan Kettering Cancer Center", "Oncologist"))
    database.session.add(Doctors("D9", "Emily", "Moore", "emily.moore@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Cardiology",
                                 "Christiana Care Health System", "Cardiologist"))
    database.session.add(Doctors("D10", "Matthew", "Jackson", "matthew.jackson@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Urology",
                                 "University of Michigan Health System", "Urologist"))
    database.session.add(Doctors("D11", "Olivia", "White", "olivia.white@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Ophthalmology",
                                 "Bascom Palmer Eye Institute", "Ophthalmologist"))
    database.session.add(Doctors("D12", "David", "Harris", "david.harris@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Rheumatology",
                                 "Hospital for Special Surgery", "Rheumatologist"))
    database.session.add(Doctors("D13", "Emily", "Martin", "emily.martin@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Anesthesiology",
                                 "Brigham and Women's Hospital", "Anesthesiologist"))
    database.session.add(Doctors("D14", "Joshua", "Thompson", "joshua.thompson@example.com",
                                 str(bcrypt.hashpw("12345678".encode(), bcrypt.gensalt())), "Endocrinology",
                                 "University of Alabama at Birmingham Hospital", "Endocrinologist"))

    database.session.commit()


deploy()
