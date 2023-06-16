from pydantic import BaseSettings, Field


class UserCredentials(BaseSettings):
    first_username: str = Field(..., env="FIRST_USERNAME")
    second_username: str = Field(..., env="SECOND_USERNAME")
    first_user_password: str = Field(..., env="FIRST_USER_PASSWORD")
    second_user_password: str = Field(..., env="SECOND_USER_PASSWORD")
