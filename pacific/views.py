from pyramid.view import view_config


@view_config(route_name='home', renderer='/index.plim')
def home(request):
    users_repo = request.db.repositories.get('users')
    user = users_repo.get_by_id(1)
    return {'project': 'Pacific'}
