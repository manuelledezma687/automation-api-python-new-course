import json
import allure
import pytest
from utils import read_file
from services.api_service import APIClient
from services.status_code import Status

@allure.title("Obtener todos los Albumes")
@allure.label("critical")
@pytest.mark.smoke
def test_get_all_albums() -> None:
    response = APIClient.get("/albums")
    Status.status_code_ok(response)

@allure.title("Obtener un Album")
@allure.label("critical")
@pytest.mark.smoke
def test_get_an_album() -> None:
    response = APIClient.get("/albums")
    albums = response.json() 
    title_content = [album['title'] for album in albums]
    Status.check_message_expected('quidem molestiae enim',title_content)

@allure.title("Crear un Post")
@allure.label("critical")
@pytest.mark.smoke
def test_create_resource() -> None:
    payload = json.dumps(read_file.reader('post.json'))
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = APIClient.post("/posts", data=payload, headers=headers)
    Status.status_code_created(response)
