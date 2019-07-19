from datetime import datetime
from projeto1.actions import *


class Employee:

    def __init__(self, id, name, age, gender, salary, date_birth):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.date_birth = date_birth

    def __str__(self):
        return '{} - {}'.format(self.name, self.age)

    @property
    def age(self):
        now = datetime.now().date()
        diff = now - str_to_date(self.date_birth)
        return (diff / 365).days
