# Um mecanismo de uma lista de dicionario

funcionarios = list({'nome': 'Gizelly', 'idade': 20})

nomes = [
    {'nome': 'Dawn', 'idade': 13},
    {'nome': 'Dick', 'idade': 13},
    {'nome': 'Nick', 'idade': 13},
    {'nome': 'Rick', 'idade': 8},
    {'nome': 'Milk', 'idade': 10}
]

for funcionario in nomes:
    funcionarios.append(funcionario)


print(funcionarios)

# profer

employees = []

add = True

while add:
    add = input('Add employees or 0 to exit ->')

    if not add == '0':
        employee = dict()
        employee['name'] = input('Input your name -> ')
        employee['age'] = int(input('Input you age -> '))

        employees.append(employee)

        add = True
    else:
        print(employees)
        break