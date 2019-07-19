funcionarios = []

funcionario_a = {'id': 1, 'nome': 'Gizelly'}
funcionario_b = {'id': 2, 'nome': 'Luis'}

funcionarios.append(funcionario_a)
funcionarios.append(funcionario_b)


lista_com_ids_impares = [f for f in funcionarios if f['id'] % 2 == 1]

print(funcionarios)
print(lista_com_ids_impares)

numeros = [5, 2, 7, 9, 12, 7, 6, 12, 4, 6, 2, 98, 12, 54, 76, 43]
# numeros = {5, 2, 7, 9, 12, 7, 6, 12, 4, 6, 2, 98, 12, 54, 76, 43}

numeros_maiores_que_5 = [num for num in numeros if num > 5]
numeros_menores_ou_igual_a_5 = [num for num in numeros if num <= 5]

print("Lista de numeros: ", numeros)
print("Numeros maiores que 5: ", numeros_maiores_que_5)
print("Numeros menores ou igual a 5: ", numeros_menores_ou_igual_a_5)
