import requests
import json
from config import Data
from utils import read_file

def test_get_all_albums() -> None:
    response = requests.get(Data.BASE_URL + "/albums", timeout=10)
    print(response)
    assert response.status_code == 200

def test_get_a_album() -> None:
    response = requests.get(Data.BASE_URL + "/albums", timeout=10)
    albums = response.json() 
    title_content = [album['title'] for album in albums]
    assert 'quidem molestiae enim' in title_content 

def test_create_resource() -> None:
    payload = json.dumps(read_file.reader('post.json'))
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(Data.BASE_URL + "/posts", data=payload, headers=headers, timeout=10)
    assert response.status_code == 201