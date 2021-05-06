import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()



#Different Tests

def test_fortune(app, client):
    res = client.get('/')
    assert res.status_code == 302
    page_output = res.get_data(as_text=True)
    assert len(page_output) != 0


def test_cowsay(app, client):
    message = 'hello'
    res = client.get('/cowsay/%s/' % message)
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output


def test_cowfortune(app, client):
    res = client.get('/cowfortune/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert len(page_output) != 0
