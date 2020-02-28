def primo(n):
    cont = 0 
    for i in range (1, n, +1):
        if n % i == 0:
            cont +=1
    if cont ==2:
        return True
    else:
        return False


def primosmenores (num):
    for i in range (1, num, +1):
        if primo (i) == True:
            print (i)

num = int (input('Informe um numero:  '))
(primosmenores(num))
