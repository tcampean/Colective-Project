import bcrypt
from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin

from Application.Model.Doctors import Doctors
from Application.Model.LoginMeta import LoginMeta
from Application.Model.Patients import Patients
from Application.Model.Response import Response
from Application.Utils.salt_utils import salt

login_api = Blueprint('login_api', __name__)

@cross_origin()
@login_api.route('/login', methods= ["POST", "OPTIONS"])
def amazing_diagnostics():
    if request.method == "POST":
        login_info = request.json
        type = ""
        user = Doctors.query.filter_by(email= login_info["email"]).first()
        if user is None:
            user = Patients.query.filter_by(email= login_info["email"]).first()
            if user is None:
                return make_response("Wrong credentials", 400)
            else:
                type = "patient"
        else:
            type = "doctor"
        encoded_password = str(user.password).encode()

        # Hashing the password
        hash_password = bcrypt.hashpw(encoded_password, salt)

        if bcrypt.checkpw(login_info["password"].encode(), hash_password):
            return make_response("Wrong credentials", 400)
        response = Response(LoginMeta(user.get_id(), type), [])
        return _corsify_actual_response(jsonify(response.serialize())), 200

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