# versao do professor
from collections import namedtuple as nt
from typing import List

DATABASE = 'C:/Users/admin/Documents/classroom/curso_python/employees.txt'

Employee = nt('Employee', ['id', 'name', 'gender', 'salary'])


def transform_in_line(employee: Employee):
    return '{id};{name};{gender};{salary};\n'.format(
        id=employee.id,
        name=employee.name,
        gender=employee.gender,
        salary=employee.salary
    )


def transform_in_employee(line: str) -> Employee:
    keys = ['id', 'name', 'gender', 'salary']
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


def main():
    option = 1

    while option != 0:
        print('1 - Add Employee')
        print('2 - List Employee')
        print('0 - Exit')
        option = int(input('Input your choice: '))

        if option == 1:
            employee = Employee(
                id=int(input('Id: ')),
                name=input('Name: '),
                gender=input('Gender: '),
                salary=input('Salary: ')
            )
            add_employee(path_file=DATABASE, employee=employee)
        elif option == 2:
            employees = obtains_employees(DATABASE)
            for e in employees:
                print("""
                    Id: {}
                    Name: {}
                    Gender: {}
                    Salary: {}
                    ---------------------------
               """.format(e.id, e.name, e.gender, e.salary))


main()
