import requests
import pytest
BASE_URL = "https://jsonplaceholder.typicode.com/todos/"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# assert " id" in response.text
# print(response.text)

@pytest.mark.parametrize("expected_data", [
    {"userId": 4, "id": 62},
    {"userId": 4, "id": 64},
    {"userId": 4, "id": 65}
])
def test_positive_get(expected_data):
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    json_data = response.json()
    for item in json_data:
        if expected_data["userId"] == item["userId"] and expected_data["id"] == item["id"]:
            assert "title" in item, "Key 'title' not found in the response"
            assert "completed" in item, "Key 'completed' not found in the response"

@pytest.mark.parametrize("id", [-2, 1.0, "ABC1"])
def test_simple_negative_get(id):
    get_url = f"{BASE_URL}{id}"
    response = requests.get(get_url)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"


@pytest.mark.parametrize("data", [
    {
        "title": "Create test 1",
        "body": "Some text in our body 3.",
        "userId": 1
    },
    {
        "title": "TCreate test 2",
        "body": "Some text in our body 4.",
        "userId": 2
    }])
def test_positive_post(data):
    response = requests.post(BASE_URL, json=data)
    assert response.status_code == 201, f"Status code is not 201, but {response.status_code}"
    response_data = response.json()
    assert 'id' in response_data, "Response does not contain 'id'"
    assert isinstance(response_data['id'], int), "'id' should be an integer"
    assert response_data.get('title') == data['title'], "Title doesn't match!"
    assert response_data.get('body') == data['body'], "Body doesn't match!"
    assert response_data.get('userId') == data['userId'], "User ID doesn't match!"


@pytest.mark.parametrize("id", [ 1, 10, 99])
def test_positive_delete(id):
    deleted_url = f"{BASE_URL}{id}"
    response = requests.delete(deleted_url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@pytest.mark.parametrize(
    "url", [("https://jsonplaceholder.typicode.com/todAs/1")])
def test_incorrect_url(url):
    response = requests.delete(url)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
