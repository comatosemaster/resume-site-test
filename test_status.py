import requests
import pytest

BASE_URL = "https://davit-resume.com"

PAGES = [
    "/",
    "/skills/",
    "/experience/",
    "/projects/",
    "/education/",
    "/certificates/",
    "/languages/",
    "/contact/",
    "/animes/",
    "/movies/",
    "/bands/",
]

@pytest.mark.parametrize("path", PAGES)
def test_internal_pages_return_200(path):
    response = requests.get(f"{BASE_URL}{path}", timeout=10)
    assert response.status_code == 200
