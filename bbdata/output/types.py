import requests
from ..config import output_api_url
from ..exceptions import UnknownResponseError


class Types:

    base_path = "/types"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        GET /types
        https://bbdata.daplab.ch/api/#types_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        if r.status_code == 200:
            return r.json()
        else:
            raise UnknownResponseError
