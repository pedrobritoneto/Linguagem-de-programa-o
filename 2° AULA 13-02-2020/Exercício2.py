from random import randint


dados = []
for i in range(10):
    n = randint(1, 6)
    dados.append(n)

print(dados)
for item in range(1, 7):
    print('O número', item, 'Aparece', dados.count(item), 'vezes')
