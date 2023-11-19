import pytest
import requests
from env_setup import Credentials, Endpoints
from support.custom_errors import TokenNotFoundError, TokenNotGeneratedError
from endpoints.employees import Employees


# from support.logger import log_func
# import json
# import time
# from env_setup import PATH_SINGLE_EMPLOYEE, PATH_ALL_EMPLOYEES, PATH_DATASET


@pytest.fixture(scope="session")
def create_session():
    yield requests.Session()


@pytest.fixture(scope="session")
def credentials():
    return Credentials.get_env_variables()


@pytest.fixture(scope="session")
def bearer_token(credentials):
    response = requests.post(f"{Endpoints.TOKEN_URL}",
                             json={"username": credentials.APP_USERNAME, "password": credentials.APP_PASSWORD},
                             headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        token = response.json().get("token")
        if token is None:
            raise TokenNotFoundError
        yield token
    else:
        raise TokenNotGeneratedError(response.status_code)


@pytest.fixture()
def employees_instance(create_session, bearer_token):
    yield Employees(create_session, Endpoints.EMPLOYEES_URL, bearer_token)
