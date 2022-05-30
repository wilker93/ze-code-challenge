import time
from datetime import datetime, timedelta
import pytest
import httpx
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize("url", [lazy_fixture("connection")])
class TestOpenWeatherMap:
    def test_post_open_weather_map(self, url, key, lat, lon):
        endpoint = f"{url}lat={lat}&lon={lon}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == "BR")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == "Brasília")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_open_weather_map_units_metric(self, url, key, lat, lon):
        endpoint = f"{url}lat={lat}&lon={lon}&appid={key}&units=metric"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == "BR")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == "Brasília")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_open_weather_map_units_imperial(self, url, key, lat, lon):
        endpoint = f"{url}lat={lat}&lon={lon}&appid={key}&units=imperial"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == "BR")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == "Brasília")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_open_weather_map_lang_pt_br(self, url, key, lat, lon, lang_pt_br):
        endpoint = f"{url}lat={lat}&lon={lon}&appid={key}&lang={lang_pt_br}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == "BR")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == "Brasília")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_by_city_name(self, url, key, city_name, lat, lon):
        endpoint = f"{url}q={city_name}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == "BR")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == f"{city_name}")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_by_city_name_and_country_code(self, url, key, city_name, lat, lon, country_code_br):
        endpoint = f"{url}q={city_name},{country_code_br}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == f"{country_code_br}")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == f"{city_name}")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_by_city_id(self, url, key, lat, lon, city_id, city_name):
        endpoint = f"{url}id={city_id}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 200:
            assert (response_dict["coord"]["lon"] == lon and response_dict["coord"]["lat"] == lat)
            assert (response_dict["sys"]["type"] == 1 and response_dict["sys"]["id"] == 8336 and response_dict["sys"][
                "country"] == "BR")
            assert (response_dict["timezone"] == -10800)
            assert (response_dict["id"] == 3469058)
            assert (response_dict["name"] == f"{city_name}")
            assert (response_dict["cod"] == 200)
            print("PASSED")
        else:
            assert False

    def test_post_wrong_latitude(self, url, key, lon):
        lat = 500
        endpoint = f"{url}lat={lat}&lon={lon}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 400:
            assert (
                    response_dict["cod"] == "400"
                    and response_dict["message"] == "wrong latitude"
            )
            print("PASSED")
        else:
            assert False

    def test_post_wrong_longitude(self, url, key, lat):
        lon = 210
        endpoint = f"{url}lat={lat}&lon={lon}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 400:
            assert (
                    response_dict["cod"] == "400"
                    and response_dict["message"] == "wrong longitude"
            )
            print("PASSED")
        else:
            assert False

    def test_post_wrong_key(self, url, wrong_key, lat, lon):
        endpoint = f"{url}lat={lat}&lon={lon}&appid={wrong_key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 401:
            assert (
                    response_dict["cod"] == 401
                    and response_dict[
                        "message"] == "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."
            )
            print("PASSED")
        else:
            assert False

    def test_post_wrong_city(self, url, key, wrong_city_name):
        endpoint = f"{url}q={wrong_city_name}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 404:
            assert (
                    response_dict["cod"] == "404"
                    and response_dict["message"] == "city not found"
            )
            print("PASSED")
        else:
            assert False

    def test_post_city_not_found_in_country_code(self, url, key, city_name, country_code_uk):
        endpoint = f"{url}q={city_name},{country_code_uk}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 404:
            assert (
                    response_dict["cod"] == "404"
                    and response_dict["message"] == "city not found"
            )
            print("PASSED")
        else:
            assert False

    def test_post_by_city_id_not_found(self, url, key, wrong_city_id):
        endpoint = f"{url}id={wrong_city_id}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 404:
            assert (
                    response_dict["cod"] == "404"
                    and response_dict["message"] == "city not found"
            )
            print("PASSED")
        else:
            assert False

    def test_post_by_wrong_city_id(self, url, key, not_city_id):
        endpoint = f"{url}id={not_city_id}&appid={key}"
        response = httpx.post(url=endpoint, timeout=100)
        response_dict = response.json()
        print(response_dict)

        if response.status_code == 400:
            assert (
                    response_dict["cod"] == "400"
                    and response_dict["message"] == f"{not_city_id} is not a city ID"
            )
            print("PASSED")
        else:
            assert False
