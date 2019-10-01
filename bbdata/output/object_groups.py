import requests
from ..config import output_api_url


class ObjectGroups:

    base_path = "/objectGroups"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def list(self, with_objects=False, writable=False, ):
        params = {
            "withObjects": with_objects,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()
