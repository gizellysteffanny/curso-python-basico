lendo_arquivo  = open('C:/Users/admin/Documents/classroom/curso_python/meu_primeiro_arquivo.txt', 'r')

linhas = lendo_arquivo.readlines()

for l in linhas:
    print(l)
