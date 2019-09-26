import json
import requests
from pathlib import Path

from ..config import api_url


class Login:

    credentials = None
    username = None
    password = None
    user_id = None
    secret = None

    def __init__(self):

        home = Path.home()
        credentials = Path(".bbdata/credentials.json")
        credentials_path = home / credentials

        if credentials_path.is_file():
            with open(str(credentials_path)) as json_file:
                data = json.load(json_file)
            self.credentials = data
            self.username = data['username']
            self.password = data['password']
            print("Welcome " + self.username)

        else:
            print("You don't have any credentials file. Create it at ~" + str(credentials))
            print("The content should be :")
            print("""\t{ "username": "<USERNAME>", "password": "<PASSWORD>" }""")

    def login(self):
        headers = {'content-type': 'application/json'}
        url = api_url + "/login"
        r = requests.post(url, headers=headers, json=self.credentials)
        response = r.json()
        self.user_id = response["userId"]
        self.secret = response["secret"]
        return response

    def logout(self):
        headers = {
            'bbuser': str(self.user_id),
            'bbtoken': str(self.secret)
        }
        url = api_url + "/logout"
        r = requests.post(url, headers=headers)
        return r.text
