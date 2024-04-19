import requests

class BrasilAPI:
    def __init__(self) -> None:
        self.base_url = "https://brasilapi.com.br/api"
    
    def get_taxes(self):
        response = requests.get(self.base_url+"/taxas/v1")
        if response.status_code in range(200, 300, 1):
            return response.json()
        else:
            raise Exception(response.text)