
import requests

class Status:
    
    @staticmethod
    def status_code_ok(response: requests.Response) -> None:
        assert response.status_code == 200, f"El status esperado es 200, pero se obtuvo {response.status_code}"

    @staticmethod
    def status_code_created(response: requests.Response) -> None:
        assert response.status_code == 201, f"El status esperado es 201, pero se obtuvo  {response.status_code}"

    @staticmethod
    def check_message_expected(message: str,response: str) -> None:
        assert message in response