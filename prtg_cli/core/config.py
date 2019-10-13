from dataclasses import dataclass

import requests

from .constants import PRTG_REQUEST_CONFIGS


@dataclass
class PrtgConfig:
    host: str
    username: str
    password: str
    passhash: str

    def __post_init__(self):
        if not self.host:
            raise Exception("Please enter the valid 'host' for the PRTG")

        if not self.username:
            raise Exception("Please enter the valid 'username' for the PRTG")

        if not (self.password or self.passhash):
            raise Exception(
                "Please enter at least one of 'password' or 'passhash' for the PRTG"
            )

    @property
    def auth(self):
        if self.password:
            return {"username": self.username, "password": self.password}

        return {"username": self.username, "passhash": self.passhash}

    def __str__(self):
        return f"{self.host}{self.username}"
