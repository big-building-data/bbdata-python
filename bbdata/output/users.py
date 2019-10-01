import requests
from ..config import output_api_url


class Users:

    base_path = "/users"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        GET /users
        https://bbdata.dsaplab.ch/api/#users_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return r.json()
