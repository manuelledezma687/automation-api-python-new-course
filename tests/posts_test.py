import requests
import json
import allure
import pytest
from config import Data
from utils import read_file

@allure.title("Obtener todos los Albumes")
@allure.label("critical")
@pytest.mark.smoke
def test_get_all_albums() -> None:
    response = requests.get(Data.BASE_URL + "/albums", timeout=10)
    assert response.status_code == 200

@allure.title("Obtener un Album")
@allure.label("critical")
@pytest.mark.smoke
def test_get_an_album() -> None:
    response = requests.get(Data.BASE_URL + "/albums", timeout=10)
    albums = response.json() 
    title_content = [album['title'] for album in albums]
    assert 'quidem molestiae enim' in title_content 

@allure.title("Crear un Post")
@allure.label("critical")
@pytest.mark.smoke
def test_create_resource() -> None:
    payload = json.dumps(read_file.reader('post.json'))
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(Data.BASE_URL + "/posts", data=payload, headers=headers, timeout=10)
    assert response.status_code == 201
