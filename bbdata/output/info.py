import requests
from ..config import output_api_url


class Info:

    base_path = "/info"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        GET /info
        https://bbdata.daplab.ch/api/#info_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return r.json()
