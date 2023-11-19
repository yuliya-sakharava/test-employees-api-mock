import pytest
import allure

existing_employee_1 = [1, {"employeeId": 1, "name": "Eddy", "organization": "IT", "role": "Lead Developer"}]
existing_employee_2 = [2, {"employeeId": 2, "name": "Jack", "organization": "Finance", "role": "Accountant"}]
existing_employee_3 = [3,
                       {"employeeId": 3, "name": "Ariel", "organization": "Marketing", "role": "Marketing Specialist"}]


@allure.description('Create new employee.')
@allure.label('owner', 'Yuliya')
@allure.title('Create new employee.')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("employee_id, expected_data",
                         (existing_employee_1, existing_employee_2, existing_employee_3),
                         ids=['existing_employee_1', 'existing_employee_2', 'existing_employee_3'])
def test_create_new_employee(employees_instance, employee_id, expected_data):
    employees_instance.create_new_employee(data=expected_data)


# @allure.description('Fetch single employee. Positive case - Fetch single existing employee.')
# @allure.label('owner', 'Yuliya')
# @allure.title('Fetch single employee (positive case).')
# @allure.suite('Authorization suite')
# @allure.severity(allure.severity_level.CRITICAL)
# @pytest.mark.parametrize("employee_id, expected_data",
#                          (existing_employee_1, existing_employee_2, existing_employee_3),
#                          ids=['existing_employee_1', 'existing_employee_2', 'existing_employee_3'])
# def test_fetch_single_employee_positive_case(employees_instance, employee_id, expected_data):
#     employees_instance.fetch_single_employee_positive_case(employee_id=employee_id, data=expected_data)


# The same function, but without parameterization
# @allure.description('Fetch single employee. Positive case - Fetch single existing employee.')
# @allure.label('owner', 'Yuliya')
# @allure.title('Fetch single employee (positive case).')
# @allure.suite('Authorization suite')
# @allure.severity(allure.severity_level.CRITICAL)
# def test_fetch_single_employee_positive_case(employees_instance, read_dataset):
#     employees_instance.fetch_single_employee_positive_case(employee_id=str(read_dataset[0]["employeeId"]),
#                                                            data=read_dataset[0])
