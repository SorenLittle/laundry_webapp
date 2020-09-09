from datetime import datetime

from laundry_webapp import models


def todays_appointments(request):
    appts_query = request.dbsession.query(models.Appointment) \
        .filter(models.Appointment.date == datetime.today().date()) \
        .all()

    appts = {appointment.hour: appointment.user.name for appointment in appts_query}

    return appts
