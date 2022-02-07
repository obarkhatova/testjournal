import pytest

from users.tests.fixtures import users

pytestmark = pytest.mark.django_db


def test_create_user(admin, make_diff):
    data = {"username": 'test_user',
            "password": 'P@ssw0rd!123',
            "email": 'test_user@mail.com'}
    r = admin.post('/api/users', data)
    assert r.status_code == 201
    data.update({"is_staff": False,
                 "last_login": None,
                })
    diff = make_diff(data, r.json(), ignore=('password',), skip_unexpected=True)
    assert not diff, diff


@pytest.mark.parametrize('users',
                         [
                             [{"username": 'test_user1',
                              "password": 'P@ssw0rd!123',
                              "email": 'test_user1@mail.com'},
                             {"username": 'test_user2',
                              "password": 'P@ssw0rd!123',
                              "email": 'test_user2@mail.com'},
                             {"username": 'test_user3',
                              "password": 'P@ssw0rd!123',
                              "email": 'test_user3@mail.com'}
                              ],
                         ],
                        indirect=['users'])
def test_list_users(admin, make_diff, users):
    r = admin.get('/api/users')
    assert r.status_code == 200
    expected = [{
        "username": 'admin',
        "email": '1@mail.com',
        "id": 1,
        "is_staff": True,
    }]
    for i in users:
        expected.append({
             "username": i.username,
             "email": i.email,
             "id": i.id,
             "is_staff": i.is_staff,
             })

    diff = make_diff(expected, r.json(), ignore=('password', 'date_joined', 'last_login'),
                     skip_unexpected=True)
    assert not diff, diff

