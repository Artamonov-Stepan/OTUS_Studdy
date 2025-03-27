import requests
import pytest
# url = "https://jsonplaceholder.typicode.com/todos/"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# assert " id" in response.text
# print(response.text)

@pytest.mark.parametrize(
    "url", [("https://jsonplaceholder.typicode.com/todos/")])
def test_simple_positive_get(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

@pytest.mark.parametrize(
    "url", [("https://jsonplaceholder.typicode.com/todys/")])
def test_simple_negative_get(url):
    response = requests.get(url)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

body = {
    "title": "Create test",
    "body": "some text in our body\n'Hello everyone'\nsome text in our body"
}

@pytest.mark.parametrize(
    "url", [("https://jsonplaceholder.typicode.com/posts/")])
def test_positive_post(url):
    response = requests.post(url, json=body)
    assert response.status_code == 201, f"Status code is not 201, but {response.status_code}"
    response_data = response.json()
    assert 'id' in response_data, "Response does not contain 'id'"
    assert isinstance(response_data['id'], int), "'id' should be an integer"
    assert response_data.get('title') == body['title'], "Title doesn't match!"
    assert response_data.get('body') == body['body'], "Body doesn't match!"

@pytest.mark.parametrize(
    "url", [("https://jsonplaceholder.typicode.com/todos/1")])
def test_simple_positive_deleted(url):
    response = requests.delete(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

@pytest.mark.parametrize(
    "url", [("https://jsonplaceholder.typicode.com/todys/9999")])
def test_simple_negative_deleted(url):
    response = requests.delete(url)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

