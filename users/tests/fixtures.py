import pytest

from users.models import User


@pytest.fixture
def users(request, db):
    users = []
    if hasattr(request, 'param'):
        param = request.param
        k = User.objects.all()
        if isinstance(param, list):
            for val in param:
                users.append(User.objects.create(**val))
        else:
            users.append(User.objects.create(**param))
    else:
        users.append(User({"username": 'test_user',
                           "password": 'P@ssw0rd!123',
                           "email": 'test_user@mail.com'}))
    if len(users) == 1:
        yield users[0]
    else:
        yield users

