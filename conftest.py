import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.login.login_page(username="lenapac22@mail.ru", password="cktlcndtyysq2321")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.login.login_page(username="lenapac22@mail.ru", password="cktlcndtyysq2321")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.login.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
