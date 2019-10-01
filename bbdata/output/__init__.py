from .auth import Auth
from .info import Info
from .object_groups import ObjectGroups
from .objects import Objects
from .me import Me
from .values import Values


class Output:

    def __init__(self):
        self.auth = Auth()
        self.info = Info(self.auth)
        self.me = Me(self.auth)
        self.object_groups = ObjectGroups(self.auth)
        self.objects = Objects(self.auth)
        self.values = Values(self.auth)

    def login(self):
        return self.auth.login()

    def logout(self):
        return self.auth.logout()


output = Output()
