from pytest import fixture
from app.main import application


@fixture
def client():
    with application.test_client() as client:
        yield client


def test_tokens_list_status(client):
    response = client.get("/tokens")
    assert response.status_code == 200


def test_tokens_active(client):
    response = client.get("/tokens")
    assert b'<a href="/tokens" class="headline__menu__item headline__menu__item_active">Tokens</a>' in response.data


def test_tokens_add_html(client):
    response = client.get("/tokens/add")
    assert b' <form action="/tokens/add" method="post" class="form">' in response.data
