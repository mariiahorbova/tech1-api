import time
import jwt
from decouple import config


JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


def token_response(token: str) -> dict:
    return {
        "access": token
    }


def create_jwt() -> dict:
    payload = {
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM]
        )
        return decoded_token if decoded_token[
                                    "expires"
                                ] >= time.time() else None
    except:
        return {}
