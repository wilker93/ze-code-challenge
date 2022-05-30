import json
import pytest


@pytest.fixture()
def connection():
    return "https://api.openweathermap.org/data/2.5/weather?"


@pytest.fixture()
def key():
    return "081e7158f17c12894a724118d7f0e5a3"


@pytest.fixture()
def lang_pt_br():
    return "pt_br"


@pytest.fixture()
def wrong_key():
    return "aBc123"


@pytest.fixture()
def lat():
    return -15.7797


@pytest.fixture()
def lon():
    return -47.9297


@pytest.fixture()
def city_name():
    return "Brasília"


@pytest.fixture()
def wrong_city_name():
    return "Brasolia"


@pytest.fixture()
def country_code_br():
    return "BR"


@pytest.fixture()
def country_code_uk():
    return "UK"


@pytest.fixture()
def city_id():
    return "3469058"


@pytest.fixture()
def wrong_city_id():
    return "123456"


@pytest.fixture()
def not_city_id():
    return "ABC"
