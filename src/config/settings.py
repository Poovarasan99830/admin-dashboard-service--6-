# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str
#     ADMIN_API_KEY: str = "changeme"
#     SERVICE_NAME: str = "admin-dashboard-service"
    

#     class Config:
#         env_file = ".env"
        

# settings = Settings()


# src/config/settings.py
# from pydantic import BaseSettings


# class Settings(BaseSettings):
#     DATABASE_URL: str
#     ADMIN_API_KEY: str = "changeme"
#     SERVICE_NAME: str = "admin-dashboard-service"
#     database_url: str  # maps to DATABASE_URL in .env
#     app_env: str = "development"
#     secret_key: str = "change-me"

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"

# settings = Settings()


from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str          # maps to DATABASE_URL in .env
    admin_api_key: str = "changeme"
    service_name: str = "admin-dashboard-service"
    app_env: str = "development"
    secret_key: str = "change-me"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
