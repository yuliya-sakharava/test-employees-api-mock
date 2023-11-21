import pytest
import allure
from env_setup import ALL_EMPLOYEES_FILE
from support.json_handler import JSONHandler

existing_employee_1 = [1, {"employeeId": 1, "name": "Eddy", "organization": "IT", "role": "Lead Developer"}]
existing_employee_2 = [2, {"employeeId": 2, "name": "Jack", "organization": "Finance", "role": "Accountant"}]
existing_employee_3 = [3,
                       {"employeeId": 3, "name": "Ariel", "organization": "Marketing", "role": "Marketing Specialist"}]


@allure.description('Create new employee')
@allure.label('owner', 'Yuliya')
@allure.title('Create new employee')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("employee_id, expected_data",
                         (existing_employee_1, existing_employee_2, existing_employee_3),
                         ids=['existing_employee_1', 'existing_employee_2', 'existing_employee_3'])
@pytest.mark.smoke
def test_create_new_employee(employees_instance, employee_id, expected_data):
    employees_instance.create_new_employee(data=expected_data)


@allure.description('Fetch all employees')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch all employees')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_fetch_all_employees(employees_instance):
    employees_instance.fetch_all_employees()


@allure.description('Fetch single employee. Positive case - Fetch single existing employee')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch single employee (positive case)')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_fetch_single_employee_positive_case(employees_instance):
    employees_instance.fetch_single_employee_positive_case(
        employee_id=JSONHandler.load_json(ALL_EMPLOYEES_FILE)[0]['employeeId'],
        data=JSONHandler.load_json(ALL_EMPLOYEES_FILE)[0])


@allure.description('Fetch single employee. Negative case - Fetch single non-existing employee')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch single employee (negative case)')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_fetch_single_employee_negative_case(employees_instance):
    employees_instance.fetch_single_employee_negative_case(
        employee_id=str(len(JSONHandler.load_json(ALL_EMPLOYEES_FILE)) + 1))


@allure.description('Update single data for particular employee')
@allure.label('owner', 'Yuliya')
@allure.title('Update single field')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_single_field(employees_instance):
    employees_instance.update_single_field(
        employee_id=JSONHandler.load_json(ALL_EMPLOYEES_FILE)[0]['employeeId'],
        new_data='Ivan')


@allure.description('Update full data for particular employee')
@allure.label('owner', 'Yuliya')
@allure.title('Update all fields')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_full_employee(employees_instance):
    employees_instance.update_full_employee(
        employee_id=JSONHandler.load_json(ALL_EMPLOYEES_FILE)[0]['employeeId'],
        new_data={"name": "Jacob", "organization": "IT", "role": "Senior Developer"})


@allure.description('Delete single employee')
@allure.label('owner', 'Yuliya')
@allure.title('Delete single employee')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_delete_employee(employees_instance):
    employees_instance.delete_employee()
