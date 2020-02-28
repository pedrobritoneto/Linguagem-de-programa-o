continua = True
while continua:
    try:
        x = int(input('Primeiro valor: '))
        y = int(input('Segundo valor: '))
        z = x / y
        if (x <= 0 or y <= 0):
            raise ValueError
    # tratar se o denominador for zero
    except ZeroDivisionError:
        print('O segundo valor não pode ser ZERO')
    # Tratar se o valor imputado não for válido, não for um número
    except ValueError:
        print('O tipo de valor é inválido, informe um número')
    except Exception:
        print('OPA, algo errado não está certo!!!')
    # except TypeError:
        # print('O valor não pode ser negativo')
    else:
        continua = False

print('Valor da divisão é', z)
