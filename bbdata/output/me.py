import requests
from ..config import output_api_url


class Me:

    base_path = "/me"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        GET /me
        https://bbdata.daplab.ch/api/#me_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def get_groups(self, admin=False):
        """
        GET /me/groups
        https://bbdata.daplab.ch/api/#me_groups_get
        """
        # TODO add admin query param
        url = output_api_url + self.base_path + "/groups"
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def get_apikeys(self):
        """
        GET /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_get
        """
        url = output_api_url + self.base_path + "/apikeys"
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def put_apikeys(self, writable, expire, description=None):
        """
        PUT /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_put
        """
        # TODO Implement
        raise NotImplementedError

    def post_apikeys(self, apikey_id, read_only, secret, user_id):
        """
        POST /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_post
        """
        # TODO Implement
        raise NotImplementedError

    def delete_apikeys(self, apikey_id):
        """
        DELETE /me/apikeys
        https://bbdata.daplab.ch/api/#me_apikeys_delete
        """
        # TODO Implement
        raise NotImplementedError
