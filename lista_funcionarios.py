funcionarios = []
print("Escolha uma das Opções abaixo:")


def iniciar_valores_na_lista():
    lendo_arquivo = open('C:/Users/admin/Documents/classroom/curso_python/meu_primeiro_arquivo.txt', 'r')
    linhas = lendo_arquivo.readlines()

    funcionario = dict()

    for l in linhas:
        pessoa = l.split(';')
        funcionario['nome'] = pessoa[0]
        funcionario['sexo'] = pessoa[1]
        funcionario['salario'] = pessoa[2]
        funcionarios.append(funcionario)

def mostrar_opcoes():
    print("""
    0 - Sair do Programa
    1 - Adicionar pessoa
    2 - Listar pessoas
    3 - Somar salário dos homens
    4 - Somar salário das mulheres

    """)

def listar():
    lendo_arquivo = open('C:/Users/admin/Documents/classroom/curso_python/meu_primeiro_arquivo.txt', 'r')

    linhas = lendo_arquivo.readlines()

    for l in linhas:
        print(l)

def adicionar():
    funcionario = dict()
    funcionario['nome'] = input('Informe seu nome -> ')
    funcionario['sexo'] = input('Informe seu sexo -> ')
    funcionario['salario'] = int(input('Informe seu salario -> '))

    funcionarios.append(funcionario)

    file = open('C:/Users/admin/Documents/classroom/curso_python/meu_primeiro_arquivo.txt', 'w+')

    for funcionario in funcionarios:
        file.write('{};{};{}'.format(funcionario['nome'], funcionario['sexo'], funcionario['salario']))
        file.write('\n')

    file.close()

def salario_homem():
    salarioTotal = 0
    for pessoa in funcionarios:
        if pessoa['sexo'] == 'M':
            salarioTotal  = salarioTotal + pessoa['salario']

    print('Salario total dos homens: ', salarioTotal)

def salario_mulher():
    salarioTotal = 0
    for pessoa in funcionarios:
        if pessoa['sexo'] == 'F':
            salarioTotal  = salarioTotal + pessoa['salario']

mostrar_opcoes()
iniciar_valores_na_lista()
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
            mostrar_opcoes()

    else:
        break
