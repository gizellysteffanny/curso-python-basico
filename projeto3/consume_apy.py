import json
import requests


def add_employee():
    payload = {'name': 'Gizelly'}
    result = requests.post(url='http://192.168.43.45:8000/api/sale/employee/', data=payload)

    print('status code: {}'.format(result.status_code))
    result_json = json.loads(result.content.decode('utf-8'))

    print(
        'Id: {}'.format(result_json.get('id')),
        'Name: {}'.format(result_json.get('name'))
    )


def list_employee():
    result = requests.get(url='http://192.168.43.45:8000/api/sale/employee/')

    print('status code: {}'.format(result.status_code))
    result_json = json.loads(result.content.decode('utf-8'))

    for person in result_json:
        print(
            'Id: {}'.format(person.get('id')),
            'Name: {}'.format(person.get('name'))
        )


def get_employee():
    result = requests.get(url='http://192.168.43.45:8000/api/sale/employee/3')

    print('status code: {}'.format(result.status_code))
    result_json = json.loads(result.content.decode('utf-8'))

    print(
            'Id: {}'.format(result_json.get('id')),
            'Name: {}'.format(result_json.get('name'))
    )


def add_moviment():
    payload = {'value': 543.50, 'address': '127.0.0.1', 'operation': 'C', 'employee': 3}
    result = requests.post(url='http://192.168.43.45:8000/api/sale/movement/', data=payload)

    print('status code: {}'.format(result.status_code))
    result_json = json.loads(result.content.decode('utf-8'))

    print(
        'Id: {}'.format(result_json.get('id')),
        'Address: {}'.format(result_json.get('address')),
        'Value: {}'.format(result_json.get('value')),
        'Operation: {}'.format(result_json.get('operation')),
        'Employee: {}'.format(result_json.get('employee'))
    )

# add_employee()


list_employee()
get_employee()
add_moviment()
