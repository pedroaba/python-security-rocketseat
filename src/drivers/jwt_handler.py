from datetime import datetime, timedelta, timezone

import jwt


class JwtHandler:
    def create_jwt_token(self, payload: dict = None) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(minutes=1),
                **(payload or {}),
            },
            key="my_key",
            algorithm="HS256",
        )

        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(token, key="my_key", algorithm="HS256")
        return token_information
