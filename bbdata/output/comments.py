import requests
from ..config import output_api_url


class Comments:

    base_path = "/comments"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self):
        """
        GET /comments
        https://bbdata.daplab.ch/api/#comments_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def put(self, object_id, from_datetime, to_datetime, comment):
        """
        PUT /comments
        https://bbdata.daplab.ch/api/#comments_put
        """
        # TODO Implement
        raise NotImplementedError

    def get(self, comment_id):
        """
        GET /comments/{id}
        https://bbdata.daplab.ch/api/#comments__id__get
        """
        # TODO Implement
        raise NotImplementedError

    def delete(self, comment_id):
        """
        DELETE /comments/{id}
        https://bbdata.daplab.ch/api/#comments__id__delete
        """
        # TODO Implement
        raise NotImplementedError

    def post(self, comment_id, object_id, from_datetime, to_datetime, comment):
        """
        POST /comments/{id}
        https://bbdata.daplab.ch/api/#comments__id__post
        """
        # TODO Implement
        raise NotImplementedError