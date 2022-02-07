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
        users.append(User.objects.create({"username": 'test_user',
                                           "password": 'P@ssw0rd!123',
                                           "email": 'test_user@mail.com'}))
    if len(users) == 1:
        yield users[0]
    else:
        yield users


@pytest.fixture
def admin(login_user):
    return login_user(username='admin', password='P@ssw0rd')


@pytest.fixture
def demo_users(login_user):
    users = []
    u = User(
        username='user1',
        firstname='Firstname1',
        lastname='Lasname1',
        email='user1@mail.com',
        is_staff=False,
        is_superuser=False,
        is_active=True,
    )
    u.set_password('P@ssw0rd')
    u.save()
    users.append(u)

    u = User(
        username='user2',
        firstname='Firstname2',
        lastname='Lasname2',
        email='user2@mail.com',
        is_staff=False,
        is_superuser=False,
        is_active=True,
    )
    u.set_password('P@ssw0rd')
    u.save()
    users.append(u)

    clients = [login_user(username=x.username, password='P@ssw0rd') for x in users]

    yield list(zip(users, clients))


