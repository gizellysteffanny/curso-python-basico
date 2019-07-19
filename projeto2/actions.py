from typing import List
from projeto2.models import Person

DATABASE = 'C:/Users/admin/Documents/classroom/curso_python/projeto2/database.txt'


def transform_in_line(person: Person):
    return '{id};{name};\n'.format(
        id=person.id,
        name=person.name
    )


def transform_in_person(line: str) -> Person:
    keys = ['id', 'name']
    columns = line.split(';')
    person_as_dict = dict(zip(keys, columns))
    return Person(**person_as_dict)


def add_person(path_file, person: Person):
    reference_file = open(path_file, 'a')
    reference_file.write(transform_in_line(person=person))
    reference_file.close()


def obtains_people(path_file) -> List['Person']:
    people = []
    reference_file = open(path_file, 'r')
    lines = reference_file.readlines()
    for line in lines:
        people.append(transform_in_person(line=line))
    return people
