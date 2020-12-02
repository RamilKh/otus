from pytest import fixture
from app.main import application


@fixture
def client():
    with application.test_client() as client:
        yield client


def test_users_list_status(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_users_active(client):
    response = client.get("/users")
    assert b'<a href="/users" class="headline__menu__item headline__menu__item_active">Users</a>' in response.data


def test_users_add_html(client):
    response = client.get("/users/add")
    assert b' <form action="/users/add" method="post" class="form">' in response.data
