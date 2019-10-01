import requests
from ..config import output_api_url


class Objects:

    base_path = "/objects"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def list(self, page, per_page, writable=False, ):
        params = {
            "page": page,
            "perPage": per_page,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def search(self, page, per_page, search="led", writable=False):
        params = {
            "page": page,
            "perPage": per_page,
            "search": search,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def create_new(self, name, unit, group_id, description=None):
        params = {
            "name": name,
            "description": description,
            "unitSymbol": unit,
            'owner': group_id
        }
        url = output_api_url + self.base_path
        r = requests.put(url, params, headers=self.auth.headers)
        response = r.json()
        return response

    def edit_description(self):
        # TODO Implement
        print("Not Implemented")

    def get_details(self, object_id):
        url = output_api_url + self.base_path + "/" + str(object_id)
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def add_token(self):
        # TODO Implement
        print("Not Implemented")

    def get_tokens(self, object_id):
        url = output_api_url + self.base_path + "/" + str(object_id) + "/tokens"
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def remove_tokens(self):
        # TODO Implement
        print("Not Implemented")

    def add_tags(self):
        # TODO Implement
        print("Not Implemented")

    def remove_tags(self):
        # TODO Implement
        print("Not Implemented")

    def get_comments(self, object_id):
        url = output_api_url + self.base_path + "/" + str(object_id) + "/comments"
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def disable(self):
        # TODO Implement
        print("Not Implemented")

    def enable(self):
        # TODO Implement
        print("Not Implemented")

    def remove(self):
        # TODO Implement
        print("Not Implemented")
