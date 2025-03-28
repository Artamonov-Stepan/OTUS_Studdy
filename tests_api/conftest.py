import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        type=int,
        default=200,
        help="Expected response status code"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")

def test_check_response(base_url, expected_status_code):
    response = requests.get(f"{base_url}/sfhfh")
    assert response.status_code == expected_status_code, (
        f"Expected response status code doesn't match. Expect: {expected_status_code}, got: {response.status_code}"
    )