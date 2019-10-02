import requests
from ..exceptions import UnknownResponseError
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
        if r.status_code == 200:
            return r.json()
        else:
            raise UnknownResponseError
