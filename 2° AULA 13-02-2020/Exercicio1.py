lista = []
for item in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)

maiornumero = max(lista)
menornumero = min(lista)
print("O maior número é", maiornumero, "e o menor número é", menornumero)
media = sum(lista) / len(lista)
print('A média é', media)
listademenores = []
for item in lista:
    if item < media:
        listademenores.append(item)
print('Os itens da lista que são menores que a média são:', listademenores)
