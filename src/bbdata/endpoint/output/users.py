import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response


class Users:

    base_path = "/users"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        Get the list of all users registered.

        GET /users
        https://bbdata.dsaplab.ch/api/#users_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

