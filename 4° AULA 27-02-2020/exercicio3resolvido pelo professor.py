def inserir_nome(lista_nome, nome):
    lista_nome.append(nome)


def busca_nome(lista_nome, indice):
    try: 
        if indice >= len(lista_nome):
            raise IndexError
    except IndexError:
        return'Indice Inexistente'
    else:
        return lista_nome[indice]


lista_nomes = []
inserir_nome(lista_nomes, 'Pedro')
nome = busca_nome(lista_nomes, 0)
print(nome)