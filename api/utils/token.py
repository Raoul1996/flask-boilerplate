from itsdangerous import URLSafeTimedSerializer
from api.config import config


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(config["base"].SECRET_KEY)
    return serializer.dumps(email, salt=config["base"].SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config["base"].SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=config["base"].SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except Exception:
        return False
    return email
