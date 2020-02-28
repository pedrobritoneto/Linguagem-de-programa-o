import funcao_Exercicio3


tupla1 = ()
tupla2 = ()

for i in range(3):
    n = int(input('numero: '))
    tupla1 = tupla1 + (n,)

for i in range(3):
    n = int(input('numero: '))
    tupla2 = tupla2 + (n,)

tupla3 = funcao_Exercicio3.intercala(tupla1, tupla2)
print(tupla3)
