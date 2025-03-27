import requests
import pytest
# url = "https://dog.ceo/api/breed/hound/images"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

@pytest.mark.parametrize(
    "url", [("https://dog.ceo/api/breed/hound/images")])
def test_positive_get(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 404, got {response.status_code}"
    assert response.json().get("status") == "success"

@pytest.mark.parametrize(
    "url", [("https://dog.ceo/api/breed/hound/images")])
def test_negative_post(url):
    response = requests.post(url)
    assert response.status_code == 405, f"Expected status code 405, got {response.status_code}"
    assert response.json().get("status") == "error"
    response_text = response.text
    error_phrase = "Method Not Allowed"
    assert error_phrase in response_text, f"Error phrase '{error_phrase}' not found in response. Got: '{response_text}'"

@pytest.mark.parametrize(
    "url", [("https://dog.ceo/api/breed/indian/images/random")])
def test_negative_get(url):
    response = requests.get(url)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    assert response.json().get("status") == "error"
    response_json = response.json()
    expected_message = "Breed not found"
    actual_message = response_json.get('message')
    assert expected_message in actual_message, f"Message does not contain '{expected_message}'. Actual message: '{actual_message}'"


@pytest.mark.parametrize(
    "url", [("https://dog.ceo/api/breed/husky/images/random")])
def test_negative_delete_get(url):
    response = requests.delete(url)
    assert response.status_code == 405, f"Expected status code 405, got {response.status_code}"
    response_json = response.json()
    assert 'message' in response_json, "Response does not contain 'message' key"
    assert "Method Not Allowed" in response_json['message'], "Error message does not indicate method restriction"


@pytest.mark.parametrize(
    "url", [("https://dog.ceo/api/breeds/list/all")])
def test_list_all_breeds(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_json = response.json()
    assert 'message' in response_json, "Response does not contain 'message' key"
    breeds = response_json['message']
    assert len(breeds) > 0, "Response contains no breeds"
    for breed_name, sub_breeds in breeds.items():
        assert isinstance(sub_breeds, list), f"Breed '{breed_name}' has incorrect format for sub-breeds"
