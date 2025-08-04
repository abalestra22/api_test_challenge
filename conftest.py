import os
import pytest

@pytest.fixture(scope="session")
def api_token():
    return os.getenv("API_TOKEN", "xxx")

@pytest.fixture(scope="session")
def db_credentials():
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "dbname": os.getenv("DB_NAME", "worldsys_db"),
        "user": os.getenv("DB_USER", "admin"),
        "password": os.getenv("DB_PASSWORD", "your-password"),
        "port": int(os.getenv("DB_PORT", 5432)),
    }
