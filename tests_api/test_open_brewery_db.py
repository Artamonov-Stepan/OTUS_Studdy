import requests
import pytest
BASE_URL = "https://api.openbrewerydb.org/v1/breweries/"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

url = f"{BASE_URL}/meta"
def test_positive_get():
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json().get("total") == "8369"
    assert response.json().get("per_page") == "50"


@pytest.mark.parametrize(
    "params, expected_values",
    [(       {"by_city": "san diego", "per_page": 3},
             {"city": "San Diego", "country": "United States"}
    )])
def test_positive_search(params, expected_values):
    search_url = f"{BASE_URL}/search?by_city={params['by_city']}&per_page={params['per_page']}"
    response = requests.get(search_url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Response is not a list"
    expected_length = params['per_page']
    assert len(data) <= expected_length, f"Expected length <= {expected_length}, got {len(data)}"
    for brewery in data:
        assert expected_values['city'] in brewery.get('city'), f"City '{expected_values['city']}' not found in response"
        assert expected_values['country'] in brewery.get(
            'country'), f"Country '{expected_values['country']}' not found in response"


@pytest.mark.parametrize(
    "city", ["Williamsville", "San Diego", "Bend", "Denver"]
)
def test_get_breweries_by_city(city):
    response = requests.get(BASE_URL, params={"by_city": city})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    for resp_info in response.json():
        assert city in resp_info.get('city')


@pytest.mark.parametrize(
    "params, expected_status_code", [({"query": "san diego", "per_page": 90001}, 429)])
def test_negative_search(params, expected_status_code):
    get_url = f"{BASE_URL}/search?{params['query']}&per_page={params['per_page']}"
    response = requests.get(get_url)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, got {response.status_code}"


@pytest.mark.parametrize(
    "params, expected_status_code", [({"query": "san diego", "per_page": 9}, 404)])
def test_negative_delete(params, expected_status_code):
    deleted_url = f"{BASE_URL}/search?{params['query']}&per_page={params['per_page']}"
    response = requests.delete(deleted_url)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, got {response.status_code}"