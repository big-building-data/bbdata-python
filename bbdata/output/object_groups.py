import requests
from ..config import output_api_url


class ObjectGroups:

    base_path = "/objectGroups"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self, with_objects=False, writable=False):
        """
        GET /objectGroups
        https://bbdata.daplab.ch/api/#objectgroups_get
        """
        params = {
            "withObjects": with_objects,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def put(self, name, description, unit_symbol, owner):
        """
        PUT /objectGroups
        https://bbdata.daplab.ch/api/#objectgroups_put
        """
        params = {
            "name": name,
            "description": description,
            "unitSymbol": unit_symbol,
            "owner": owner,
        }
        url = output_api_url + self.base_path
        r = requests.put(url, params, headers=self.auth.headers)
        return r.json()

    def get(self, group_id):
        """
        GET /objectGroups/{groupId}
        https://bbdata.daplab.ch/api/#objectgroups__groupid__get
        """
        params = {
            "groupId": group_id,
        }
        url = output_api_url + self.base_path + "/" + str(group_id)
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def post(self, group_id):
        """
        POST /objectGroups/{groupId}
        https://bbdata.daplab.ch/api/#objectgroups__groupid__post
        """
        # TODO Implement
        raise NotImplementedError

    def delete(self, group_id):
        """
        DELETE /objectGroups/{groupId}
        https://bbdata.daplab.ch/api/#objectgroups__groupid__delete
        """
        # TODO Implement
        raise NotImplementedError

    def get_objects(self, group_id):
        """
        GET /objectGroups/{groupId}/objects
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_get
        """
        # TODO Implement
        raise NotImplementedError

    def put_object(self, group_id, object_id):
        """
        GET /objectGroups/{groupId}/objects
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        # TODO Implement
        raise NotImplementedError

    def delete_object(self, group_id, object_id):
        """
        GET /objectGroups/{groupId}/objects
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_delete
        """
        # TODO Implement
        raise NotImplementedError

    def get_permissions(self, group_id):
        """
        GET /objectGroups/{groupId}/permissions
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        # TODO Implement
        raise NotImplementedError

    def put_permissions(self, group_id, group_id_to_add):
        """
        GET /objectGroups/{groupId}/permissions
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        # TODO Implement
        raise NotImplementedError

    def delete_permissions(self, group_id, group_id_to_delete):
        """
        GET /objectGroups/{groupId}/permissions
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        # TODO Implement
        raise NotImplementedError



