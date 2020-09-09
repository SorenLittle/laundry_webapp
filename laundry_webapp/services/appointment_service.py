from datetime import datetime

from laundry_webapp import models


def todays_left_appointments(request):
    appts_query = request.dbsession.query(models.Appointment) \
        .filter(models.Appointment.date == datetime.today().date()) \
        .filter(models.Appointment.machine_id == "Left") \
        .all()

    appts = {appointment.hour: appointment.user.name for appointment in appts_query}

    return appts


def todays_right_appointments(request):
    appts_query = request.dbsession.query(models.Appointment) \
        .filter(models.Appointment.date == datetime.today().date()) \
        .filter(models.Appointment.machine_id == "Right") \
        .all()

    appts = {appointment.hour: appointment.user.name for appointment in appts_query}

    return appts
