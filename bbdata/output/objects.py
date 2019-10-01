import requests
from ..config import output_api_url


class Objects:

    base_path = "/objects"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self, tags=None, search=None, page=None, per_page=None, writable=False):
        """
        GET /objects
        https://bbdata.daplab.ch/api/#objects_get
        """
        params = {
            "tags": tags,
            "search": search,
            "page": page,
            "perPage": per_page,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def put(self, name, unit_symbol, owner, description=None):
        """
        PUT /objects
        https://bbdata.daplab.ch/api/#objects_put
        """
        params = {
            "name": name,
            "description": description,
            "unitSymbol": unit_symbol,
            'owner': owner
        }
        url = output_api_url + self.base_path
        r = requests.put(url, params, headers=self.auth.headers)
        return r.json()

    def get(self, object_id):
        """
        GET /objects/{objectIs}
        https://bbdata.daplab.ch/api/#objects__objectid__get
        """
        url = output_api_url + self.base_path + "/" + str(object_id)
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def post(self, object_id):
        """
        POST /objects/{objectId}
        https://bbdata.daplab.ch/api/#objects__objectid__post
        """
        # TODO Implement
        raise NotImplementedError

    def delete(self, object_id):
        """
        POST /objects/{objectId}
        https://bbdata.daplab.ch/api/#objects__objectid__delete
        """
        # TODO Implement
        raise NotImplementedError

    def post_disable(self, object_id):
        """
        POST /objects/{objectId}/disable
        https://bbdata.daplab.ch/api/#objects__objectid__disable_post
        """
        # TODO Implement
        raise NotImplementedError

    def post_enable(self, object_id):
        """
        POST /objects/{objectId}/enable
        https://bbdata.daplab.ch/api/#objects__objectid__enable_post
        """
        # TODO Implement
        raise NotImplementedError

    def get_tokens(self, object_id):
        """
        GET /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_get
        """
        url = output_api_url + self.base_path + "/" + str(object_id) + "/tokens"
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def put_tokens(self):
        """
        PUT /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_put
        """
        # TODO Implement
        raise NotImplementedError

    def post_tokens(self):
        """
        POST /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_post
        """
        # TODO Implement
        raise NotImplementedError

    def delete_tokens(self):
        """
        DELETE /objects/{objectId}/tokens
        https://bbdata.daplab.ch/api/#objects__objectid__tokens_delete
        """
        # TODO Implement
        raise NotImplementedError

    def put_tags(self):
        """
        PUT /objects/{objectId}/tags
        https://bbdata.daplab.ch/api/#objects__objectid__tags_put
        """
        # TODO Implement
        raise NotImplementedError

    def delete_tags(self):
        """
        DELETE /objects/{objectId}/tags
        https://bbdata.daplab.ch/api/#objects__objectid__tags_delete
        """
        # TODO Implement
        raise NotImplementedError

    def get_comments(self, object_id):
        url = output_api_url + self.base_path + "/" + str(object_id) + "/comments"
        r = requests.get(url, headers=self.auth.headers)
        return r.json()
