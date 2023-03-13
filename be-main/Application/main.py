
from flask_cors import CORS
from Application.app import app
from Application.diagnostic_routes import diagnostics_api
from Application.doctors_routes import doctorapi
from Application.login_routes import login_api

from Application.patient_routes import patients_api
from Application.appointment_routes import appointments_api

app.register_blueprint(patients_api)
app.register_blueprint(appointments_api)
app.register_blueprint(diagnostics_api)
app.register_blueprint(doctorapi)
app.register_blueprint(login_api)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    app.run(debug=True)