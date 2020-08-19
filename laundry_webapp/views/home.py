from pyramid.view import view_config


@view_config(route_name='home', renderer='laundry_webapp:templates/home.pt')
def home(request):



    return {
        'project': 'laundry_webapp'
    }
