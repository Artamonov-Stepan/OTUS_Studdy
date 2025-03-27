import requests
import pytest
# url = "https://api.openbrewerydb.org/v1/breweries/"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

@pytest.mark.parametrize(
    "url", [("https://api.openbrewerydb.org/v1/breweries/meta")]
)
def test_positive_get(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json().get("total") == "8368"
    assert response.json().get("per_page") == "50"

@pytest.mark.parametrize(
    "url", [("https://api.openbrewerydb.org/v1/breweries/search?query=san%20diego&per_page=3")]
)
def test_positive_search(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@pytest.mark.parametrize(
    "url", [("https://api.openbrewerydb.org/v1/breweries/search?query=san%20diego&per_page=90001")]
)
def test_negative_search(url):
    response = requests.get(url)
    assert response.status_code == 429, f"Expected status code 429, got {response.status_code}"
    assert response.json().get("message") == "Concurrent request limit exceeded. Please delay concurrent calls using debounce or throttle."

@pytest.mark.parametrize(
    "url", [("https://api.openbrewerydb.org/v1/breweries/search?query=san%20diego&per_page=9")])
def test_negative_delete(url):
    response = requests.delete(url)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"


def test_with_params():
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {'by_state': "california", 'per_page': "3"}
    response = requests.get(url, params=params)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_json = response.json()
    assert isinstance(response_json, list), "Response is not a list"
    ids = [item.get('id') for item in response_json]
    expected_ids = ['ef970757-fe42-416f-931d-722451f1f59c', '4788221a-a03b-458c-9084-4cadd69ade6d', '5ae467af-66dc-4d7f-8839-44228f89b596']
    for expected_id in expected_ids:
     assert expected_id in ids, f"ID '{expected_id}' not found in response IDs: {ids}"