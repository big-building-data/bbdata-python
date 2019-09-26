import requests
from ..config import output_api_url


class Me:

    base_path = "/me"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def me(self):
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        response = r.json()
        return response

    def groups(self):
        url = output_api_url + self.base_path + "/groups"
        r = requests.get(url, headers=self.auth.headers)
        response = r.json()
        return response
