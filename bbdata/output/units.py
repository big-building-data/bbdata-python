import requests
from ..config import output_api_url


class Units:

    base_path = "/units"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        GET /units
        https://bbdata.daplab.ch/api/#units_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def post(self, name, symbol, type):
        """
        POST /units
        https://bbdata.daplab.ch/api/#units_post
        """
        data = {
            "name": name,
            "symbol": symbol,
            "type": type
        }
        url = output_api_url + self.base_path
        r = requests.post(url, data, headers=self.auth.headers)
        return r.json()
