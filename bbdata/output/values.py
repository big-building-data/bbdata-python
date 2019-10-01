from enum import Enum
import requests
from ..config import output_api_url


class Aggregation(Enum):
    QUARTERS = "quarters"
    HOURS = "hours"


class Values:

    base_path = "/values"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self, object_id, from_timestamp, to_timestamp, with_comments=False, headers=True):
        """
        GET /values
        """
        params = {
            "ids": object_id,
            "from": from_timestamp,
            "to": to_timestamp,
            "withComments": with_comments,
            "headers": headers
        }

        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def get_latest(self, object_id, before_timestamp, with_comments=False):
        """
        GET /values/latest
        """
        params = {
            "ids": object_id,
            "before": before_timestamp,
            "withComments": with_comments,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()

    def get_hours(self, object_id, from_timestamp, to_timestamp, with_comments=False, headers=True):
        """
        GET /values/hours
        """
        return self.__aggregation(object_id, from_timestamp, to_timestamp, "hours", with_comments, headers)

    def quarters(self, object_id, from_timestamp, to_timestamp, with_comments=False, headers=True):
        """
        GET /values/quarters
        """
        return self.__aggregation(object_id, from_timestamp, to_timestamp, "quarters", with_comments, headers)

    def __aggregation(self, object_id, from_timestamp, to_timestamp, aggregation, with_comments=False, headers=True):
        """
        Generic method to call the aggregations implemented in the API
        """
        params = {
            "ids": object_id,
            "from": from_timestamp,
            "to": to_timestamp,
            "withComments": with_comments,
            "headers": headers
        }

        url = output_api_url + self.base_path
        if aggregation == Aggregation.HOURS.value:
            url = url + "/hours"
        elif aggregation == Aggregation.QUARTERS.value:
            url = url + "/quarters"
        else:
            print("This aggregation isn't implemented")

        r = requests.get(url, params, headers=self.auth.headers)
        return r.json()
