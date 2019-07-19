from projeto2.actions import add_person, obtains_people, DATABASE
from projeto2.models import Person


def main():
    option = 1

    while option != 0:
        print('1 - Add Employee')
        print('2 - List Employee')
        print('0 - Exit')
        option = int(input('Input your choice: '))

        if option == 1:
            employee = Person(
                id=int(input('Id: ')),
                name=input('Name: ')
            )
            add_person(path_file=DATABASE, person=Person)
        elif option == 2:
            employees = obtains_people(DATABASE)
            for e in employees:
                print("""
                    Id: {}
                    Name: {}

                    ---------------------------
               """.format(e.id, e.name))


main()