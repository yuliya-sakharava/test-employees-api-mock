from dataclasses import dataclass
from dotenv import load_dotenv
import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
PATH_SINGLE_EMPLOYEE = os.path.join(ROOT_PATH, "schemas", "single_employee.json")
SECRET_FILE = os.path.join(ROOT_PATH, "secrets", "secrets.json")


@dataclass
class Credentials:
    load_dotenv()
    APP_USERNAME: str = os.getenv("APP_USERNAME")
    APP_PASSWORD: str = os.getenv("APP_PASSWORD")

    @classmethod
    def get_env_variables(cls):
        if not Credentials.APP_USERNAME or not Credentials.APP_PASSWORD:
            raise "CredsNotFoundError"

        return cls(Credentials.APP_USERNAME, Credentials.APP_PASSWORD)


@dataclass
class Endpoints:
    BASE_URL: str = "https://employees-api-i9ae.onrender.com"
    TOKEN_URL: str = f"{BASE_URL}/generate-token"
    EMPLOYEES_URL: str = f"{BASE_URL}/employees"
