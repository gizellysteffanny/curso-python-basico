from typing import List
from .models import Employee

DATABASE = 'C:/Users/admin/Documents/classroom/curso_python/meu_primeiro_arquivo.txt'


def format_date(date_as_str):
    pass


def str_to_date(date_as_str):
    pass


def transform_in_line(employee: Employee):
    return '{id};{name};{gender};{salary};\n'.format(
        id=employee.id,
        name=employee.name,
        gender=employee.gender,
        salary=employee.salary,
        age=employee.age
    )


def transform_in_employee(line: str) -> Employee:
    keys = ['id', 'name', 'gender', 'salary', 'age']
    columns = line.split(';')
    employee_as_dict = dict(zip(keys, columns))
    return Employee(**employee_as_dict)


def add_employee(path_file, employee: Employee):
    reference_file = open(path_file, 'a')
    reference_file.write(transform_in_line(employee=employee))
    reference_file.close()


def obtains_employees(path_file) -> List['Employee']:
    employees = []
    reference_file = open(path_file, 'r')
    lines = reference_file.readlines()
    for line in lines:
        employees.append(transform_in_employee(line=line))
    return employees
