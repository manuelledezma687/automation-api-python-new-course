import requests
from config import Data

class APIClient:
    
    @staticmethod
    def get(endpoint: str, timeout: int = 10):
        try:
            response = requests.get(Data.BASE_URL + endpoint, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise AssertionError(f"Error en la petición GET: {e}")

    @staticmethod
    def post(endpoint: str, data: dict, headers: dict, timeout: int = 10):
        try:
            response = requests.post(Data.BASE_URL + endpoint, data=data, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise AssertionError(f"Error en la petición POST: {e}")