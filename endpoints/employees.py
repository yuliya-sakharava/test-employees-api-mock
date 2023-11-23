import json
import requests
from env_setup import PATH_SINGLE_EMPLOYEE, PATH_ALL_EMPLOYEES, ALL_EMPLOYEES_FILE
from support.json_handler import JSONHandler
import jsonschema
import allure
from endpoints.base import BaseAPI
from support.logger import log_func


class Employees(BaseAPI):
    LOG = log_func()

    def __init__(self, session: requests.Session, url: str, token):
        super().__init__(session, url)
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    @allure.step("Add new employee(s)")
    def create_new_employee(self, data):
        response = self.session.post(self.url, headers=self.headers, json=data)
        assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
        assert response.json() == data, f"Failed. Actual response: {response.json()}, but expected {data}"
        jsonschema.validate(response.json(), JSONHandler.load_json(PATH_SINGLE_EMPLOYEE))
        self.LOG.info(f"Test employee {data} has been created")
        current_data = JSONHandler.load_json(ALL_EMPLOYEES_FILE)
        current_data.append(data)
        JSONHandler.dump_json(ALL_EMPLOYEES_FILE, current_data)
        self.LOG.info(
            f"Test data has been added to the all_employees.json file. You can find the file here: {ALL_EMPLOYEES_FILE}")

    @allure.step("Fetch all employees")
    def fetch_all_employees(self, data):
        response = self.get(self.url, headers=self.headers)
        assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
        assert response.json() == data, f"Failed. Actual response: {response.json()}, but expected {data}"
        jsonschema.validate(response.json(), JSONHandler.load_json(PATH_ALL_EMPLOYEES))
        self.LOG.info(f"All existing test employees has been fetched: {data}")

    @allure.step("Fetch single employee - positive case (existing employee)")
    def fetch_single_employee_positive_case(self, employee_id, data):
        response = self.get(url=f"{self.url}/{employee_id}", headers=self.headers)
        assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
        assert response.json() == data, f"Failed. Actual response: {response.json()}, but expected {data}"
        jsonschema.validate(response.json(), JSONHandler.load_json(PATH_SINGLE_EMPLOYEE))
        self.LOG.info(f"Existing test employee employeeId={employee_id} has been fetched")

    @allure.step("Fetch single employee - negative case (non-existing employee)")
    def fetch_single_employee_negative_case(self, employee_id):
        response = self.get(url=f"{self.url}/{employee_id}", headers=self.headers)
        assert response.status_code == 404
        assert response.json() == {"error": "Employee not found"}
        self.LOG.info(f"An attempt was made to get a non-existent test employee employeeId={employee_id}")

    @allure.step("Update single field")
    def update_single_field(self, employee_id, new_data):
        data = {'name': f"{new_data}"}
        response = self.session.patch(f"{self.url}/{employee_id}", headers=self.headers, json=data)
        assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
        assert response.json() == {'message': 'Employee updated'}
        self.LOG.info(
            f"Existing test employee employeeId={employee_id} has been partially updated. Updated data: {data}")

    @allure.step("Update full employee data")
    def update_full_employee(self, employee_id, new_data):
        response = self.session.put(f"{self.url}/{employee_id}", headers=self.headers, json=new_data)
        assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
        assert response.json() == {'message': 'Employee updated'}
        self.LOG.info(f"Test employee employeeId={employee_id} has been fully updated. Updated data: {new_data}")

    @allure.step("Delete single employee")
    def delete_employee(self):
        for employee_id in range(1, (len(JSONHandler.load_json(ALL_EMPLOYEES_FILE)) + 1)):
            response = self.session.delete(f"{self.url}/{employee_id}", headers=self.headers)
            assert response.status_code == 200, f"Status code should be 200, but received {response.status_code}"
            assert response.json() == {'message': 'Employee deleted'}
            self.LOG.info(f"Test employee employeeId={employee_id} has been deleted")
        JSONHandler.dump_json(ALL_EMPLOYEES_FILE, [])
        self.LOG.info(f"The file all_employees.json has been cleared. You can find the file here: {ALL_EMPLOYEES_FILE}")
