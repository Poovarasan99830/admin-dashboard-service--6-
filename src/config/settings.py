from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ADMIN_API_KEY: str = "changeme"
    SERVICE_NAME: str = "admin-dashboard-service"

    class Config:
        env_file = ".env"

settings = Settings()
