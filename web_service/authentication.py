from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

from web_service.settings import UserCredentials

auth = HTTPBasicAuth()
credentials = UserCredentials()

users = {
    credentials.first_username: generate_password_hash(credentials.first_user_password),
    credentials.second_username: generate_password_hash(credentials.second_user_password),
}


@auth.verify_password
def verify_password(username: str, password: str) -> str | None:
    if username in users and check_password_hash(users.get(username), password):
        return username
