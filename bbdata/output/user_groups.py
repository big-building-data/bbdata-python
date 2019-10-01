import requests
from ..config import output_api_url


class UserGroups:

    base_path = "/usergroups"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self):
        """
        GET /usergroups
        https://bbdata.daplab.ch/api/#usergroups_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def put(self, name):
        """
        GET /usergroups
        https://bbdata.daplab.ch/api/#usergroups_put
        """
        # TODO Implement
        raise NotImplementedError

    def delete(self, user_group_id):
        """
        GET /usergroups
        https://bbdata.daplab.ch/api/#usergroups_delete
        """
        # TODO Implement
        raise NotImplementedError

    def get(self, user_group_id):
        """
        GET /usergroups/{userGroupId}
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__get
        """
        url = output_api_url + self.base_path + "/" + str(user_group_id)
        r = requests.get(url, headers=self.auth.headers)
        return r.json()

    def get_users(self, user_group_id):
        """
        GET /usergroups/{userGroupId}/users
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_get
        """
        # TODO Implement
        raise NotImplementedError

    def put_users(self, user_group_id, user_id, is_admin=False):
        """
        GET /usergroups/{userGroupId}/users
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_put
        """
        # TODO Implement
        raise NotImplementedError

    def delete_users(self, user_group_id, user_id):
        """
        GET /usergroups/{userGroupId}/users
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_delete
        """
        # TODO Implement
        raise NotImplementedError

    def put_users_new(self, user_group_id, name, email, password, is_admin=False):
        """
        PUT /usergroups/{userGroupsId}/users/new
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_new_put
        """
        # TODO Implement
        raise NotImplementedError
