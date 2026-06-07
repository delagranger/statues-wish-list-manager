import requests

class HTMLLoader:
    def __init__(self):
        self._session = requests.Session()
        self._session.trust_env = False


    def load(self, url: str) -> str:
        response = self._session.get(url, timeout=30)
        return response.text
