from datetime import date
from pyramid.view import view_config

from laundry_webapp import models


@view_config(route_name='home',
             renderer='laundry_webapp:templates/home.pt')
def home(request):
    # if hasattr(request.POST.get('name'), 'text'):
    #     name = request.POST.get('name')
    #     appt = models.LeftAppt(date=date.today(), seven=name)
    #     request.dbsession.add(appt)

    name = request.POST.getall('name')
    appt = models.LeftAppt(date=date.today(), seven=name)
    request.dbsession.add(appt)

    return {
        'url': request.route_url('home')
    }
