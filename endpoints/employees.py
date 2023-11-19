import requests
from env_setup import PATH_SINGLE_EMPLOYEE
from support.json_handler import JSONHandler
import jsonschema
# from env_setup import PATH_SINGLE_EMPLOYEE, PATH_ALL_EMPLOYEES
import allure
from endpoints.base import BaseAPI


class Employees(BaseAPI):

    def __init__(self, session: requests.Session, url: str, token):
        super().__init__(session, url)
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    @allure.step("Add new employee.")
    def create_new_employee(self, data):
        response = self.session.post(self.url, headers=self.headers, json=data)
        assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
        assert response.json() == data, f"Failed. Actual response: {response.json()}, but expected {data}"
        jsonschema.validate(response.json(), JSONHandler.load_json(PATH_SINGLE_EMPLOYEE))

    # @allure.step("Fetch single employee - positive case (existing employee).")
    # def fetch_single_employee_positive_case(self, employee_id, data):
    #     response = self.get(url=f"{self.url}/{employee_id}", headers=self.headers)
    #     assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
    #     assert response.json() == data, f"Failed. Actual response: {response.json()}, but expected {data}"
    #     jsonschema.validate(response.json(), JSONHandler.load_json(PATH_SINGLE_EMPLOYEE))

    # @allure.step("Fetch single employee - negative case (non-existing employee).")
    # def fetch_single_employee_negative_case(self, employee_id):
    #     response = self.get(url=f"{self.url}/{employee_id}", headers=self.headers)
    #     assert response.status_code == 404
    #     assert response.json() == {"error": "Employee not found"}
