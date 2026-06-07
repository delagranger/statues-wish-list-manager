import requests
from exceptions import HTMLLoaderError

class HTMLLoader:
    def __init__(self):
        self._session = requests.Session()
        self._session.trust_env = False


    def load(self, url: str) -> str:
        try:
            response = self._session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise HTMLLoaderError(str(e)) from e
