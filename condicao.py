idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Maior de idade')
# elif 12 <= idade < 18:
elif idade >= 12 and idade < 18:
    print('Aborrecente')
else:
    print('Criança')
