from datetime import datetime
from pyramid.view import view_config

from laundry_webapp import models


@view_config(route_name='home',
             renderer='laundry_webapp:templates/home.pt')
def home(request):
    # TODO: distinguish between left and right machines -> change "appointment = models..." line

    # execute when there is a POST request
    if request.POST.get('name'):

        # receive a "given_name" from the users POST into the website
        given_name = request.POST.get('name')
        # TODO: add other kinds of string cleaning
        given_name = given_name.lower()
        given_id = ''

        # get the appropriate id from the database
        first_time = True
        for user_id, name in request.dbsession.query(models.User.id, models.User.name):
            if given_name == name:
                first_time = False
                given_id = user_id
                break

        # if the user is not in the database, add them
        if first_time:
            request.dbsession.add(models.User(name=given_name))

            # get that new users id from the database
            for user_id, name in request.dbsession.query(models.User.id, models.User.name):
                if given_name == name:
                    given_id = user_id
                    break

        # build appointment for that user
        appointment = models.Appointment(datetime=datetime.today().replace(hour=7),
                                         user_id=given_id,
                                         machine_id="Left",
                                         )

        request.dbsession.add(appointment)

    # send updated dictionary of appointments
    todays_appts = {}
    for appointment in request.dbsession.query(models.Appointment):
        # get only appointments for today
        if appointment.datetime.date() == datetime.today().date():
            todays_appts[appointment.datetime.strftime("%H:00")] = appointment.user.name

    return {
        'url': request.route_url('home'),
        'todays_appts': todays_appts,
    }
