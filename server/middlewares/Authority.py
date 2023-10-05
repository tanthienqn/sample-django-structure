from rest_framework import exceptions
import jwt
import re
from functools import wraps
from server.settings import SIMPLE_JWT


class Authority:
    regex_bearer = re.compile(r"^[Bb]earer (.*)$")

    @classmethod
    def requires_rights(cls, rights: list):
        def requires_rights(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                header_authorization_value = args[1].headers.get("authorization")
                if not header_authorization_value:
                    raise exceptions.AuthenticationFailed("Authorization header is not present")
                match = cls.regex_bearer.match(header_authorization_value)
                if not match:
                    raise exceptions.AuthenticationFailed(
                        "Authorization header must start with Bearer followed by its token")
                token = match[1]
                data_jwt = jwt.decode(token, SIMPLE_JWT.get("VERIFYING_KEY"), algorithms=[SIMPLE_JWT.get("ALGORITHM")])
                return f(*args, **kwargs)

            return decorated

        return requires_rights
