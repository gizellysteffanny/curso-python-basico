from functools import partial


def funcao(a, b):
    return a + b

print(funcao(10, 5))

funcao_anonima = lambda a, b : a + b
print(funcao_anonima(100, 300))

#  Funcao delegate
def funcao_a_b_c(funcao, a, b, c):
    return funcao(a, b) + c

print(funcao_a_b_c(funcao, 10, 34, 94))


# Função parcial
def multiplicacao(a,b,c):
	return a * b * c

partial(multiplicacao, 39, 87)

nova_funcao = partial(multiplicacao, 18, 22)

print(nova_funcao(54))

# Funções Parâmentros como Lista

def funcao(*args):
	soma = 0
	for x in args:
		soma += x
		return soma

funcao(1,2,3)

1# Funções Parâmentros como Dicionario

def soma(a, b):
	return a + b

def funcao(**parametros):
	return soma(**parametros)

funcao(a=10, b=15)
