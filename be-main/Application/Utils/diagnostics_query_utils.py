from sqlalchemy import or_, desc
from Application.Model.Appointments import Appointments
from Application.Model.Diagnostic import Diagnostic
from Application.Utils import constants

def get_diagnostic(query):
    try:
        id_position = query.index("id")
        appointment_id = query[id_position + 1]
        diagnostic = Diagnostic.query.filter_by(id_appointment=str(appointment_id)).first()
        return diagnostic
    except:
        # no patient filter added
        pass
    return 0

