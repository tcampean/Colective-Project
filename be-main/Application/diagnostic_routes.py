import datetime

from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin

from Application.Model.Diagnostic import Diagnostic
from Application.Model.Metadata import Metadata
from Application.Model.Response import Response
from Application.Utils.diagnostics_query_utils import get_diagnostic
from Application.database import database

diagnostics_api = Blueprint('diagnostics_api', __name__)

@cross_origin()
@diagnostics_api.route('/diagnostics/', methods= ["GET", "POST", "OPTIONS"])
def amazing_diagnostics():
    if request.method == "GET":
        query = request.query_string.decode()
        query = query.replace("&", "=")
        query = query.split("=")
        diagnostic = []
        diagnostic.append(get_diagnostic(query))
        if diagnostic != 0:
            response = Response(Metadata(1), diagnostic)
            return jsonify(response.serialize())
        else:
            return 404

    elif request.method == "POST":
        new_diagnostic = request.json
        Diagnostic.query.filter_by(id_appointment=new_diagnostic['id_appointment']).delete()
        database.session.commit()
        diagnostic = Diagnostic(int(new_diagnostic["id_appointment"]),
                                new_diagnostic["prescription"], datetime.datetime.strptime(new_diagnostic["issue_date"],'%Y-%m-%d').date(),
                                datetime.datetime.strptime(new_diagnostic["expiration_date"],'%Y-%m-%d').date(),
                                int(new_diagnostic["compensated"]))
        database.session.add(diagnostic)
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