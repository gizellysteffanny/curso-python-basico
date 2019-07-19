lista = []

print("Escolha uma das Opções abaixo:")


def showOptions():
    print("""
    0 - Sair do Programa
    1 - Adicionar pessoa
    2 - Listar pessoas
    3 - Somar salário dos homens
    4 - Somar salário das mulheres

    """)

def adicionar():
    nome = input('Informe o nome: ')
    sexo = input('informe o sexo, F para feminino ou M para masculino: ')
    salario = int(input('Informe o salario: '))

    lista.append({'nome': nome, 'sexo': sexo, 'salario': salario})


def listar():
    print(lista)

def salario_homem():
    salarioTotal = 0
    for pessoa in lista:
        if pessoa['sexo'] == 'M':
            salarioTotal  = salarioTotal + pessoa['salario']

    print('Salario total dos homens: ', salarioTotal)

def salario_mulher():
    salarioTotal = 0
    for pessoa in lista:
        if pessoa['sexo'] == 'F':
            salarioTotal  = salarioTotal + pessoa['salario']

    print('Salario total das Mulheres: ', salarioTotal)

showOptions()

while True:
    opcao = int(input("Digite a opção desejada: "))

    if not opcao == 0:

        if opcao == 1:
            adicionar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            salario_homem()
        elif opcao == 4:
            salario_mulher()
        else:
            print('Opção inválida!')
            showOptions()

    else:
        break