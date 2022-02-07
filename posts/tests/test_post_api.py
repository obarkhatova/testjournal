import pytest

from users.tests.fixtures import demo_users

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures('demo_users')
def test_create_post(demo_users, login_user):
    user = demo_users[0][0]
    client = demo_users[0][1]
    r = client.post("/api/posts", {"title": "Some test post",
                                 "content": "Some content as."
                            })
    assert r.status_code == 201
    post = r.json()
    assert post['blog'] == user.blog.pk

