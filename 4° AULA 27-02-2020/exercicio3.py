def inserir_nome_lista(lista, nome):
    lista.append(nome)
    # print(lista)


def receber_lista(lista, indice):
    try:
        lista2 = [lista]
        raise IndexError
    except IndexError:
        print('Indice inexistente')
    else:
        return lista2[indice]


# Programa Principal

lista_vazia = []
nome = input('Inserir um nome na lista: ')
indice = int(input('Digite o indice: '))
# lista_vazia = inserir_nome_lista(lista_vazia, nome)
parametros = receber_lista(lista_vazia, indice)
# print(lista2)
